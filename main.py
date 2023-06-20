import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='Create a Gantt diagram in python from a csv')
parser.add_argument('task_file', help='Task to the csv that represent the tasks')
parser.add_argument('--m', nargs='?', help='Optional - Path to the csv that represent the milestones')

args = parser.parse_args()

# tasks
df = pd.read_csv(args.task_file, sep=';')
df['Start'] = pd.to_datetime(df['Start'], format='%d/%m/%Y')
df['Finish'] = pd.to_datetime(df['Finish'], format='%d/%m/%Y')
tasks = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Type")
tasks.update_traces(marker=dict(line=dict(width=1, color='black')))
tasks.update_yaxes(autorange='reversed')

# milestones
if args.m:
    df_milestones = pd.read_csv(args.m, sep=';')
    df_milestones['Due'] = pd.to_datetime(df_milestones['Due'], format='%d/%m/%Y')
    milestones = px.scatter(df_milestones, x="Due", y="Task", color="Type", symbol_sequence=['diamond'], color_discrete_sequence=px.colors.qualitative.Alphabet)
    milestones.update_traces(marker=dict(size=12, line=dict(width=2)))
    fig = go.Figure(data=tasks.data+milestones.data, layout=tasks.layout)
else:
    fig = go.Figure(data=tasks.data, layout=tasks.layout)

fig.show()
