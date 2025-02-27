# Resetting Meters

For meters that record cummulative readings, meter resets will occur automatically.

If the latest reading is less than the previous one, there will be a temporary  gap in the energy values at the time of the reset.

Subsequently, when the next reading comes in - it will be calculated based on the previous reading that was sent.



Note that  readings of '0' (zero) are silently dropped and treated as communciation errors or integration errors. So if a reading is recorded at the moment of a reset, it will not be used until the next reading is sent.
