# Configuring Meters

Once you have setup your utility types you can start adding and configuring meters.

{% hint style="info" %}
Here 'meters' refers to physical metres - that will record consumption data
{% endhint %}



Go to the Configuration section in the application and under 'Meters' you can start adding meters.



The Meters section shows a list of all physical meters you have configured. You can click 'Add Item' on the top to register a new meter. You can edit each meter by clicking the 'edit' icon on the right side of each meter.



## Configuring Meters

When adding a new meter you need to specify the following details:

1. Meter Name - a name to help you identify this meter. You can give any name you want but it should be unique. You won't be allowed to create multiple meters with the same name
2. Description - a brief descriptoin of this meter - only for your informational purpose. This is not used by the application
3. Meter Type - what kind of meter this is - you will pick one of the utility types you configured earlier (example: energy or water or waste)
4. Unit - what unit this meter records data in. This is important because when data is uploaded/sent/recorded for this meter, it is assumed to be in the unit you specify here. So if your base unit is 'kwh' but the meter being configured uses btu, then specify btu as the unit.  When data gets recorded, it will automatically be converted from btu to kwh when data gets received and stored.
5. Serving Location - what location this meter serves. When you anayze consumption data by location, this location data is used to determine what meters serve and contribute to a specific location.
6. Tags - you can apply multiple tags to a meter. Tags need to be predefined. See the [configuring-tags.md](configuring-tags.md "mention") section for more information on how tags work.\
   To add a new tag, click the 'Add Tag' button, then choose a tag type. \
   Once you choose a tag type - you will be presented with a list of possible tags for that tag type. You can pick one to apply it.\
   You can pick one tag of each type but you can add any number of tag types you want.
7. Baselines. You can configure baseline values for each baseline that you have defined. These are daily consumption baseline values. See  the section on configuring baselines for more information
   1. Metadata - You can configure various custom fields under the 'metadata' section. Custom fields are defined under the metadata configuration section which is in the 'Advanced' section.&#x20;

{% hint style="info" %}
All changes are saved only when you hit the 'Submit' button. None of your edits are saved until you do that.
{% endhint %}

