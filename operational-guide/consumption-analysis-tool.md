# Consumption Analysis Tool

The consumption analysis tool gives you an interface to analyze consumption of any object (meter, group or tag) in various ways.

{% hint style="info" %}
When we say 'object' we mean either a meter, virtual meter, meter group or tag
{% endhint %}



The tool can be addressed in a few ways:

1. Clicking on a meter inside the meter explorer
2. On the right side panel in the tag explorer where it shows consumption data for the selected tag(s)
3. It can be added to a dashboard as a widget and customized

The tool looks like this:

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

1. Details Panel - contains details about the specific object. This may or may not be visible depending on how you invoked the tool
2. The analysis panel
3. The date filter - you can pick a date range to analyze consumption&#x20;
4. High level KPIs - currently shows the largest peak consumption and (if applicable) the overall deviation from the baseline
   1. You can export the data being viewed at any time using the export button. It downloads a csv export of the data
5. The filter panel - click this to expand the tool to show all avaialble filters
6. [consumption-contribution-tool.md](consumption-contribution-tool.md "mention")- this is only applicable to virtual meters and meter groups.

## Date Ranges

When picking a date range, you can either pick a relative date range or a custom date range.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-29 at 20.58.08.png" alt="" width="369"><figcaption></figcaption></figure>

When you pick a relative date range, you can select to show data for either

1. Last 7 Days
2. Last 30 Days
3. Last 365 Days

The date range selected will be automatic based on what you selected.

You can also choose 'Custom' in which case you can specify a start date and an end date.

First click on the start date in the calendar, and then click the end date- the calendar should auto highlight all dates in between the start date and end date

{% hint style="info" %}
Comparing the current time period to the previous time period is only available if you choose a relative date range - so that the tool will know what dates for her also
{% endhint %}

## Extended Filters and Analysis

