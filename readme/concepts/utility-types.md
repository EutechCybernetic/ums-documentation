# Utility Types



Utility types define the kinds of utilties you want to measure and analyize. These are typically:

* Electricity
* Water
* Gas
* Chilled Water
* Waste etc...

You can add these utility types into the system. Each utility type can be measured in different units. You can configure different units for each utility type. For example, electricity can be recorded in kWh or mWh or BTU.

#### Units

Within each utility type, you need to define the possible units they can be measured in. For each unit - you need to give a name and a conversion factor. The conversion factor is a multiplier to convert that unit to the base unit.

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

###
