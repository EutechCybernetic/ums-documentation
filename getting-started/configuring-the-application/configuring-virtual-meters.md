# Configuring Virtual Meters

Virtual meter configuration is just like the physical meter configuration except there is an additional configuration for the formula for the virtual meter.



The formula is defined by selecting one or more physical meters and applying a scaling factor to each meter (the scaling factor can be negative or a fraction).

So if you wish to define a virtual meter as having the total from meter A and B and subtracting meter C, you would add the following meters and scaling factors:

| Meter | Scaling Factor |
| ----- | -------------- |
| A     | 1              |
| B     | 1              |
| C     | -1             |

This would result in the formula `Ax1 + Bx1  + Cx-1`being applied for that virtual meter
