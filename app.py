from flask import Flask, jsonify
from gpiozero import LED

app = Flask(__name__)

led = LED(18)


@app.route('/1')
def onLed():
    led.on()    
    return jsonify(ledState=1)

@app.route('/0')
def offLed():
    led.off()    
    return jsonify(ledState=0)
