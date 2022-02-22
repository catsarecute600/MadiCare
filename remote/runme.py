import max30102
import hrcalc
import paho.mqtt.client as mqtt

client = mqtt.Client("Maddie1")
client.username_pw_set(username="maddie", password="my_password")
print("Connecting...")
client.connect("192.168.86.XX")
client.publish("mytopic",'{"name":"x", "email":"y"}')
m = max30102.MAX30102()

# 100 samples are read and used for HR/SpO2 calculation in a single loop
while True:
    red, ir = m.read_sequential()
    result = hrcalc.calc_hr_and_spo2(ir, red)

    # hr, hr_valid, spo2, spo2_valid
    msg = f"\"hr\":{result[0]},"\
        f"\"hr_valid\":\"{result[1]}\","\
        f"\"spo2\":{result[2]},"\
        f"\"spo2_valid\":\"{result[3]}\""
        
    print(".")
    client.publish("madicare", "{" + msg + "}")