You can click on the 'filter' icon on the top right (#6 in the diagram above) to expand to the full view of the analysis interface.

<figure><img src="../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

This is similar to the earlier interface but more options are available.



1. The ability to change the visualization type. You can choose between
   1. Bar Chart (default view)
   2. Column Chart (bars layed out horizontally)
   3. Area Chart
   4. Line Chart
   5. Donut Chart (pie chart - not relevant for some types of analytics)
2. The filter panel on the right side giving you more filter options



## Filtering Options

The filter panel gives you a range of filtering and grouping and aggregation options for data.

Not all filters are always applicable.



### Utility Type

Choose which utility type you want to analyze.

&#x20;This option is only available when you configure the tool from a dashboard.&#x20;

When you access the tool from a meter or tag, the utility type is already known so that option is not available in those cases.



### Units

Based on the utility type - the list of possible units will be shown with the default base unit selected.

You can change the units that the data is presented in.



### Target Type

{% hint style="info" %}
This option is only available when you access the consumption anaylsis tool from a dashboard widget
{% endhint %}

Select what kind of object you want to analyze.

This can one of:

1. Utility Meters
2. Virtual Metres
3. Meter Groups
4. Tags

### Target

{% hint style="info" %}
This option is only available when you access the consumption anaylsis tool from a dashboard widget and after you select the 'Target Type'
{% endhint %}

Once you select your target type, based on the selection you have different options.

#### Utility Meters

If you selected 'Utility Meter' as the target type, you can now select which utility meter you want to analyze. You can select multiple utility meters as well.

#### Virtual Meters

If you selected 'Virtual Meter' as the target type, you can now select which virtual meter you want to analyze. You can select multiple virtual meters as well.

#### Meter Groups

If you selected 'Meter Group' as the target type, you can now select which group you want to analyze. You can select multiple groups to analyze as well.

#### Tags

If you selected 'Tag' as the target type, you can now choose a specific tag that you want to anaylze.

You will first be asked to choose the tag type, and then presented with a tag tree to pick your tag.

You can pick multiple tags and the data shown will be from the _intersection_ of all tags.

For example, if you pick \`Location:Building1\` and \`System:PlugLoad\`

The consumption will be shown for meters that have both those tags.

{% hint style="info" %}
Sub-tags will also be considered as each tag's consumption automatically includes the consumption from sub-tags as well.
{% endhint %}

Using the example above, the meters with the green tick mark will be selected using the combination of Location:Building1 and System:PlugLoad

<figure><img src="../.gitbook/assets/image (19).png" alt="" width="563"><figcaption></figcaption></figure>

### Comparing Multiple Items

You can compare multiple items (called 'targets').

To do so - first select a single target.

Once you select a target,  you will have the option to select additional targets to compare against.

<figure><img src="../.gitbook/assets/image (20).png" alt="" width="375"><figcaption></figcaption></figure>

When you use that option - you will be presented with a screen where you can add more targets.

Each target could either be a meter, virtual meter, group or tag.&#x20;

<figure><img src="../.gitbook/assets/Screenshot 2025-02-12 at 16.19.01.png" alt=""><figcaption></figcaption></figure>

On the left pane, the list of additional targets is shown.

When you click on a target, on the right pane, you can change the target by specifying a new target type and then choosing the actual target item.

You can add new targets by clicking the '+ Add Target' button on the top.



As soon as you add targets, the widget will be refreshed to show the updated targets as new bars or columns or wedges in the chart.

### Buckets

By default, data is selected based on the date range and other filters and accumulated into increments of 1 day.

This increment is called a _bucket_. There are other buckets available:

15min, 30min, 1hr, Day, Week,  Month and Year

**15min** buckets will show data in 15min intervals. Meaning for every hour, it would show 4 values:

3:00, 3:15, 3:30, 3:45 (assuming its the 3 o'clock time period)



**30min** buckets will similary show data in 30min intervals - 3:00 and 3:30



**Day** buckets will show one data point per day.&#x20;



**Week** buckets show one data point for every week. Note that week doesn't mean '7 days' but it literally means 'one week'.

If you are in the middle of the week (say, Tuesday) - it would show data from Sunday-Tuesday for that week.\
For previous weeks it would show data from Sunday to Saturday.



**Month** bucket groups the data into one data point for every month of the year.



**Year** buckets group data for an entire year.

{% hint style="info" %}
If you want to see the total accumulated consumption as a single number, choosing 'Year' is a good way to do that as it will sum up all data for the entire year
{% endhint %}



When data points are grouped, all the data is summed together and shown in that data point.



### Grouping Data

Apart from showing data based on actual dates (or hours or months etc...) you can also analyze data by 3 different groups:

1. Hour of Day
2. Day Of Week
3. Day Of Month

You can choose to see the average, sum, min or max across that time range.

To enable grouping, check off the 'Enable Grouping' checkbox in the filter panel.

{% hint style="info" %}
When grouping is enabled, the 'bucket' parameter is not considered as it is not relevant. Buckets are only relevant when using absolute date ranges
{% endhint %}





#### Hour of Day

When you analyze data by 'Hour Of Data', within the selected date range, all the data for a given hour (ex: 12 am, 1am, 2am 3am .... 4pm 6pm ... 11pm)  are accumulated together.&#x20;

This is useful to anaylze how consumption changes through out a day.

For example, all the consumption that occurred from 1am-2am every day are grouped under the '1am' slot.



#### Day Of Week

This option will group data by the day of the week that it falls on.

For example, all consumption that occurs on Mondays (12am-12am) get grouped together and aggregated under the bar for 'Monday' and so on.



#### Day Of Month

This will group data by the day of the month that the consumption falls under.

So you would get up to 31 bars (depending on the date range you choose)



### Tag Grouping

In addition to grouping by various date criteria, when you select 'Tag' as your target type you have the option to furthur group by sub tags.



## Examples With Grouping



### Scenario 1

I want to find out which hour of the day has the highest energy consumption for `Meter A`and consider the last 6 months of data for this.

Filters

| Filter       | Value         |
| ------------ | ------------- |
| Utility Type | energy        |
| Unit         | kwh           |
| Target Type  | Utility Meter |
| Target       | Meter A       |
| Grouping     | enabled       |
| Group        | Hour Of Day   |
| Aggregation  | Max           |
| Date Range   | 6 months      |



## Tag Grouping

In addition to grouping by different time intervals, if you are analyzing tags (ie, target type = 'Tags') there is an additional feature to group the results by sub-tags of the selected tag.

For example, if you have the following tag tree:

<figure><img src="../.gitbook/assets/Screenshot 2025-01-30 at 17.25.49.png" alt=""><figcaption></figcaption></figure>

and you then analyze by the top level 'area' tag like this:

<figure><img src="../.gitbook/assets/Screenshot 2025-01-30 at 17.25.21.png" alt=""><figcaption></figcaption></figure>

You can then add a tag group filter (at the bottom right in the filter panel) and choose to group by the 'area' tag.

The result is that each bar will now be further grouped by each of the sub-tags of the selected tag.

In this case, the top level tag we have chosen to filter by has  4 sub tags:  car park, data center, lettable and other.

So 4 groups will be defined.

<figure><img src="../.gitbook/assets/Screenshot 2025-01-30 at 17.25.31.png" alt=""><figcaption></figcaption></figure>
