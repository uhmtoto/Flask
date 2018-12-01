from App import app
from App.database import *
from flask import (
    render_template
)

@app.route('/')
def main():
    return render_template('index.html')
