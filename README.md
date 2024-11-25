# Utility Management System

The iviva Utility Management System (UMS) is an application and service to manage data and provide analytics related to utility resources.

What are utility resources?

Broadly speaking - any resource that can be *consumed* and *metered* could be considered a utiltiy resource.

Some examples are:

* Electricity
* Water
* Gas
* Waste
* Internet Bandwidth
* Fuel
* Oxygen


These are some of the resources for which data can be managed in the UMS application.

# Overview


The UMS application can manage multiple types of utilities as mentioned in the previous section.

Consumption data - including meter readings - can be fed into the system either via API or Mqtt.
Other integrations are also available for ingesting data.
Using Lucy, its possible to read consumption data from invoice PDFs and images and feed them into the application as well.


Once data is ingested, the application will calculate and store consumption data and other metrics, using interpolation where required.

You can then track consumption data across many dimensions including date ranges, tags, and base lines.


# Concepts
This section describes the main concepts used in the UMS application.

## Utility Types

Utility types define the kinds of utilties you want to measure and analyize.
These are typically:

* Energy
* Water
* Gas
* Chilled Water
* Waste
etc...

You can add these utility types into the system.
Each utility type can be measured in different units. You can configure different units for each utility type.
For example, energy can be recorded in kWh or mWh or BTU.

### Units
Within each utility type, you need to define the possible units they can be measured in.
For each unit - you need to give a name and a conversion factor.
The conversion factor is a multiplier to convert that unit to the base unit.

You can define a base unit by giving the conversion factor as one.

For example, if you are storing water volumes, you may want to configure the following units:

* litres
* US gallons
* Imperial gallons

If we choose litres is the base unit, then the following conversion factors can be used:

* litres - 1
* US gallons - 3.785
* Imperial Gallons - 4.546


If we wanted to choose US Gallons as the base unit, the following conversion factors can be used:

* litres - 0.2642 (1/3.785)
* US Gallons - 1
* Imperial Gallons - 1.20095


## Meters
Physical meters are entities that record consumption.
As the name suggest, you would typically map these to real world physical meters that you have.
Readings can then be recorded against the meters at regular intervals and those are the raw data points that drive all the analytics.


If your building has one 3 energy meters and 1 water meter, you would register 3 meters as energy meters and 1 meter as a water meter.

Each meter has a few properties that can be configured:

1. The utility type (is it an energy meter? or water meter? or something else?)
2. A name - can be anything descriptive
3. Units - what units this meter uses for recording and showing readings.
4. A location - what location this meter is tied to. Meters can be tied to individual units, a floor or an entire building. You would typically pick the location that is *served* by this particular meter.
5. Tags - you can tag meters with arbitrary tags that you pre-define. See the section on Tagging for more information on why you would want to do that
6. Baseline configuration - configure daily baseline values for each meter - see the baseline section for more information.

You can record readings for meters in several ways including manually entering the reading, uploading a csv file, uploading a bill or integration with IoT and BMS systems.

## Virtual Meters
Virtual meters - or 'soft meters' - a meters that are defined in the software layer and have values that are derived from one more more physical meters.
Often, a building may not have meters for every subsystem that needs to be measured - however you can often calculate the energy value for that subsystem by deriving the data from other pyhsical meters.

For example, if a floor has a meter for it (lets call it F1), and each of the units within the floor has its own meter (lets call them U1 and U2), then we can measure the total energy into the floor as well as the energy into each individual unit.

But what about the energy consumed by the common area on the floor?
There's no separate meter to measure that.
However we can *calculate* it by taking the consumption from F1 and subtracting the consumptions from U1 and U2.
The remaining energy is the energy of the common areas in the floor.

In this case, you can define a virtual meter called 'CA1' to represent energy consumption of common areas.
And you can configure it to be based on the formula `F1 - U1 - U2`

When configuring virtual meters, you need to specify a serving location, name and tags.
In addition you need to specify what meters this virtual meter derives its data from and the scaling factor for each of those meters.

Using the example above - `F1 - U1 - U2`, you would add the following 3 meters and corresponding scaling factor:

| Meter | Scaling Factor|
|------|-------|
| F1 |  1 |
| U1 | -1 |
| U2 | -1 |



### Units for virtual meters
Virtual meters can be calculated from meters that have different units.
All consumption for virtual meters are stored in the utility type's base unit.
So if you have defined a virtual water meter and the `water` utility type has 'Imperial Gallons' as the base unit (ie, conversion factor of the unit is 1), then all of the virtual meter consumption data is calculated in Imperial Gallons regardless of the units of the meters that the virtual meter is dervied from.

