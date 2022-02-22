# Repository
https://github.com/catsarecute600/MadiCare

# Install libraries
pip install Flask 
pip install Flask-RESTful 
pip install Flask-SocketIO 
pip install Flask-MQTT
pip install eventlet

# Install MQTT Broker on ubuntu
sudo apt-get update 
sudo apt-get install mosquitto

## security
sudo mosquitto_passwd -c /etc/mosquitto/passwd maddie
Password: my_password

sudo vi /etc/mosquitto/conf.d/default.conf
> Add: 
> 
> allow_anonymous false 
> 
> password_file /etc/mosquitto/passwd 

sudo systemctl restart mosquitto

# Install MQTT client (Server and Raspberry PI)
sudo apt-get install mosquitto-clients

# Test MQTT connectivity
## subscription
mosquitto_sub -t "madicare" -u maddie -P my_password

## publish message
mosquitto_pub -t madicare -m '{"name" : "Steve Li", "email":"steve.wmli@gmail.com" }' -u maddie -P my_password

# Example
https://ithelp.ithome.com.tw/articles/10198250

# Run
cd py_ws/MaddieCare
source ./venv/bin/activate
cd server
python MaddieCareServer.py

# Remote Install
pip install RPi.GPIO
pip install smbus
pip install numpy

# Remote environment setup
ssh pi@raspberrypi.local
cd py_ws/MadiCareRemote
source ./venv/bin/activate
sudo pigpiod
python runme.py

# Sample
http://www.steves-internet-guide.com/into-mqtt-python-client/