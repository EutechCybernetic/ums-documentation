# Complex Implementation Process

The complex implementation process is the same as the simple implementation process except for one major extra step: Mapping meters to locations

* Configure Meters. See [configuring-meters.md](../getting-started/configuring-the-application/configuring-meters.md "mention")
* Setup the integration for meters
* Optionally setup tags, virtual meters or meter groups. (See [configuring-virtual-meters.md](../getting-started/configuring-the-application/configuring-virtual-meters.md "mention"), [configuring-meter-groups.md](../getting-started/configuring-the-application/configuring-meter-groups.md "mention"), [configuring-tags.md](../getting-started/configuring-the-application/configuring-tags.md "mention"))
* Map Meters to locations
* Setup your dashboards



## Why do I need to map meters to locations

When you have meters and sub meters, the consumption for a location can be misleading as it would also include sub meters, the values of which would have already been factored into the parent meter.&#x20;

For example, if the parent meter is a distribution board and the sub meter is a utility meter within a floor, the distribution board would already include the consumption of the sub meter.

So if both are attached to the same location, it would double count some of the consumption.



The solution is to mark the distribution board as the main meter for the location.

For every location you wish to track consumption for and has sub meters, you can mark one of the meters as the main meter for that location.&#x20;

{% hint style="info" %}
The main meter would typically be the distribution board at that location.
{% endhint %}

You can also map a virtual meter or a meter group.

So if there are more than one main meter in a location - you can create a virtual meter or meter group for it and then map that group or virtual meter as the main meter for the location.



See the [marking-the-main-meter.md](../getting-started/configuring-the-application/marking-the-main-meter.md "mention") section for more info on mapping a meter to a location.

