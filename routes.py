from datetime import datetime
import requests
import os
from dotenv import load_dotenv
from flask import Blueprint, render_template

routes = Blueprint("routes", __name__)

load_dotenv()
ACCESS_KEY = os.getenv("ACCESS_KEY")
URL = os.getenv("URL")

@routes.context_processor
def inject_current_year():
    """This method is setting the current year"""
    return {"current_year": datetime.now().year}

@routes.route("/")
def home():
    """This method create the route the Home page"""

    params = {
        "access_key": ACCESS_KEY
    }

    response = requests.get(url=URL, params=params)
    data_api = response.json()["data"]

    return render_template("index.html", data=data_api)
