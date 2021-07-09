from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseServerError
from django.views.decorators import gzip

import cv2
import os
import time
import Adafruit_DHT
from time import sleep
from gpiozero import LED, DistanceSensor, AngularServo

# Define PIN
led = LED(21)
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 12
servoT = AngularServo(24, min_angle=-90, max_angle=90)
servoP = AngularServo(25, min_angle=-90, max_angle=90)

sensorF = DistanceSensor(20, 16)
sensorB = DistanceSensor(26, 19)

def index(request):
    try:
        return render(request,"home.html")
    except Exception as e:
            return HttpResponseServerError(str(e))

def get_frame():
    camera =cv2.VideoCapture(0) 
    while True:
        _, img = camera.read()
        imgencode=cv2.imencode('.jpg',img)[1]
        picamData=imgencode.tostring()
        yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n'+picamData+b'\r\n')
    del(camera)
    
@gzip.gzip_page
def picam_stream(request,stream_path="video"):
    try :
        return StreamingHttpResponse(get_frame(),content_type="multipart/x-mixed-replace;boundary=frame")
    except :
        return "Error"

def ledOn(request):
    if request.method == 'POST':
        led.on()
        con = "LED ON"
    return HttpResponse(con)

def ledOff(request):
    if request.method == 'POST':
        led.off()
        con = "LED OFF"
    return HttpResponse(con)

def dth(request):
    if(int(round(sensorF.distance * 100))<5 or int(round(sensorB.distance * 100))<5):
        led.on()
    else:
        led.off()
    dth_dict = "Failure"+","+"Check"
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        dth_dict = str(temperature)+","+str(humidity)
    time.sleep(1)
    return HttpResponse(dth_dict)

def panLL(request):
    if request.method == 'POST':
        servoP.angle = -90
        con = 'Camera moveing max left'
    return HttpResponse(con)

def panL(request):
    if request.method == 'POST':
        servoP.angle = -45
        con = 'Camera moveing left'
    return HttpResponse(con)

def panM(request):
    if request.method == 'POST':
        servoP.angle = 0
        con = 'Camera is center'
    return HttpResponse(con)

def panR(request):
    if request.method == 'POST':
        servoP.angle = 45
        con = 'Camera moveing right'
    return HttpResponse(con)

def panRR(request):
    if request.method == 'POST':
        servoP.angle = 90
        con = 'Camera moveing max right'
    return HttpResponse(con)

def tiltDD(request):
    if request.method == 'POST':
        servoT.angle = -90
        con = 'Camera moveing max down'
    return HttpResponse(con)

def tiltD(request):
    if request.method == 'POST':
        servoT.angle = -45
        con = 'Camera moveing Down'
    return HttpResponse(con)

def tiltM(request):
    if request.method == 'POST':
        servoT.angle = 0
        con = 'Camera is center'
    return HttpResponse(con)

def tiltU(request):
    if request.method == 'POST':
        servoT.angle = 45
        con = 'Camera moveing Up'
    return HttpResponse(con)

def tiltUU(request):
    if request.method == 'POST':
        servoT.angle = 90
        con = 'Camera moveing max Up'
    return HttpResponse(con)

def forward(request):
    if request.method == 'POST':
        os.system('python3 rc/forward.py')
        con = 'Going forwards'
    return HttpResponse(con)

def stop(request):
    if request.method == 'POST':
        os.system('python3 rc/stop.py')
        con = 'Stop'
    return HttpResponse(con)

def backward(request):
    if request.method == 'POST':
        os.system('python3 rc/backward.py')
        con = 'Going backwards'
    return HttpResponse(con)

def left(request):
    if request.method == 'POST':
        os.system('python3 rc/left.py')
        con = 'Going Left'
    return HttpResponse(con)

def right(request):
    if request.method == 'POST':
        os.system('python3 rc/right.py')
        con = 'Going Right'
    return HttpResponse(con)