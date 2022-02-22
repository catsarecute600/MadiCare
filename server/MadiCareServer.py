from flask import Flask, abort
from flask_mqtt import Mqtt
from flask import render_template
import json

app = Flask(__name__)

# app.config['MQTT_BROKER_URL'] = '0.0.0.0'
# app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_REFRESH_TIME'] = 1.0
app.config['MQTT_USERNAME'] = 'maddie'
app.config['MQTT_PASSWORD'] = 'my_password'
mqtt = Mqtt(app)

@app.route('/')
def index():
    return 'Index Hello World'

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('madicare')

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    payload = message.payload.decode()
    p = json.loads(payload)
    print("-------msg-------")
    print('hr         :', p['hr'])
    print('hr_valid   :', p['hr_valid'])
    print('spo2       :', p['spo2'])
    print('spo2_valid :', p['spo2_valid'])

@app.route('/api/v1.0/mqtt/refresh', methods=['GET'])
def refresh():
    mqtt.unsubscribe_all()
    mqtt.subscribe('madicare')
    return "OK"

if __name__ == '__main__':
    app.run(debug=True)