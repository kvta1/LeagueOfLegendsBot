# api_client.py
import requests

class APIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://euw1.api.riotgames.com"
        self.europe_url = "https://europe.api.riotgames.com"

    def fetch_matchid(self, puuid):
        url = f"{self.europe_url}/lol/match/v5/matches/by-puuid/{puuid}/ids"
        headers = {"X-Riot-Token": self.api_key}
        response = requests.get(url, headers=headers)
        
        # print(response.json())
        return response.json()
    
    def fetch_match_metadata(self, matchId):
        url = f"{self.europe_url}/lol/match/v5/matches/{matchId}"
        headers = {"X-Riot-Token": self.api_key}
        response = requests.get(url, headers=headers)
        return response.json()
    
    def fetch_summoner_data(self, summoner_name):
        url = f"{self.base_url}/lol/summoner/v4/summoners/by-name/{summoner_name}"
        headers = {"X-Riot-Token": self.api_key}
        response = requests.get(url, headers=headers)
        
        # print(response.json())
        return response.json()
    


        
