---
description: Documentation on the consumption flow analysis tool
---

# Consumption Contribution Tool

The consumption contribution tool allows you to see how consumption for a virtual meter or meter group is constructed from the underlying meters.

You can access it by going ot the consumption analysis tool for a specific virtual meter or group and clicking the 'View Contributions' button at the bottom.

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

This will open up the contributions interface.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-30 at 17.30.19.png" alt=""><figcaption></figcaption></figure>

On the left side, the bar shows the virtual meter or group that is currently being inspected.

On the left side, the underlying meters that make up the virtual meter's consumption is shown.

The lines connecting the virtual meters to its underlying meters represents the flow of energy.

The thickness of the line is proportional to how much that metre contributed to the virtual meter's energy consumption for the selected date range.

Red lines represent negative consumption (ie, the formula subtracts that energy from the virtual metre).

Gree lines represent positive consumption.

{% hint style="info" %}
The date range in the consumption analysis interface is used to show the energy values in the contribution chart
{% endhint %}

You can hover over each bar to see the actual energy consumption value contributed by it.

If any of the bars on the left are themselves, virtual metres or groups, you can double click on it to expand it out to show its underlying meters as well.
