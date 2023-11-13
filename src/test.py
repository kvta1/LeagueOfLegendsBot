# test.py
import pandas as pd
import os
from data_handler import *
from api_client import APIClient

# Riot Games API Key
api_key = "RGAPI-72f1f11a-dd5c-495a-ad8d-aeec06bf14d6"

# Make the API client
api_client = APIClient(api_key)

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load summoners_df from the CSV file
summoners_df = pd.read_csv(os.path.join(f"{script_dir}/testing", "summoners_data.csv"))
matches_df = pd.read_csv(os.path.join(f"{script_dir}/testing", "matches_df.csv"))
match_metadata_df = pd.read_csv(os.path.join(f"{script_dir}/testing", "match_metadata_df.csv"))


data = match_metadata_df['1'][0]

print(type(data))
puuid = 'Lf0ghEcdrzd-zmXH3pt3bzhBejqrnGXFPgLRLpA0dKAD5mK1YyTld9kHqJ59mA_8bNjPk0C9QSEmeg'

win = data['info']['participants'][puuid]['win']

print(win)
