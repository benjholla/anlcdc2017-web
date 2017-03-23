#!/usr/bin/python3
import RPi.GPIO as GPIO
from flask import Flask, render_template

app = Flask(__name__)

# Initiate GPIO
GPIO.setmode(GPIO.BCM)

# Correlate GPIO pins to sevices
WaterPins = [17]
PowerPins = [27]

# Water ON
global wON
wON = True

# Power ON
global pON
pON = True

# Kill Switch OFF
ksON = False

# Start Water service
for pin in WaterPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Start Power service
for pin in PowerPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)


# HMI Dash/Home page
@app.route('/')
def hmi():
    return render_template('home.html')


# Water service HMI
@app.route('/water')
def water():
    global wON
    return render_template('PangeaWater.html', wON=wON)


# Function to turn Water service On and OFF
def water_on():
    global wON
    if not wON:
        GPIO.output(WaterPins, GPIO.HIGH)
        wON = True
        message = "Service: Water has been turned ON"
        print(message)
        return message
    return


def water_off():
    global wON
    if wON:
        GPIO.output(WaterPins, GPIO.LOW)
        wON = False
        message = "Service: Water has been turned OFF"
        print(message)
        return message
    return None


@app.route('/water/won')
def WaterOn():
    global wON
    message = water_on()
    return render_template('PangeaWater.html', wON=wON, message=message)


@app.route('/water/woff')
def WaterOff():
    global wON
    message = water_off()
    return render_template('PangeaWater.html', wON=wON, message=message)


# Power service HMI
@app.route('/power')
def power():
    global pON
    return render_template('PangeaPnE.html', pON=pON)


# Function to turn Power service ON and OFF
def power_on():
    global pON
    if not pON:
        GPIO.output(PowerPins, GPIO.HIGH)
        pON = True
        message = "Service: Power has been turned ON"
        print(message)
        return message
    return None


def power_off():
    global pON
    if pON:
        GPIO.output(PowerPins, GPIO.LOW)
        pON = False
        message = "Service: Power has been turned OFF"
        print(message)
        return message
    return None


@app.route('/power/pon')
def poweron():
    global pON
    message = power_on()
    return render_template('PangeaPnE.html', pON=pON, message=message)


@app.route('/power/poff')
def poweroff():
    global pON
    message = power_off()
    return render_template('PangeaPnE.html', pON=pON, message=message)


# Kill Switch HMI
@app.route('/killswitch')
def killswitch():
    return render_template('KillSwitch.html')


@app.route('/killswitch/on')
def killswitchon():
    global ksON
    ksON = True
    message = KillSwitch()
    return render_template('KillSwitch.html', message=message)


# Function to turn on Kill Switch to all services
def KillSwitch():
    global ksON
    if ksON:
        global wON
        global pON
        message = {}
        if wON or pON:
            GPIO.output(WaterPins, GPIO.LOW)
            GPIO.output(PowerPins, GPIO.LOW)
            wON = False
            pON = False
            message['status'] = 'Success'
            message['message'] = 'All services: Water and Power has been turned OFF'
        else:
            message['status'] = 'Danger'
            message['message'] = "All services are already turned off"

        print(message)
        ksON = False
        return message
    return None


@app.route('/status')
def status():
    global pON
    global wON
    return render_template('status.html', pON=pON, wON=wON)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')
    GPIO.cleanup()
