import pandas as pd

# Read the IPL 2025 players data
df = pd.read_csv('data/ipl_2025_players.csv')

# Find the Orange Cap holder (most runs)
orange_cap = df.loc[df['runs'].idxmax()]
print(f"Orange Cap Holder: {orange_cap['player']} ({orange_cap['team']}) with {orange_cap['runs']} runs")

# Find the Purple Cap holder (most wickets)
purple_cap = df.loc[df['wickets'].idxmax()]
print(f"Purple Cap Holder: {purple_cap['player']} ({purple_cap['team']}) with {purple_cap['wickets']} wickets")

# Display top 5 run scorers
print("\nTop 5 Run Scorers:")
top_runs = df.sort_values(by='runs', ascending=False).head(5)
for i, player in top_runs.iterrows():
    print(f"{player['player']} ({player['team']}): {player['runs']} runs")

# Display top 5 wicket takers
print("\nTop 5 Wicket Takers:")
top_wickets = df.sort_values(by='wickets', ascending=False).head(5)
for i, player in top_wickets.iterrows():
    print(f"{player['player']} ({player['team']}): {player['wickets']} wickets")