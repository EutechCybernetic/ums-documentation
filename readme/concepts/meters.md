# Meters

Physical meters are entities that record consumption. As the name suggest, you would typically map these to real world physical meters that you have. Readings can then be recorded against the meters at regular intervals and those are the raw data points that drive all the analytics.

If your building has one 3 energy meters and 1 water meter, you would register 3 meters as energy meters and 1 meter as a water meter.

Each meter has a few properties that can be configured:

1. The utility type (is it an energy meter? or water meter? or something else?)
2. A name - can be anything descriptive
3. Units - what units this meter uses for recording and showing readings.
4. A location - what location this meter is tied to. Meters can be tied to individual units, a floor or an entire building. You would typically pick the location that is _served_ by this particular meter.
5. Tags - you can tag meters with arbitrary tags that you pre-define. See the section on Tagging for more information on why you would want to do that
6. Baseline configuration - configure daily baseline values for each meter - see the baseline section for more information.

You can record readings for meters in several ways including manually entering the reading, uploading a csv file, uploading a bill or integration with IoT and BMS systems.
