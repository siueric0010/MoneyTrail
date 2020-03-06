##############
## Script listens to serial port and writes contents into a file
##############
## requires pySerial to be installed 
import serial  # sudo pip install pyserial should work
import requests

REST_IP = "http://localhost:5001"
LOCATION_ROUTE = '/location'
serial_port = '/dev/ttyACM0'
baud_rate = 9600 #In arduino, Serial.begin(baud_rate)
write_to_file_path = "output.txt"
output_file = open(write_to_file_path, "w+")
ser = serial.Serial(serial_port, baud_rate)
while True:
    line = ser.readline()
    line = line.decode("utf-8") #sr.readline returns a binary, convert to string
    print(line)
    output_file.write(line)
    latitude = line.split("atitude= ")[1].split(" Longitude =")[0]
    longitude = line.split(" Longitude = ")[1]
    data = {'latitude': latitude, 'longitude': longitude}
    print(data)
    requests.post(REST_IP + LOCATION_ROUTE, data = data)
    sleep(1000)
    