# Complex Implementations

The first step to executing a complex implementation is understanding the meter hierarchy.

## Understanding Meter Hierarchies

A meter tree or meter hierarchy refers to the structured arrangement of energy meters (e.g., electricity, gas, water) in a parent-child relationship to represent how energy usage is measured and aggregated within a facility, campus, or network.&#x20;

This hierarchy helps in tracking, analyzing, and optimizing energy consumption at different levels of granularity.



This is an example of a meter hierarchy

<figure><img src="../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

A meter hierarchy is typically organized into multiple levels:

* Root Meter - This is the main feed into the building or workplace
* Intermediate Meters - Represents divisions like floors
* Leaf Meters - Represents specific equipment or rooms or tenants

Consumption data is rolled up from child meters to their parent meters.



### Some examples of a meter hierarchy:

#### Simple Building Example

* Main Meter (Root):&#x20;
  * Measures total energy consumed by the building.
* Sub-Meters (Intermediate):
  * Measure energy used by specific floors.
* Equipment Meters (Leaf):
  * Measure energy consumed by HVAC systems, lighting, and elevators.

#### Industrial Facility

* Main Utility Meter:
  * Tracks the total energy supplied to the facility.
* Area Meters:
  * &#x20;Separate meters for production lines, office spaces, and storage areas.
*   Equipment Meters:

    * Sub-meters for high-energy equipment like boilers, compressors, or ovens.



## Modeling Meter Hierarchies

The UMS application provides a few tools for modeling and managing meter hierarchies.

### Physical Meters

These represent actual meters that are present and provide readings.

[See the concept section on physical meters for more information.](complex-implementations.md#physical-meters)

### Virtual Meters

These are calculated meters.

Use these to add soft meters that represent consumption that you want to track but where physical meters don't exist.

[See the concept section on virtual meters for more information.](complex-implementations.md#virtual-meters)



### Meter Groups

These are similar to virtual meters but can also reference other virtual meters and other meter groups.

[See the concept section on meter groups for more information](complex-implementations.md#meter-groups)

### Tags

Tags provide a flexible mechanism for organizing meters in a hierarchical fashion. Tags can be applied to meters, virtual meters or meter groups.

[See the concept section on tags for more information](complex-implementations.md#tags)

{% hint style="info" %}
Also see [Tags vs Meter Groups](../readme/concepts/tags-vs-meter-groups.md) for discussions on how these can be used and where each one should be used.
{% endhint %}



## Implementation Objectives

Now that you understand how meter hierarchies work the next step is identifying what the objectives are for setting utility consumption monitoring.



Some questions that need to be asked:

1. Do you need to monitor consumption for the entire building only? Or for each individual  sub-location as well?
   1. Does each sub-location that needs to be monitored have its own physical meter?
   2. What if some areas don't have meters? Can the consumption be calculated from the consumption readings of other meters?
2.  Do you need to monitor consumption based on different categories (equipment type, or water usage etc...) apart from location?

    1. For these categories do you need to compare consumption across different categories or sub-categories?





