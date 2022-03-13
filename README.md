# Repository
https://github.com/catsarecute600/MadiCare

# Install libraries
pip install Flask  
pip install Flask-RESTful  
pip install Flask-SocketIO  
pip install Flask-MQTT 
pip install eventlet
pip install prometheus-client
pip install psycopg2

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
> password_file /etc/mosquitto/passwd  

sudo systemctl restart mosquitto
sudo systemctl status mosquitto
  
# Install MQTT client (Server and Raspberry PI)
sudo apt-get install mosquitto-clients
  
# Test MQTT connectivity
## subscription
mosquitto_sub -t "madicare" -u maddie -P my_password
  
## publish message
mosquitto_pub -t madicare -m '{"name" : "maddie", "email":"maddie@test.com" }' -u maddie -P my_password
  
## Example Flask MQTT integration
https://ithelp.ithome.com.tw/articles/10198250

# Run Server
cd py_ws/MaddieCare  
source ./venv/bin/activate  
cd server  
python MaddieCareServer.py  
  
# Remote Install (Raspberry PI)
pip install RPi.GPIO  
pip install smbus  
pip install numpy  
  
## Remote environment setup
ssh pi@raspberrypi.local  
cd py_ws/MadiCareRemote  
source ./venv/bin/activate  
sudo pigpiod  
python runme.py  
  
## Sample
http://www.steves-internet-guide.com/into-mqtt-python-client/

# Backend Database installation
sudo apt update  

## install Prometheus
https://linoxide.com/how-to-install-prometheus-on-ubuntu/  

$ sudo mkdir -p /etc/prometheus  
$ sudo mkdir -p /var/lib/prometheus  

wget https://github.com/prometheus/prometheus/releases/download/v2.33.5/prometheus-2.33.5.linux-amd64.tar.gz  

$ tar -xvf prometheus-2.33.5.linux-amd64.tar.gz  
$ cd prometheus-2.33.5.linux-amd64  

Follow steps on web site to setup prometheus

sudo systemctl start prometheus
sudo systemctl enable prometheus
sudo systemctl status prometheus

# Install Grafana
https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-grafana-on-ubuntu-20-04  

sudo systemctl start grafana-server  
sudo systemctl status grafana-server  
sudo systemctl enable grafana-server  
http://localhost:3000/

# Install prometheus client
pip install prometheus_client 

# Timescale DB installation
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-timescaledb-on-ubuntu-20-04  

sudo timescaledb-tune --quiet --yes
ready-made configuration file at /etc/postgresql/12/main/postgresql.conf

# create database
sudo -u postgres psql  

CREATE DATABASE timeseries;  
\c timeseries  

CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;  

CREATE TABLE health (
  time        TIMESTAMP WITH TIME ZONE NOT NULL,
  device_id   TEXT,
  heartbeat   NUMERIC,
  spo2        NUMERIC
);

SELECT create_hypertable('health', 'time');

INSERT INTO health(time, device_id, heartbeat, spo2)
  VALUES (NOW(), 'p1', 102, 99.5);
INSERT INTO health(time, device_id, heartbeat, spo2)
  VALUES (NOW(), 'p1', 101, 97.5);
INSERT INTO health(time, device_id, heartbeat, spo2)
  VALUES (NOW(), 'p1', 101, 99.5);
INSERT INTO health(time, device_id, heartbeat, spo2)
  VALUES (NOW(), 'p1', 102, 97.5);
INSERT INTO health(time, device_id, heartbeat, spo2)
  VALUES (NOW(), 'p1', 99, 96.5);
INSERT INTO health(time, device_id, heartbeat, spo2)
  VALUES (NOW(), 'p1', 98, 99.5);

