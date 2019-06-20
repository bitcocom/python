# Remote LED Control by Flask web service
# Jonathan Suh www.creapple.com

from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
LED = 12
GPIO.setup(LED, GPIO.OUT)

@app.route("/<command>")
def action(command):
    if command == "on":
        GPIO.output(LED, GPIO.HIGH)
        message = "GPIO" + str(LED) + " ON"
    elif command == "off":
        GPIO.output(LED, GPIO.LOW)
        message = "GPIO" + str(LED) + " OFF"
    else:
        message = "Unknown Command : " + command

    msg = {
        'message': message,
        'status': GPIO.input(LED)
    }

    return render_template('led.html', **msg)


if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=8000, debug=True)
    except KeyboardInterrupt:
        print("Terminate program by Keyboard Interrupt")
        GPIO.cleanup()
