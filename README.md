# ugr-wifi-2017

Files related to the South Seattle College Undergraduate Research (UGR) Project, entitled "Wireless Sensor Networks for Internet of Things Applications."

This project took place during Winter and Spring 2017 at South Seattle College, under the supervision of myself (Dr. Charles Reid). 

## Project Description

This project was a low-cost undergraduate research project htat involved the use of Raspberry Pis to capture and analyze
large data sets about wifi signals. The students wrote Python code to capture wifi data onboard the Raspberry Pis using the 
aircrack-ng suite. They then stored the data in a NoSQL database (MongoDB) on a virtual private server. Finally, the students
used Jupyter notebooks to interface with MongoDB from Python, write queries, analyze data, and visualize the results.

## Project Participants

The following students participated:
* Phuong Tran
* Shelby Mirziteh
* Jadon Combs
* Thy Lee
* Angela Flores

## Project Poster

This research was presented in a poster session at the 
[University of Washington Undergraduate Research Symposium](http://www.washington.edu/undergradresearch/symposium/).

You can also find more details about the project at the [charlesreid1 research and teaching blog](https://charlesreid1.github.io):
* [Part 1](http://charlesreid1.github.io/undergraduate-research-project-wireless-sensor-networks-for-internet-of-things-applications-part-1-the-project.html)
* [Part 2](http://charlesreid1.github.io/undergraduate-research-project-wireless-sensor-networks-for-internet-of-things-applications-part-2-the-technologies.html)

## Repository Contents

### `notebooks/`

The notebooks directory contains the Jupyter notebooks used to generate plots for the 2017 UW Research Sympoisum poster.

### `poster/`

The poster directory contains an image and a PDF copy of the final poster presented at the 2017 UW Research Symposium.

### `wifi/`

Python and shell scripts used to capture wifi data from the Raspberry Pis.

### Other code

Some of the code on the backend was taken care of by me, Dr. Reid, for the students' benefit 
(so they didn't have to get elbow deep in the nuances of virtualization, encrypted tunnels, 
 SSL wrapping, and bypassing firewalls.)

Several of these repositories are for setting up Docker containers on the virtual private server
(we ran MongoDB, Stunnel, and Jupyter notebook out of Docker containers). The rest are scripts 
run on the Raspberry Pi.

Each of the following git repos is on [git.charlesreid1.com](https://git.charlesreid1.com/explore):

**Docker:**

[docker/d-stunnel](https://charlesreid1.com:3000/docker/d-stunnel) - repository with files for running an stunnel server in a docker container

[docker/d-rsync](https://charlesreid1.com:3000/docker/d-rsync) - repository with files for running an rsync server in a docker container

[docker/d-jupyter](https://charlesreid1.com:3000/docker/d-jupyter) - repository with files for running a Jupyter notebook server in a docker container 

[docker/d-mongodb](https://charlesreid1.com:3000/docker/d-mongodb) - repository with files for running a MongoDB database in a docker container

[docker/d-mongoexpress](https://charlesreid1.com:3000/docker/d-mongoexpress) - like phpMyAdmin, MongoExpress is a web-based client for interacting with MongoDB; this was also run in a docker container 

**Raspberry Pi:**

[rpi/process-wifi-data](https://charlesreid1.com:3000/rpi/pi-process-wifi-data) - code for processing wifi data

[rpi/stunnel](https://charlesreid1.com:3000/rpi/pi-stunnel) - code for running an stunnel client on the rasbperry pi

[rpi/aircrack-batch](https://charlesreid1.com:3000/rpi/pi-aircrack-batch) - code for running aircrack in batch mode to dump wifi data to CSV files at intervals

[rpi/pi-startup-services](https://charlesreid1.com:3000/rpi/pi-startup-services) - startup scripts for the Raspberry Pi, allowing it to start airodump-ng and listen for nearby wifi signals on boot

[rpi/pi-setup](https://charlesreid1.com:3000/rpi/pi-setup) - setup scripts for the Rasbperry Pis, to keep everything uniform across each Pi

[rpi/transmission](https://charlesreid1.com:3000/rpi/pi-transmission) - code for connecting to a remote server using stunnel, and transferring data via rsync tunneled through stunnel
