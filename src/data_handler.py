# data_handler.py
import pandas as pd
from summoner_class import Summoner


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
    match_metadata = []
    
    
    for puuid in summoners_df['puuid']:
        match_temp = []
        
        matchids = api_client.fetch_matchid(puuid)
        match_data.append(matchids)
        
        
        for id in matchids:
            metadata = api_client.fetch_match_metadata(id)
            match_temp.append((id, metadata))
            
        match_metadata.append(match_temp)
        
    
    matches_df = pd.DataFrame(match_data, index = summoners_df['name'])
    match_metadata_df = pd.DataFrame(match_metadata, index = summoners_df['name'])
    
    return matches_df, match_metadata_df
        
    
    

