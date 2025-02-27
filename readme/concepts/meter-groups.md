# Meter Groups

While virtual meters allow you to define a soft meter that has a calcualted value based on one or more physical meters, Meter Groups allow you define more complex groupings. A Meter group can consist of multiple physical meters, virtual meters and other meter groups as well. And each item added to the group can have an associated multiplier factor.

Like virtual meters, meter groups also keep track of consumption as a calculation of other meters. However unlike virtual meters, meter groups can also refer to other virtual meters and other meter groups.

Just like virtual meters, meter groups don't have units associated and consumption is calculated whenever the underlying physical meters receive consumption data.