### Calculating consumption
Consumptions for virtual meters are automatically calculated whenever consumption data is recorded in any of the underlying meters.


## Meter Groups
While virtual meters allow you to define a soft meter that has a calcualted value based on one or more physical meters, Meter Groups allow you define more complex groupings. A Meter group can consist of multiple physical meters, virtual meters and other meter groups as well.
And each item added to the group can have an associated multiplier factor.

Like virtual meters, meter groups also keep track of consumption as a calculation of other meters. However unlike virtual meters, meter groups can also refer to other virtual meters and other meter groups.

Just like virtual meters, meter groups don't have units associated and consumption is calculated whenever the underlying physical meters receive consumption data.

## Readings, Consumption and Demand
So we know that meters can record consumption data and that both virtual meters and meter groups can calculate consumption based on the underlying meters and their scaling multipliers.

So this means, only physical meters can *record* consumption. For the other entities, consumption is *calculated*

How do you record consumption for a physical meter?
There are a few ways:
By recording meter readings - meter readings are meant to be literally that - the reading on the actual physical meter. This will be a cummulative value that always increases.
As readings get recorded, the consumption is calculated as the difference between the current reading and the previous readings.

Consumption data is interpolated over the time from the last reading to the current reading and the change in consumption is assumed to be linear in this time interval.

In order to ensure accuracy, make sure the interval between readings isn't too long. 

Readings can be recorded in a few ways:
1. API
2. Built-in Integration
3. Manually entering a reading in the interface

See the 'Integrations' section for more information.

Sometimes, meters may not give you the cummulative reading.
For example, if you're recording data from an IoT energy meter, you may receive the actual consumption for a given time period.
Its possible to directly record that consumption data as well.
This can be done through the meter's API.


Some times with energy  meters it may give you the current instantaneous *demand*.
The ability to calculate consumption from demand will be available in a future release.

## Tags
Tags are a useful feature to organize and catalog utility consumption data in various custom and arbitrary ways.
You can apply multiple tags to meters, virtual meters or meter groups.
You can then analyze consumption data by tags.
All meters that have the same tag will have their consumption data aggregated together.
For example, if there are multiple tenants in a building and they each have mutiple meters, you can tag different meters or meter groups with the tenant name, and then analyze the consumption data based on the tenant name.

In order to provide structure and ensure data is clean, you need to pre-define your tags.

You start by defining a 'tag type' - for example 'Tenant'.
You can then define multiple items under the 'Tenant' tag. You can add a tag for each tenant - 'ACME', 'Blueberry Electronics', 'Verper Stationary' etc..

What makes tags more interesting is that they can follow a hierarchial tree structure.

### Tag Trees
You can define tags with parent and child tags.
You can create tags and subtags and sub-sub tags and keep going on.
The advantage of this is that when you want to analyze consumption data for a tag, it will automatically include all sub-tags (or child tags) as well.
For example, if the 'Sunbucks Coffee' tenant has 2 different shops in a commercial building, you can define a tag structure for tenants like this:

* Tenant
    * Food and Beverage
        * Sunbucks Coffee
            * Ground Floor
            * 3rd Floor
        * Don Pepe

You can then tag the meters as either `Tenant/Food and Beverage/Sunbucks Coffee/Ground Floor` or `Tenant/Food and Beverage/Sunbucks Coffee/3rd Floor`.

You can either analyze data for each individual meter, or if you choose to analyze data for `Tenants/Food and Beverage/Sunbucks Coffee`, data from `Ground Floor` and `3rd Floor` will autoamtically be included in it.

If you analyze data for the tag `Tenant/Food and Beverage` it will also include consumption data from `Don Pepe` tagged meters as well.

Having a tree structure lets you segregate and analyze data individually or as a group.



### Tags vs Meter Groups
Both tags and meter groups let you aggregate data from multiple meters - so what's the difference and when do we use tags and when do we use meter groups?

There are many places where you can choose to use either. 

In the above example you could have created meter groups for each of 'Sunbucks Ground Floor' and 'Sunbucks 3rd Floor' and used that instead and then created another one for 'Sunbucks' that added Ground Floor and 3rd Floor.

The advntage of tags is that its easier to setup and configure. Its also easy to view and analyze data in a tree-like structure. It gives you an explicit relationship whereas meter groups are a flat list of objects.

However, if your grouping logic is not purely adding together - if you need to apply scaling factors or subtract certain meter consumption values, then you can't purely use tags for that. You need to use virtual meters or meter groups.

(You could then tag that meter group subsequently)

## Meter Trees

## Meter Readings vs Consumption

## Metrics and Analytics

## Baselines and Benchmarks

## Resetting Meters


# Getting Started

# Data Modelling

# Analytics

# Integrations






