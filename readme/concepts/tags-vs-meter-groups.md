# Tags vs Meter Groups



Both tags and meter groups let you aggregate data from multiple meters - so what's the difference and when do we use tags and when do we use meter groups?

There are many places where you can choose to use either.

In the above example you could have created meter groups for each of 'Sunbucks Ground Floor' and 'Sunbucks 3rd Floor' and used that instead and then created another one for 'Sunbucks' that added Ground Floor and 3rd Floor.

The advantage of tags is that its easier to setup and configure. Its also easy to view and analyze data in a tree-like structure. It gives you an explicit relationship whereas meter groups are a flat list of objects.

However, if your grouping logic is not purely adding together - if you need to apply scaling factors or subtract certain meter consumption values, then you can't purely use tags for that. You need to use virtual meters or meter groups.

(You could then tag that meter group subsequently)
