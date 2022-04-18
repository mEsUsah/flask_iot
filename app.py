from flask import Flask, request
import gpiozero

app = Flask(__name__)

led = gpiozero.LED(18)


@app.route('/1')
def onLed():
    led.on()    
    return '<h1>On</h1>'

@app.route('/0')
def offLed():
    led.off()    
    return '<h1>Off</h1>'
