import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, Insighta! \n This is an uppdate after deploying in Google Cloud with docker container :) </h1>'
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)