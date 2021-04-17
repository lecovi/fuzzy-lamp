import os
from dotenv import load_dotenv
from flask import Flask


load_dotenv()
__version__ = os.environ["VERSION"]
APP_NAME = os.environ["APP_NAME"]

app = Flask(__name__)
app.logger.debug(f"Running {APP_NAME} v{__version__}")


@app.route('/')
def hello_world():
    return f'Hello, World! from {APP_NAME} v{__version__}'
