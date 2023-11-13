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


# print(summoners_df)
# print(matches_df)
# print(match_metadata_df)

# Create columns for matchId and metadata
match_columns = []
metadata_columns = []
for i in range(matches_df.shape[1]):
    match_columns.append(f'match_{i}_id')
    metadata_columns.append(f'match_{i}_metadata')
    

print(matches_df.iloc[1])

# Create a new DataFrame to store the combined data
combined_df = pd.DataFrame()

# Iterate over rows
# for i in range(len(matches_df)):
#     # Create a new row for each match and metadata
#     row_data = {}
#     for j in range(matches_df.shape[1]):
#         match_id_col = f'match_{j}_id'
#         metadata_col = f'match_{j}_metadata'
        
#         # Get match id and metadata for the current iteration
#         match_id = matches_df.iloc[i, j]
#         metadata = match_metadata_df.iloc[i, j]
        
#         # Add match id and metadata to the row data
#         row_data[match_id_col] = match_id
#         row_data[metadata_col] = metadata
    
#     # Append the row data to the combined DataFrame
#     combined_df = pd.concat([combined_df, pd.DataFrame([row_data])], ignore_index=True)

# Print the combined DataFrame
# print(combined_df)


dummydata = [['EUW1_6674904701', 'EUW1_6674850691', 'EUW1_6674487869', 'EUW1_6674411486', 'EUW1_6674106167', 'EUW1_6674076417', 'EUW1_6673018592', 'EUW1_6672509981', 'EUW1_6672472548', 'EUW1_6672438811', 'EUW1_6672401362', 'EUW1_6672359878', 'EUW1_6672316852', 'EUW1_6672060274', 'EUW1_6671795900', 'EUW1_6671767496', 'EUW1_6671704719', 'EUW1_6671625333', 'EUW1_6671612651', 'EUW1_6670970453'], ['EUW1_6674727741', 'EUW1_6674698665', 'EUW1_6674613147', 'EUW1_6672932300', 'EUW1_6672509981', 'EUW1_6672472548', 'EUW1_6672438811', 'EUW1_6672401362', 'EUW1_6672359878', 'EUW1_6672316852', 'EUW1_6672280058', 'EUW1_6672122023', 'EUW1_6672060274', 'EUW1_6671795900', 'EUW1_6671767496', 'EUW1_6671716788', 'EUW1_6670425441', 'EUW1_6670034057', 'EUW1_6670022378', 'EUW1_6670020592']]

dummycolumns = ['match_0_id', 'match_1_id', 'match_2_id', 'match_3_id', 'match_4_id', 'match_5_id', 'match_6_id', 'match_7_id', 'match_8_id', 'match_9_id', 'match_10_id', 'match_11_id', 'match_12_id', 'match_13_id', 'match_14_id', 'match_15_id', 'match_16_id', 'match_17_id', 'match_18_id', 'match_19_id']

# summoners_df = 

print(len(dummydata[1]))
