# Readings, Consumption and Demand



So we know that meters can record consumption data and that both virtual meters and meter groups can calculate consumption based on the underlying meters and their scaling multipliers.

So this means, only physical meters can _record_ consumption. For the other entities, consumption is _calculated_

How do you record consumption for a physical meter? There are a few ways:&#x20;

1. Record meter readings
2. Record consumption
3. Record load/demand

### Recording Meter Readings

By recording meter readings - meter readings are meant to be literally that - the reading on the actual physical meter. This will be a cummulative value that always increases. As readings get recorded, the consumption is calculated as the difference between the current reading and the previous readings.

Consumption data is interpolated over the time from the last reading to the current reading and the change in consumption is assumed to be linear in this time interval.

In order to ensure accuracy, make sure the interval between readings isn't too long.

Readings can be recorded in a few ways:

1. API
2. Built-in Integration
3. Manually entering a reading in the interface

See the 'Integrations' section for more information.



### Recording Consumption

Sometimes, meters may not give you the cumulative reading. For example, if you're recording data from an IoT energy meter, you may receive the actual consumption for a given time period. Its possible to directly record that consumption data as well. This can be done through the meter's API.



### Recording Load or Demand

Some times with energy meters it may give you the current instantaneous _demand_. Consumption can be automatically calculated from the instantaenous demand.

When demand readings are recorded, the consumption is calculated for the period between two demand readings by calculating the 'area under the curve'. Trapezium rule is used, assuming linear growth in consumption between the two demand readings.

That consumption is then interpolated in linear fashion across the time period.
