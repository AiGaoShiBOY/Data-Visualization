import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


def line_scatter_type():
    df = pd.read_csv('lab3-datasets/college-salaries/salaries-by-region.csv')
    df = df.sample(frac=0.5, axis=0, random_state=123)
    df.reset_index(inplace=True, drop=True)
    fig = go.Figure()
    for i in range(0, len(df)):
        fig.add_trace(go.Scatter(name=df["School Name"][i], x=['10th','25th','75th','90th'], y=[df["Mid-Career 10th Percentile Salary"][i],
                                                                            df["Mid-Career 25th Percentile Salary"][i],
                                                                            df["Mid-Career 75th Percentile Salary"][i],
                                                                            df["Mid-Career 90th Percentile Salary"][i]]))
    fig.update_layout(
        yaxis_title="Mid-Career Salary",
        xaxis_title = "Percentile"
    )
    return fig

def line_scatter_degree():
    df = pd.read_csv('lab3-datasets/college-salaries/degrees-that-pay-back.csv')
    df = df.sample(frac=0.5, axis=0, random_state=123)
    df.reset_index(inplace=True, drop=True)
    a = df[
        ["Mid-Career 10th Percentile Salary", "Mid-Career 25th Percentile Salary", "Mid-Career 75th Percentile Salary",
         "Mid-Career 90th Percentile Salary"]]
    fig = go.Figure()
    for i in range(0, len(df)):
        fig.add_trace(go.Scatter(name=df["Undergraduate Major"][i], x=['10th','25th','75th','90th'], y=[df["Mid-Career 10th Percentile Salary"][i],
                                                                            df["Mid-Career 25th Percentile Salary"][i],
                                                                            df["Mid-Career 75th Percentile Salary"][i],
                                                                            df["Mid-Career 90th Percentile Salary"][i]]))
    fig.update_layout(
        yaxis_title="Mid-Career Salary",
        xaxis_title="Percentile"
    )
    return fig

def line_scatter_region():
    df = pd.read_csv('lab3-datasets/college-salaries/salaries-by-region.csv')
    df = df.sample(frac=0.5, axis=0, random_state=123)
    df.reset_index(inplace=True, drop=True)

    a = df[
        ["Mid-Career 10th Percentile Salary", "Mid-Career 25th Percentile Salary", "Mid-Career 75th Percentile Salary",
         "Mid-Career 90th Percentile Salary"]]
    fig = go.Figure()
    for i in range(0, len(df)):
        fig.add_trace(go.Scatter(name=df["School Name"][i], x=a.columns, y=[df["Mid-Career 10th Percentile Salary"][i],
                                                                            df["Mid-Career 25th Percentile Salary"][i],
                                                                            df["Mid-Career 75th Percentile Salary"][i],
                                                                            df["Mid-Career 90th Percentile Salary"][
                                                                                i]]))
    fig.update_layout(
        yaxis_title="Mid-Career Salary",
        xaxis_title="Percentile"
    )
    return fig

def bubble_plot_region():
    df = pd.read_csv('lab3-datasets/college-salaries/salaries-by-region.csv')

    # Sampling
    df = df.sample(frac=0.5, axis=0, random_state=123)

    fig = px.scatter(df, x="Starting Median Salary", y="Mid-Career Median Salary",
                     size="Mid-Career 75th Percentile Salary", color="Region", hover_name="School Name",
                     log_x=True, size_max=15,template='ggplot2')

    return fig


def bubble_plot_degree():
    df = pd.read_csv('lab3-datasets/college-salaries/degrees-that-pay-back.csv')

    df = df.sample(frac=0.5, axis=0, random_state=123)

    fig = px.scatter(df, x="Starting Median Salary", y="Mid-Career Median Salary",
                     size="Mid-Career 75th Percentile Salary", color="Undergraduate Major",
                     hover_name="Undergraduate Major",
                     log_x=True, size_max=15, template='plotly_white')

    return fig



def bubble_plot_type():
    df = pd.read_csv('lab3-datasets/college-salaries/salaries-by-college-type.csv')

    # Sampling
    df = df.sample(frac=0.5, axis=0, random_state=123)
    fig = px.scatter(df, x="Starting Median Salary", y="Mid-Career Median Salary",
                     size="Mid-Career 75th Percentile Salary", color="School Type", hover_name="School Name",
                     log_x=True, size_max=15)

    return fig


def bar_chart_college(value):
    df = pd.read_csv('lab3-datasets/college-salaries/salaries-by-college-type.csv')
    df = df.iloc[df.groupby(['School Name']).apply(
        lambda x: x['Starting Median Salary'].idxmax())]
    # df = df.sample(frac=0.15, axis=0, random_state=123)
    df.reset_index(inplace=True, drop=True)
    df['Rate'] = (
            (df["Mid-Career Median Salary"] - df["Starting Median Salary"]) * 100 / df["Starting Median Salary"])
    df['Rate'] = [format(x, '.1f') for x in df['Rate']]
    df['Rate'] = df['Rate'].astype("float")
    df = df[value[0] <= df["Rate"]]
    df = df[df["Rate"] <= value[1]]
    fig = px.bar(df, x='School Name', y='Rate',color='Rate',height=800)
    fig.update_layout(
        yaxis_title="Growth Rate (percentile)",
    )
    return fig

def bar_chart_degree(value):
    df = pd.read_csv('lab3-datasets/college-salaries/degrees-that-pay-back.csv')

    df = df[value[0] <= df["Percent change from Starting to Mid-Career Salary"]]
    df = df[df["Percent change from Starting to Mid-Career Salary"] <= value[1]]
    df["Rate"]=df["Percent change from Starting to Mid-Career Salary"]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Undergraduate Major'], y=df['Rate'],
                              marker=dict(
                                  color=df['Rate']
                              ),
                             line=dict(
                                 color='green'
                             ),
                             mode='lines+markers',
                             name='lines+markers'))
    fig.update_layout(
        # title="Percent Change from Starting to Mid-Career Salary",
        yaxis_title="Growth Rate (percentile)",
    )
    return fig



def histogram():
    df = pd.read_csv('lab3-datasets/college-salaries/salaries-by-college-type.csv')
    # fig = px.histogram(df, x="Starting Median Salary")
    trace1 = go.Histogram(x=df["Starting Median Salary"],name='Start')
    trace2 = go.Histogram(x=df["Mid-Career Median Salary"],name='Mid-Career')
    layout = go.Layout(
        barmode='overlay'
    )
    data = [trace1, trace2]
    fig = go.Figure(data=data, layout=layout)
    fig.update_layout(
        # title="Percent Change from Starting to Mid-Career Salary",
       title="Growth Rate (percentile)",
    )
    return fig


