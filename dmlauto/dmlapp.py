from flask import Flask, render_template
from energenie import switch_on, switch_off
from gpiozero import Energenie as eg
from typing import Any#, List, Dict, Iterable, Sequence, Optional, ClassVar


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/on/')
def on():
    eg.switch_on()
    return render_template('index.html')

@app.route('/off/')
def off() -> Any:
    eg.switch_off()
    #return "poo"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
