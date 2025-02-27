#!/usr/bin/env python3
import os
import openai
import glob
import yaml
import git
from pathlib import Path
import time
import shutil
from openai import OpenAI

# Set up OpenAI client
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

# Define paths
source_dir = 'source-repo'
dest_dir = 'thai-repo'

# Configure git for the destination repo
thai_repo = git.Repo(dest_dir)
thai_repo.git.config('user.name', 'GitHub Action Bot')
thai_repo.git.config('user.email', 'action@github.com')

# Clear destination directory content (except .git)
for item in os.listdir(dest_dir):
    if item != '.git':
        item_path = os.path.join(dest_dir, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
        else:
            os.remove(item_path)

# File extensions to translate
text_extensions = ['.md', '.txt', '.html', '.json', '.yaml', '.yml', '.py', '.js', '.jsx', '.ts', '.tsx', '.css', '.scss']

# Files to skip
skip_files = ['.git', 'node_modules', '.github/workflows', '.env']

def should_translate(filepath):
    """
    Determine if a file should be translated based on its path and extension.
    
    Args:
        filepath (str): Path to the file
        
    Returns:
        bool: True if the file should be translated, False otherwise
    """
    # Check if the file should be skipped
    for skip_pattern in skip_files:
        if skip_pattern in filepath:
            return False
    
    # Check if the extension is in the list to translate
    _, ext = os.path.splitext(filepath)
    return ext.lower() in text_extensions

def translate_text(text):
    """
    Translate text from English to Thai using OpenAI API.
    
    Args:
        text (str): Text to translate
        
    Returns:
        str: Translated text
    """
    if not text.strip():
        return text
        
    try:
        response = client.chat.completions.create(
            model='gpt-4',
            messages=[
                {'role': 'system', 'content': 'You are a professional translator. Translate the following content from English to Thai. Preserve all formatting, code structure, and special characters.'},
                {'role': 'user', 'content': text}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f'Translation error: {e}')
        # If we get rate-limited, wait a bit and try again
        if 'rate limit' in str(e).lower():
            time.sleep(60)
            return translate_text(text)
        return text

def main():
    """Main function to handle the translation process."""
    print(f"Starting translation from {source_dir} to {dest_dir}...")
    
    # Process all files in the source directory
    for file_path in glob.glob(f'{source_dir}/**/*', recursive=True):
        # Skip directories
        if os.path.isdir(file_path):
            continue
            
        # Get the relative path
        rel_path = os.path.relpath(file_path, source_dir)
        dest_path = os.path.join(dest_dir, rel_path)
        
        # Create directories if they don't exist
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        
        if should_translate(file_path):
            try:
                print(f'Translating {rel_path}')
                with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
                    content = file.read()
                    
                translated_content = translate_text(content)
                
                with open(dest_path, 'w', encoding='utf-8') as file:
                    file.write(translated_content)
            except Exception as e:
                print(f'Error processing {rel_path}: {e}')
                # Just copy the file if we can't translate it
                shutil.copy(file_path, dest_path)
        else:
            # Copy binary files and others we're not translating
            shutil.copy(file_path, dest_path)

    # Commit and push changes
    try:
        thai_repo.git.add('.')
        
        # Only commit if there are changes
        if thai_repo.git.status('--porcelain'):
            thai_repo.git.commit('-m', 'Update Thai translation')
            
            # Check if the branch exists remotely
            try:
                # Try to get remote branches
                remote_branches = [ref.name for ref in thai_repo.remote().refs]
                current_branch = thai_repo.active_branch.name
                remote_branch = f'origin/{current_branch}'
                
                # If branch doesn't exist remotely, we need to set upstream
                if remote_branch not in remote_branches:
                    print(f"Branch '{current_branch}' doesn't exist in remote. Creating it...")
                    thai_repo.git.push('--set-upstream', 'origin', current_branch)
                else:
                    thai_repo.git.push()
            except Exception as branch_err:
                print(f"Error checking remote branches: {branch_err}")
                # Fallback: try push with --set-upstream
                thai_repo.git.push('--set-upstream', 'origin', thai_repo.active_branch.name)
                
            print('Changes committed and pushed to destination repository.')
        else:
            print('No changes to commit.')
    except Exception as e:
        print(f'Git operation error: {e}')

    print('Translation process completed.')

if __name__ == "__main__":
    main()
