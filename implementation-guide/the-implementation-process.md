# The Implementation Process

How you implement a utility monitoring system will vary depending on:

1. How many meters you have
2. How big an area or building (or multiple buildings) you plan on monitoring



{% hint style="info" %}
For the purpose of explanation - we will be using energy monitoring as an example but the same concepts will apply for every other utility type as well.
{% endhint %}



## Methodology

Setting up UMS can be done with  either a simple implementation or a complex implementation.

Both use the same concepts and the outcomes are the same but complex implementations require more configuration and planning. Which one you use depends on how physical meters are installed and setup for the  workplace/office/building/precinct that is being monitored.



## Complex Implementation

In a complex implementation, physical meters are typically installed in a meter tree configuration.

This means you have meters and some meters have sub-meters under it and those sub-meters can have their own sub-meters.

Futher, different meters can represent different catgories of energy consumption.

For example, you may have a meter that measures electricity to plug points and another that measures electricity for the AHU and cooling systems.

In a complex implementation, meters may not be completely independent of other meters.

You will need to define tags and meter groups and virtual meters to capture fine-grained information about how the consumption is distributed.



## Simple Implementation

In a simple implementation you have a few meters that directly measure energy for specific areas.

There is no overlap in consumption readings between different meters. Each is independent.

You may use tags to aggregate data from multiple meters that need to be logically grouped together.
