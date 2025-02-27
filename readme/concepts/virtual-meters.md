# Virtual Meters

Virtual meters - or 'soft meters' - a meters that are defined in the software layer and have values that are derived from one more more physical meters. Often, a building may not have meters for every subsystem that needs to be measured - however you can often calculate the energy value for that subsystem by deriving the data from other pyhsical meters.

For example, if a floor has a meter for it (lets call it F1), and each of the units within the floor has its own meter (lets call them U1 and U2), then we can measure the total energy into the floor as well as the energy into each individual unit.

But what about the energy consumed by the common area on the floor? There's no separate meter to measure that. However we can _calculate_ it by taking the consumption from F1 and subtracting the consumptions from U1 and U2. The remaining energy is the energy of the common areas in the floor.

In this case, you can define a virtual meter called 'CA1' to represent energy consumption of common areas. And you can configure it to be based on the formula `F1 - U1 - U2`

When configuring virtual meters, you need to specify a serving location, name and tags. In addition you need to specify what meters this virtual meter derives its data from and the scaling factor for each of those meters.

Using the example above - `F1 - U1 - U2`, you would add the following 3 meters and corresponding scaling factor:

| Meter | Scaling Factor |
| ----- | -------------- |
| F1    | 1              |
| U1    | -1             |
| U2    | -1             |

#### Units for virtual meters

Virtual meters can be calculated from meters that have different units. All consumption for virtual meters are stored in the utility type's base unit. So if you have defined a virtual water meter and the `water` utility type has 'Imperial Gallons' as the base unit (ie, conversion factor of the unit is 1), then all of the virtual meter consumption data is calculated in Imperial Gallons regardless of the units of the meters that the virtual meter is dervied from.

#### Calculating consumption

Consumptions for virtual meters are automatically calculated whenever consumption data is recorded in any of the underlying meters.
