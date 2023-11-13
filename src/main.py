# main.py
from api_client import APIClient
from data_handler import *
import openpyxl
import os

# Riot Games API Key
api_key = "RGAPI-da7807b6-8502-4379-b972-31333bc3415d"

# Make the API client
api_client = APIClient(api_key)

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the Excel file
excel_file = os.path.join(script_dir, "..", "excel", "LeagueOfLegendsData.xlsx")
summoner_names = ["Tampai", "VinhQ"]

global summoners_df

def main():
    global summoners_df, match_metadata_df
    print('Getting summoner data: ')
    summoners_df = make_summoners(summoner_names, api_client)
    
    print('Getting match data:')
    matches_df, match_metadata_df = process_match_data(summoners_df, api_client)
    
    print('check')
    
    print(match_metadata_df)
if __name__ == "__main__":
    main()
    