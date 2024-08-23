from flask import Flask, render_template
from data_handler.api_client import APIClient
from data_handler.data_handler import *
from dotenv import load_dotenv
import os

# Load the environment variables
load_dotenv()
api_key = os.getenv("API_KEY")

app = Flask(__name__)

api_client = APIClient(api_key)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/matchdata", methods=["POST"])
def matchdata():
    summoner_names = ["RiotSchmick", "RiotAether", "RiotBlaustoise"]
    summoners_df = make_summoners(summoner_names, api_client)
    wins, losses = process_match_data(summoners_df, api_client)
    return render_template("matchdata.html", wins=wins, losses=losses)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)