# Meter Explorer

The meter explorer screen lets you see all your meters/virtual meters/meter groups in one place  and drill down into them for more information. You can easily find meters that are over the normal consumption and analyze them further.

You can view the consumption trend for meters across the last 24 hours or 30 days and filter down to see only those that have deviated from the target baselines that you have configured.



The meter explorer looks like this:

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

These are the components of it:

1. Switch between meters, virtual meters and meter groups
2. The consumption/baseline filter - toggle between showing last 24 hours consumption and last 30 days consumption. Also select a baseline and filter by that baseline
3. The list of the selected meter type. You can click on the name to drill down and view details about that specific meter
4. Number of meters to show in one page of results
5. Pagination: Go  to the next/previous set of results (if any)&#x20;
6. The consumption spark line - showing the relative trend in consumption for that meter. It would either show the last 24 hours of consumption or last 30 days of consumption depending on what was selected in the baseline filter



## Baseline Filter

The baseline filter panel looks like this:

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

In the panel, you can toggle between showing 24hrs and 30 days consumption.

You can also choose any pre-configured baseline. When a baseline is selected, the consumption trend will show bars in red where the consumption has gone over the baseline for that meter.

{% hint style="info" %}
You need to configure baselines for each meter as the target consumption level for each meter can be different. If no baseline is configured for that meter, then there is no highlighting of consumption values in red.
{% endhint %}

You can also select to filter the list to show only meters that have deviations from the baseline.

This lets you quickly dive into problematic items.

When you click on a meter you are taken to the [consumption-analysis-tool.md](consumption-analysis-tool.md "mention")
