# Understanding data collection types

In order to integrate with meters, you need to understand data collection types.

Different kinds of meters record consumption data in different ways.

For example:

1. Cummulative Consumption
2. Power Load



In order to capture and record data accurately, the integration must know how to intrepret the data it receives.

Currently UMS supports 3 data collection types:

1. Cummulative Consumption
2. Rolling Average Consumption
3. Instantaneous Power Demand



## Cummulative Consumption

This is the standard way most meters record data.

A running number that only increases and tracks the total consumption since the meter was commissioned.

The consumption for a time period is the difference in the value of the meter at the start and end of that time period.

These meter values should never decrease but they may reset to 0 and start again.



## Rolling Average Consumption

These meters record consumption as an average over the last X minutes.

X could be 15 or 30 or an hour or something else.

The value at any given time is the average consumption value over the last time period.

This value will keep getting updated at any given time.



## Instantaneous Power Demand

This records the demand at any given time.

UMS will sample this data at regular intervals and use trapezium rule to calculate consumption at 15min increments.



## Collection Type Reference

When configuring data collection types for integrations, use these names:

| Collection Type ID            | Description                                                                                                                                                                                                                             |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `consumption`                 | Cummulative consumption                                                                                                                                                                                                                 |
| `powerload`                   | Instanteneous power load at any given time                                                                                                                                                                                              |
| `consumption/fromaverage/{x}` | <p>Rolling average of consumption over last <code>x</code> minutes. <code>{x}</code> should be replaced with a number in minutes.<br>For example, rolling averge over 15min window would be <code>consumption/fromaverage/15</code></p> |
