# wifi

This directory contains scripts for capturing and processing wifi data.

## `collect-wifi-data`

Scripts for capturing wifi data in CSV file format. This basically starts and stops
`airodump-ng` (part of the aircrack suite) every M seconds, for N hours.
(In our case, every 15 seconds for 2 hours.)

## `process-wifi-data`

Scripts for processing the captured wifi data (in CSV file format).
This splits the CSV file into two halves: AP data, and client data.
It then populates the MongoDB with the AP and client data in two separate 
document collections.

