# main.py
from api_client import APIClient
from data_handler import *
import openpyxl
import os

# Riot Games API Key
api_key = "RGAPI-25e3b0ba-41d9-48fd-80fe-0ef91b2e2e46"

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
    matchids_df, match_data_df, metadata_df = process_match_data(summoners_df, api_client)
    
    winloss_df = get_match_info(summoners_df, metadata_df)
    
    print(winloss_df)
if __name__ == "__main__":
    main()
    