from datetime import datetime
import requests
import os
from dotenv import load_dotenv
from flask import Blueprint, render_template

routes = Blueprint("routes", __name__)

load_dotenv()
ACCESS_KEY = os.getenv("ACCESS_KEY")
URL = os.getenv("URL")
URL_EOD = os.getenv("URL_EOD")

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

@routes.route("/view/<symbol>")
def view(symbol):
    """This method create the route the View Stocks page of a company"""

    params = {
        "access_key": ACCESS_KEY,
        "symbols": symbol,
    }

    response = requests.get(url=URL_EOD, params=params)
    eod_data_api = response.json()["data"]

    return render_template("view.html", eod_data=eod_data_api)
