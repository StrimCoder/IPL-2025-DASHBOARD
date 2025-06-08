import pandas as pd
import plotly.express as px

def points_table_race(df):
    # Create points table: 2 points for win, 0 for loss
    df_sorted = df.sort_values(by="match_id")

    teams = pd.unique(df_sorted[["team1", "team2"]].values.ravel())
    points_dict = {team: 0 for team in teams}

    frames = []
    match_ids = df_sorted["match_id"].unique()

    for match in match_ids:
        match_df = df_sorted[df_sorted["match_id"] == match]
        winner = match_df["winner"].values[0]
        if winner in points_dict:
            points_dict[winner] += 2

        temp_df = pd.DataFrame({
            "team": list(points_dict.keys()),
            "points": list(points_dict.values()),
            "match_id": f"Match {match}"
        })
        frames.append(temp_df)

    final_df = pd.concat(frames)

    fig = px.bar(final_df, 
                 x="points", y="team",
                 color="team",
                 animation_frame="match_id",
                 orientation="h",
                 title="🏆 Points Table Race (Match by Match)",
                 range_x=[0, max(final_df["points"]) + 2])

    fig.update_layout(showlegend=False)
    return fig