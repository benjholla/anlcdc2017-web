##import RPi.GPIO as GPIO

from flask import Flask, render_template, Response, redirect, url_for, request, session, abort
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

## app config
app = Flask(__name__)
app.secret_key = 'FF8AAF4701FECF49B92DB6985CA2F67BF34E7B41'

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# silly user model
class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.name = "user" + str(id)
        self.password = self.name + "_secret"
    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)

# create some users with ids 1 to 20       
users = [User(id) for id in range(1, 21)]

    
# callback to reload the user object        
@login_manager.user_loader
def load_user(userid):
    return User(userid)

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

# error handlers
@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')

@app.errorhandler(404)
def page_not_found(e):
    return Response('<p>Page not found</p>')

@app.errorhandler(500)
def page_not_found(e):
    return Response('<p>Server error</p>')

# HMI Dash/Home page
@app.route('/')
def hmi():
    return render_template('home.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']        
        if password == username + "_secret":
            id = username.split('user')[1]
            user = User(id)
            login_user(user)
            return redirect(request.args.get("next"))
        else:
            return abort(401)
    else:
        return Response('''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
        ''')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')

# Water service HMI
@app.route('/water')
@login_required
def water():
    global wON
    return render_template('PangeaWater.html', wON=wON)

@app.route('/water/on')
@login_required
def WaterOn():
    global wON
    message = water_on()
    return render_template('PangeaWater.html', wON=wON, message=message)

@app.route('/water/off')
@login_required
def WaterOff():
    global wON
    message = water_off()
    return render_template('PangeaWater.html', wON=wON, message=message)

# Power service HMI
@app.route('/power')
@login_required
def power():
    global pON
    return render_template('PangeaPnE.html', pON=pON)

@app.route('/power/on')
@login_required
def poweron():
    global pON
    message = power_on()
    return render_template('PangeaPnE.html', pON=pON, message=message)

@app.route('/power/off')
@login_required
def poweroff():
    global pON
    message = power_off()
    return render_template('PangeaPnE.html', pON=pON, message=message)

# Kill Switch HMI
@app.route('/killswitch')
@login_required
def killswitch():
    return render_template('KillSwitch.html')

@app.route('/killswitch/on')
@login_required
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

@app.route('/status')
def status():
    global pON
    global wON
    return render_template('status.html', pON=pON, wON=wON)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
##    GPIO.cleanup()