# OctoPi plugin to control relays via RPi GPIO/SPI

**[WIP]** Currently only supports a [RELAYplate hat from Pi-Plates](https://pi-plates.com/relayr1/) which uses SPI (see point 2 below) 

Could add option for relays connected directly to RPi GPIOs, (if there is a demand!)

## To install

1. SSH into your octopi. 
2. Enable remote GPIO (I think?) and SPI. I think its in the interface section.
```
sudo raspi-config
```
3. Navigate to `plugins`:
```
cd ~/.octoprint/plugins
```
4. Clone this repo:
```
git clone https://github.com/aegis1980/octopi-relay-control
```
5. Activate octoprint python venv:
```
source ~/oprint/bin/activate 
```
6. Intall req'd Python packages
```
pip install rpi.gpio spidev
```
7. Restart octoprint.


