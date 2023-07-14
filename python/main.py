## Copyright 2020 Google LLC
## 
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
## 
##     https://www.apache.org/licenses/LICENSE-2.0
## 
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
## 
## [START cloudrun_helloworld_service]
## [START run_helloworld_service]
## 
import subprocess
import sys

from flask import Flask, render_template
from flask_assets import Bundle, Environment

app = Flask(__name__)

# assets: https://flask-assets.readthedocs.io/en/latest/
assets = Environment(app)
assets.url = app.static_url_path

@app.route('/')
def index():
    return render_template('index.html', version=sys.version, release_info=find_distro())

def find_distro():
    release_info = subprocess.check_output("cat /etc/*release", shell=True).decode('utf-8')

    return release_info.strip()

if __name__ == "__main__":
    app.run(host="localhost", port=3000, debug=True)