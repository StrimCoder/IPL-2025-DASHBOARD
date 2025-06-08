import streamlit as st
import pandas as pd
import plotly.express as px
from visualizations import points_table_race
from data_cleaning import load_match_data, load_player_data

# Set page title and add logo
st.set_page_config(page_title="IPL 2025 Dashboard", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }
    .sidebar-nav {
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .section-divider {
        margin-top: 20px;
        margin-bottom: 20px;
        border-top: 1px solid #e0e0e0;
    }
    .main-divider {
        margin-top: 10px;
        margin-bottom: 30px;
        border-top: 3px solid #0066cc;
        border-radius: 2px;
    }
    .sidebar-title {
        font-weight: bold;
        color: #0066cc;
        margin-bottom: 10px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        margin-bottom: 10px;
        background-color: #0066cc;
        color: white;
    }
    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(90deg, #0066cc, #ff9933);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding: 20px 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .subtitle {
        text-align: center;
        font-size: 1.5rem;
        margin-bottom: 30px;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)

# Add stylish title in the middle
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<div class='main-title'>IPL 2025 DASHBOARD</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Comprehensive Analytics & Visualizations</div>", unsafe_allow_html=True)

# Add IPL image
st.image("https://www.hindustantimes.com/ht-img/img/2023/12/20/1600x900/Ipl-auction_1703034762917_1703034773943.jpg", width=1600)

# Add a partition/divider after the image
st.markdown("<div class='main-divider'></div>", unsafe_allow_html=True)

# Load data
match_data = load_match_data()
player_data = load_player_data()

# Define functions for other tabs
def top_run_scorers(df):
    top_players = df.sort_values('runs', ascending=False).head(10)
    fig = px.bar(top_players, x='player', y='runs', title='Top Run Scorers', color='team')
    return fig

def top_wicket_takers(df):
    top_bowlers = df.sort_values('wickets', ascending=False).head(10)
    fig = px.bar(top_bowlers, x='player', y='wickets', title='Top Wicket Takers', color='team')
    return fig

def team_win_percent(df):
    team_wins = df['winner'].value_counts().reset_index()
    team_wins.columns = ['team', 'wins']
    total_matches = len(df)
    team_wins['win_percent'] = (team_wins['wins'] / total_matches) * 100
    fig = px.pie(team_wins, values='win_percent', names='team', title='Team Win Percentage')
    return fig

def runs_per_match(df):
    # Sum team1_runs and team2_runs for each match
    df['total_runs'] = df['team1_runs'] + df['team2_runs']
    runs_by_match = df[['match_id', 'total_runs']]
    fig = px.line(runs_by_match, x='match_id', y='total_runs', title='Runs per Match', markers=True)
    return fig

def orange_cap_race(df):
    top_batsmen = df.sort_values('runs', ascending=False).head(5)
    fig = px.bar(top_batsmen, x='player', y='runs', title='Orange Cap Race', color='team')
    return fig

def purple_cap_race(df):
    top_bowlers = df.sort_values('wickets', ascending=False).head(5)
    fig = px.bar(top_bowlers, x='player', y='wickets', title='Purple Cap Race', color='team')
    return fig

# Create beautiful sidebar
st.sidebar.image("https://www.iplt20.com/assets/images/ipl-logo-new-old.png", width=200)
st.sidebar.markdown("<div class='sidebar-title'>IPL 2025 DASHBOARD</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# Data section
st.sidebar.markdown("<div class='sidebar-title'>📊 DATA VIEWS</div>", unsafe_allow_html=True)
data_view = st.sidebar.radio(
    "",
    ["Match Stats", "Player Stats"],
    key="data_section"
)

st.sidebar.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# Team Analysis section
st.sidebar.markdown("<div class='sidebar-title'>🏏 TEAM ANALYSIS</div>", unsafe_allow_html=True)
team_view = st.sidebar.radio(
    "",
    ["Team Win %", "Run Trends", "Points Table Race"],
    key="team_section"
)

st.sidebar.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# Player Analysis section
st.sidebar.markdown("<div class='sidebar-title'>👤 PLAYER ANALYSIS</div>", unsafe_allow_html=True)
player_view = st.sidebar.radio(
    "",
    ["Orange Cap Race", "Purple Cap Race"],
    key="player_section"
)

# Determine which page to show based on all radio selections
selected_page = None
if data_view in ["Match Stats", "Player Stats"]:
    selected_page = data_view
elif team_view in ["Team Win %", "Run Trends", "Points Table Race"]:
    selected_page = team_view
elif player_view in ["Orange Cap Race", "Purple Cap Race"]:
    selected_page = player_view

# Display the selected page
if selected_page == "Match Stats":
    st.header("Match Statistics")
    st.dataframe(match_data)

elif selected_page == "Player Stats":
    st.header("Player Statistics")
    st.dataframe(player_data)

elif selected_page == "Team Win %":
    st.plotly_chart(team_win_percent(match_data), use_container_width=True)

elif selected_page == "Run Trends":
    st.plotly_chart(runs_per_match(match_data), use_container_width=True)

elif selected_page == "Orange Cap Race":
    st.plotly_chart(orange_cap_race(player_data), use_container_width=True)

elif selected_page == "Purple Cap Race":
    st.plotly_chart(purple_cap_race(player_data), use_container_width=True)

elif selected_page == "Points Table Race":
    st.plotly_chart(points_table_race(match_data), use_container_width=True)