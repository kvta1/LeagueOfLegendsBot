# data_handler.py
import pandas as pd
from summoner_class import Summoner
import numpy as np


def make_summoners(summoner_names, api_client):
    summoners_data = []

    for name in summoner_names:
        summoner_data = api_client.fetch_summoner_data(name)
        summoner_instance = Summoner(
            summoner_data['name'],
            summoner_data['id'],
            summoner_data['accountId'],
            summoner_data['puuid'],
            summoner_data['profileIconId'],
            summoner_data['revisionDate'],
            summoner_data['summonerLevel']
        )
        summoners_data.append(summoner_instance.__dict__)

    summoners_df = pd.DataFrame(summoners_data, index = summoner_names)
    return summoners_df

def process_match_data(summoners_df, api_client):
    # Implement your logic to process match data and extract wins and losses
    # wins = len([match for match in match_data["matches"] if match["win"]])
    # losses = len(match_data["matches"]) - wins
    # return wins, losses
    match_data = []
    match_ids = []
    match_metadata = []
    
    
    for puuid in summoners_df['puuid']:
        match_temp_data = []
        match_temp_ids = []
        match_temp_metadata = []
        
        matchids = api_client.fetch_matchid(puuid)
        
        for id in matchids:
            metadata = api_client.fetch_match_metadata(id)
            
            match_temp_metadata.append(metadata)
            match_temp_ids.append(id)
            
            match_temp_data.append(id)
            match_temp_data.append(metadata)

        match_data.append(match_temp_data)
        match_ids.append(match_temp_ids)
        match_metadata.append(match_temp_metadata)
    
    
    match_columns = [f'match_{i}_id' for i in range(len(match_metadata[1]))]
    metadata_columns = [f'match_{i}_metadata' for i in range(len(match_metadata[1]))]
    data_columns = [f'match_{i}_id' for i in range(len(match_metadata[1]))] + [f'match_{i}_metadata' for i in range(len(match_metadata[1]))]

    
    # Interleave the columns to stagger match IDs and metadata
    data_columns = [col for pair in zip(data_columns[:len(match_metadata[1])], data_columns[len(match_metadata[1]):]) for col in pair]
    
    matchids_df = pd.DataFrame(match_ids, index = summoners_df['name'], columns = match_columns)
    match_data_df = pd.DataFrame(match_data, index = summoners_df['name'], columns=data_columns)
    metadata_df = pd.DataFrame(match_metadata, index = summoners_df['name'], columns = metadata_columns)
    
    return matchids_df, match_data_df, metadata_df

def get_match_info(summoners_df, metadata_df):
    
    wins = 0
    losses = 0
    
    # Loops over every player in summoners_df and checks game statistics in metadata
    for name in summoners_df['name']:
        puuid = summoners_df.loc[name]['puuid']
        
        for match_idx in range(len(metadata_df.loc[name])):

            match = metadata_df.loc[name].iloc[match_idx]
            
            # Find index of player that we are looking for
            part_idx = match['metadata']['participants'].index(puuid)
            
            # Check if player won
            win = match['info']['participants'][part_idx]['win']

            if win:
                wins += 1
            else:
                losses += 1

    print(f'Amount of total wins: {wins}')
    print(f'Amount of total losses: {losses}')
