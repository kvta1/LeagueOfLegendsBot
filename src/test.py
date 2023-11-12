import pandas as pd

# Sample data
data = {
    'name': ['Tampai', 'VinhQ'],
    'Match_0': [('EUW1_6673018592', {'metadata': {'dataVersion': '2', 'matchId': '6673018592'}}),
                ('EUW1_6672932300', {'metadata': {'dataVersion': '2', 'matchId': '6672932300'}})],
    'Match_1': [('EUW1_6672509981', {'metadata': {'dataVersion': '2', 'matchId': '6672509981'}}),
                ('EUW1_6672472548', {'metadata': {'dataVersion': '2', 'matchId': '6672472548'}})]
}

# Create the DataFrame
df = pd.DataFrame(data)

print(df)

# Rename columns for clarity
df.columns = [f'Match_{i}' for i in range(len(data))]

# Reset the index for the 'name' column
df.reset_index(inplace=True)

# Create separate columns for match_id and metadata
df[['Match_0_ID', 'Match_0_Metadata']] = pd.DataFrame(df['Match_0'].tolist(), index=df.index)
df[['Match_1_ID', 'Match_1_Metadata']] = pd.DataFrame(df['Match_1'].tolist(), index=df.index)

# Drop the original tuple columns
df.drop(columns=['Match_0', 'Match_1'], inplace=True)

# Set the 'name' column as the index again
df.set_index('name', inplace=True)

# Display the resulting DataFrame
print(df)