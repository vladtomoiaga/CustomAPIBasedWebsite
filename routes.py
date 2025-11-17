import pandas as pd
import plotly.express as px
import plotly.io as pio
from datetime import datetime
import requests
import os
from dotenv import load_dotenv
from flask import Blueprint, render_template, request

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

    response = requests.get(url=URL, params=params, verify=False)
    data_api = response.json()["data"]

    return render_template("index.html", data=data_api)

def get_eod_data(symbol):
    """Returns end-of-day (EOD) data for a given stock symbol."""
    params = {
        "access_key": ACCESS_KEY,
        "symbols": symbol,
    }
    response = requests.get(url=URL_EOD, params=params, verify=False)
    return response.json()["data"]

@routes.route("/view/<symbol>")
def view(symbol):
    """This method create the route the View Stocks page of a company"""
    eod_data_api = get_eod_data(symbol)

    return render_template("view.html", eod_data=eod_data_api)

@routes.route("/plot")
def plot():
    """Plot the evolution of the stocks"""
    symbol = request.args.get("symbol")
    if not symbol:
        return "No symbol provided", 400

    data = get_eod_data(symbol)
    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"]).dt.date

    fig = px.line(df, x="date", y=["open", "low", "high", "close"])
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Value"
    )
    graph_html = pio.to_html(fig, full_html=False)

    return render_template("plot.html", graph_html=graph_html, symbol=symbol)