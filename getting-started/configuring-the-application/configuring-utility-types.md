# Configuring Utility Types

You can configure multiple utility types within the application.

Under the Configuration section go to the 'Meter Types' tab to configure the various utility types.

{% hint style="info" %}
We use 'meter type' and 'utility type' interchangeably&#x20;
{% endhint %}

Here you can view existing utility types, edit them and add new types.

Click the 'Add Item' button on the top right to add a new utility type.

You can click the 'edit' button under a utility type to edit its properties.

You can also delete utility types by clicking the delete (trash) icon.

{% hint style="warning" %}
Deleting, like diamonds, is forever. Please don't delete utility types unless you accidentally created it just now.&#x20;
{% endhint %}



## Configuring utility types

Whether you add a new utility type or edit an existing one, the interface for doing so is similar.

You have the option to specify units that are supported for this utility type.

Configuring units is important. You need at least one unit for each utility type.



## Understanding Units

Each utility type can support multiple units in which consumption is recorded.

For electricity - this could be `mWh` or `kWh`

For chilled water, this could be `mWh`or  `btu`

For waste consumption it could be \`kg\`

For water it might be litres or gallons

Each utility type has one **base unit**

And then other units are defined in relationship to the base unit.

Each unit is defined with a _conversion factor_ that defines how it can be translated to the base unit.

The base unit always has a conversion factor of 1.

{% hint style="info" %}
How you define a base unit is basically by defining a new unit and giving the conversion factor as 1. That automatically makes it your base unit
{% endhint %}

{% hint style="info" %}
Can you have multiple base units by defining multiple units with a conversion factor of 1? Technically you can but it won't really serve any purpose.
{% endhint %}



The base unit is important - by default all data is converted into the base unit when recorded and the default unit for reporting will be the base unit.

