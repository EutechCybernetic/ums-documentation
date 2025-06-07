# Integration with IBMS

A common use case is to setup the connectivity to electric or other meters via the iviva IBMS application and then use that as a source of data for UMS.

UMS can automatically sync meters and their data from IBMS.



## Understanding how integration with IBMS works.

IBMS  models building data using equipment and points.

And IBMS typically deals with more than just utility meters. Many other types of devices and equipment are monitored through the IBMS app.

In order to sync data from IBMS, UMS needs to know which equipment and points to sync.

Rather than manually specifying all meter equipment and points, you just need to specify the equipment template name and point name to use and UMS will automatically pull in all meters that match that criteria.

In order for this to work - you should structure the IBMS configuration and data model so that you have a predefined set of equipment templates that represent your meters and a predefined list of point names that represent the consumption data point.



## Enabling the IBMS integration

Go to the 'Configuration' section in UMS.

Click on the 'Integrations' tab. Here you can see a list integrations that have been configured.

This list is probably empty.

Click on 'Add Item' at the top.

You will be given a few options to choose from.&#x20;

Choose the option to add an integration.

Choose 'Integartion to iviva IBMS app'

<figure><img src="../.gitbook/assets/Screenshot 2025-06-07 at 05.41.45.png" alt=""><figcaption><p>In the screenshot it shows that the integration is already installed. That will show only if you have already enabled the integration.</p></figcaption></figure>

Once you select the option - the integration will be added to the list of enabled integrations. You may have to reload the page to see it.

<figure><img src="../.gitbook/assets/Screenshot 2025-06-07 at 05.43.34.png" alt=""><figcaption></figcaption></figure>

Once the integration is registered, you can see that it has imported a Lucy model called UMSIBMSIntegration. This Lucy model is used to facilitate the integration of meter data and meter configuration.

The next step is configuring that Lucy model.



## Configuring the IBMS Integration

You can see that the Lucy model used to orchestrate the integration with IBMS is called 'UMSIBMSIntegration'

{% hint style="info" %}
Technically, you can click 'edit' next to the integration and change the model to a different one. However, for the out of the box IBMS integration we don't recommend doing that. Create a new integration instead.
{% endhint %}

Go to the Lucy interface and search for UMSIBMSIntegration. Once you locate and select the model, click on the 'Data Collections' tab to configure it.

![](<../.gitbook/assets/Screenshot 2025-06-07 at 07.52.49.png>)



In the iviva IBMS app, you would setup your meters as equipment and define points that map to the consumption values of those meters.

To allow UMS to pull the right data from IBMS, you need to specify how you have mapped the meters in the IBMS App.

Specifically, you need this information:

1. What equipment template name represents each meter type?
2. What point name within that equipment template represents the consumption value?

You need this information for every meter type you configure.

For example, for electricity meters, the equipment template used in IBMS may be called 'Energy Meter'.

For water meters, the equipment template used in IBMS may be called 'Water Meter'

Within the 'Energy Meter' equipment template, you may have a list of points configured. One of them would be the point that represents the consumption. It may be called 'Consumption Value' or 'Value' etc...

Once you have collected the equipment templates that represent meters and point names that represent values, you need to configure them in the Lucy model.

In the data collections tab, click on 'mappings' and enter the configuration mapping in the table.

It should look like what you see below:

<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

You need to enter the following details:

|                       |                                                                                                                                                                                                                                  |                                    |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| Field                 | Description                                                                                                                                                                                                                      | Example                            |
| EquipmentTemplateName | The name of the equipment template that represent the particular meter type                                                                                                                                                      | 'Energy Meter'                     |
| PointTemplateName     | The point within that equipment template that represents the meter consumption value                                                                                                                                             | 'Value' or 'Consumption'           |
| DataCollectionType    | What kind of reading is being recorded by the point mentioned above. See the [understanding-data-collection-types.md](understanding-data-collection-types.md "mention") section for more information.                            | <p>consumption or<br>powerload</p> |
| MeterType             | <p>The name of the meter type in UMS that this equipment and point represent. </p><p>See <a data-mention href="../getting-started/configuring-the-application/configuring-utility-types.md">configuring-utility-types.md</a></p> | 'electricity' or 'gas'             |

{% hint style="info" %}
You need at least one item for each meter type you want to integrate but you could also have multiple items for a single meter type. For example, if you have different kinds of energy meters that record data in different ways, you may have different equipment templates for them. But they are still part of electricity meter type. So you would have 2 entries with the same meter type configured.
{% endhint %}



That's it - once you have setup your equipment template names and point names and collection types for each meter type - the configuration is done.



## Syncing meter configuration from IBMS

Go back to the integration section in UMS.

Next to the IBMS Integration item there will be a 'Sync' button.

This button syncs the master meter data configuration from IBMS to UMS.

Use this to add all meters from IBMS into UMS automatically.

When you click it, it will open a dialog showing all meters it found in IBMS that are currently not present in UMS. You can manually select meters to sync or 'select all' and begin the sync process.

Keep the UI open while syncing is going on and until it completes.

Once the sync is done, the new meters will appear in the 'Meters' tab.

You can see that each meter that got synced stores some extra metadata. This metadata is important and identifies which integration the meter came from and keeps track of details like the unique id of the meter in the source system to make sync easier. Do not edit this information manually.

### Why doesn't the meter sync automatically happen?

You may wonder why the integration doesn't automatically sync new meters periodically.

This is because it's possible that the meter is not yet commissioned or fully configured in IBMS yet.

Its possible the meter has been setup in IBMS but not yet connected to live data or is pending verification. So we recommend always manually running the sync when new meters are available.

{% hint style="info" %}
It is possible to trigger a sync via an API call so you can automate it if required. Contact your account representative to learn about how this works
{% endhint %}



## Syncing meter data

Once your meter configuration is synced into the system, data sync happens automatically.

Every 15 minutes, the integration will run and invoke the Lucy model to capture data and send it to UMS for storage.
