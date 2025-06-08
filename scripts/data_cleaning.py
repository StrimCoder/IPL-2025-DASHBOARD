import pandas as pd

def load_match_data():
    return pd.read_csv("data/ipl_2025_matches.csv")

def load_player_data():
    return pd.read_csv("data/ipl_2025_players.csv")