# Baselines

Baselines let you track your actual consumption against an idea consumption.

What is the ideal consumption? It depends on your needs!

Your ideal consumption maybe whatever you recorded as consumption at a specific point in time in the past and you want to compare how your current consumption tracks against that.

Your ideal consumption could be based on some regulatory or compliance-based standard that you are looking to adhere to.

You can define multiple baselines  - some may be based on your internal standards for what consumption should be like and others could be to track against country or global standards based on your building type.



### Why do I need to define baselines?

The main reason to define baselines is to easily generate analytics and view data on how your current consumption tracks against some fixed baseline.



### How do baselines work?

You can define multiple baselines. You first need to give a name for your baseline. And then configure corresponding values for your baseline.

There are a few rules for how they work:

1. A single baseline can be applied to multiple utility types. So you can define a baseline called 'My Company Internal Baseline' and set different baseline values for water consumption and energy consumption and gas consumption
2. Each meter, virtual meter, group, tag or location can have a baseline value attached to it. You can define specific baseline values for each entity. The baselines may differ wildly between them based on the nature of the item. For example, a meter recording the lighting across the entire building will have a different baseline from a meter recording the plug load in floor 3.
3. Baselines are optional - you can choose not to configure values for some or all entities
4. Baselines are configured as a daily consumption value. When doing analytics, the system will calculate what the baseline should be for the date period you choose based on the daily value that you configure.



