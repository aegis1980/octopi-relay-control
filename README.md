# OctoPi plugin to control relays via RPi GPIO/SPI

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


