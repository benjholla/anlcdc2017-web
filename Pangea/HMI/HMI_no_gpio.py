##import RPi.GPIO as GPIO

import flask
from flask import Flask, Response, render_template, redirect, url_for, escape, request, session, abort
from flask_login import LoginManager
#from models import User
import ldap_auth
from sets import Set
import os
from datetime import timedelta
import time
import hashlib
import datetime

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

# set sessions to timeout after 30 seconds
@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(seconds=30)

# renew user session timeout after each request
@app.before_request
def renew_session():
  session.modified = True

# LDAP roles
WATER_TECH_ROLE = "water_tech"
POWER_TECH_ROLE = "power_tech"

# Initiate GPIO
##GPIO.setmode(GPIO.BCM)

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
##for pin in WaterPins:
##    GPIO.setup(pin, GPIO.OUT)
##    GPIO.output(pin, GPIO.LOW)

# Start Power service
##for pin in PowerPins:
##    GPIO.setup(pin, GPIO.OUT)
##    GPIO.output(pin, GPIO.LOW)

# Function to turn Water service On and OFF
def water_on():
    global wON
    if not wON:
##        GPIO.output(WaterPins, GPIO.HIGH)
        wON = True
        message = "Service: Water has been turned ON"
        print(message)
        return message
    return

def water_off():
    global wON
    if wON:
##        GPIO.output(WaterPins, GPIO.LOW)
        wON = False
        message = "Service: Water has been turned OFF"
        print(message)
        return message
    return None

# Function to turn Power service ON and OFF
def power_on():
    global pON
    if not pON:
##        GPIO.output(PowerPins, GPIO.HIGH)
        pON = True
        message = "Service: Power has been turned ON"
        print(message)
        return message
    return None

def power_off():
    global pON
    if pON:
##        GPIO.output(PowerPins, GPIO.LOW)
        pON = False
        message = "Service: Power has been turned OFF"
        print(message)
        return message
    return None

# Function to turn on Kill Switch to all services
def KillSwitch():
    global ksON
    if ksON:
        global wON
        global pON
        message = {}
        if wON or pON:
##            GPIO.output(WaterPins, GPIO.LOW)
##            GPIO.output(PowerPins, GPIO.LOW)
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

# error handlers
@app.errorhandler(401)
def page_not_found(e):
    return render_template('401.html', session=session), 401

@app.errorhandler(401)
def page_not_found(e):
    return render_template('403.html', session=session), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', session=session), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html', session=session), 500

@app.route('/')
def status():
    global pON
    global wON
    return render_template('status.html', session=session, pON=pON, wON=wON)

@app.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        otp = request.form['otp'] # not really a otp exactly, but whatever

        # compute a time based password
        #t = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M")
        t = datetime.datetime.utcnow().strftime("%Y-%m-%d %H")

        md5 = hashlib.md5()
        md5.update(t)
        digest = str(md5.hexdigest())
        seed = 1526
        for c in digest:
            seed = seed + ord(c);
        secret = str(seed)[0:4]

        authorized = ldap_auth.authenticate(username, password) and (otp == secret)
        if authorized:
            print "Logged in as: " + escape(username)
            session['logged_in'] = True
            session['username'] = escape(username)
            session['is_watertech'] = ldap_auth.hasMembershipWithSession(username, authorized, WATER_TECH_ROLE)
            session['is_powertech'] = ldap_auth.hasMembershipWithSession(username, authorized, POWER_TECH_ROLE)
            return redirect(url_for('home'))
        else:
            return render_template('login-error.html', session=session)
    else:
        return render_template('login.html', session=session)

@app.route("/logout/")
def logout():
    if session:
        session['logged_in'] = False
        session['username'] = None
        session['is_watertech'] = False
        session['is_powertech'] = False
    return render_template('logout.html', session=session)

# HMI Dash/Home page
@app.route('/home')
def home():
    if not session.get('logged_in'):
        return render_template('401.html', session=session), 401
    else:
        return render_template('home.html', session=session)

# Water service HMI
@app.route('/water')
def water():
    global wON
    if not session.get('logged_in'):
        return render_template('401.html', session=session), 401
    else:
        if not session.get('is_watertech'):
            return render_template('403.html', session=session), 403
        else:
            return render_template('PangeaWater.html', session=session, wON=wON)

@app.route('/water/on')
def WaterOn():
    global wON
    if not session.get('logged_in'):
        return render_template('401.html', session=session), 401
    else:
        if not session.get('is_watertech'):
            return render_template('403.html', session=session), 403
        else:
            message = water_on()
            return render_template('PangeaWater.html', session=session, wON=wON, message=message)

@app.route('/water/off')
def WaterOff():
    global wON
    if not session.get('logged_in'):
        return render_template('401.html', session=session), 401
    else:
        if not session.get('is_watertech'):
            return render_template('403.html', session=session), 403
        else:
            message = water_off()
            return render_template('PangeaWater.html', session=session, wON=wON, message=message)

# Power service HMI
@app.route('/power')
def power():
    global pON
    if not session.get('logged_in'):
        return render_template('401.html', session=session), 401
    else:
        if not session.get('is_powertech'):
            return render_template('403.html', session=session), 403
        else:
            return render_template('PangeaPnE.html', session=session, pON=pON)

@app.route('/power/on')
def poweron():
    global pON
    if not session.get('logged_in'):
        return render_template('401.html', session=session), 401
    else:
        if not session.get('is_powertech'):
            return render_template('403.html', session=session), 403
        else:
            message = power_on()
            return render_template('PangeaPnE.html', session=session, pON=pON, message=message)

@app.route('/power/off')
def poweroff():
    global pON
    if not session.get('logged_in'):
        return render_template('401.html', session=session), 401
    else:
        if not session.get('is_powertech'):
            return render_template('403.html', session=session), 403
        else:
            message = power_off()
            return render_template('PangeaPnE.html', session=session, pON=pON, message=message)

# Kill Switch HMI
@app.route('/killswitch')
def killswitch():
    if not session.get('logged_in'):
        return render_template('401.html', session=session), 401
    else:
        if not session.get('is_watertech'):
            return render_template('403.html', session=session), 403
        if not session.get('is_powertech'):
            return render_template('403.html', session=session), 403
        else:
            return render_template('KillSwitch.html', session=session)

@app.route('/killswitch/on')
def killswitchon():
    global ksON
    if not session.get('logged_in'):
        return render_template('401.html', session=session), 401
    else:
        if not session.get('is_watertech'):
            return render_template('403.html', session=session), 403
        if not session.get('is_powertech'):
            return render_template('403.html', session=session), 403
        else:
            ksON = True
            message = KillSwitch()
            return render_template('KillSwitch.html', session=session, message=message)

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(port=8080,debug=False)