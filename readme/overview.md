# Overview

The UMS application can manage multiple types of utilities as mentioned in the previous section.

Consumption data - including meter readings - can be fed into the system either via API or Mqtt. Other integrations are also available for ingesting data. Using Lucy, its possible to read consumption data from invoice PDFs and images and feed them into the application as well.

Once data is ingested, the application will calculate and store consumption data and other metrics, using interpolation where required.

You can then track consumption data across many dimensions including date ranges, tags, and base lines.
