#!/usr/bin/env python3
import os
from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def get_time():
    time_str = datetime.datetime.now().isoformat()
    # decoded_str = datetime.datetime.strptime(time_str,"%Y-%m-%dT%H:%M:%S.%f")
    return time_str

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8888))
    app.run(host='0.0.0.0', port=port)
