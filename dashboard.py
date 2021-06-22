import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

import preparation

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
                        "//netdna.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]



app = dash.Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)

app.layout = html.Div([
    html.H1([html.I(
        className="fa fa-eye"
    ),' Data Visualization of College Salaries'],style={'margin-buttom':'1cm','margin-top':'1cm'}),
    html.H2([html.I(className="fa fa-bullseye"), " Scattered Distribution"], style={'margin-top': '1cm'}),
    html.Div([
        dcc.Graph(
            id='bubble-plot',
            figure=preparation.bubble_plot_type(),
            style={'height':'500px','margin-left': 'auto', 'margin-right': 'auto'}
        ),
        dcc.Dropdown(
            id='dropdown-value',
            options=[
                {'label': 'Filter by College Type ', 'value': 'type'},
                {'label': 'Filter by Major', 'value': 'degree'},
                {'label': 'Filter by Region', 'value': 'region'},
            ],
            value='type',
            style={'width':'220px','margin-left':'auto','margin-right':'auto'},
            clearable=False
        )
    ], style={'width': '60%','margin-left':'auto','margin-right':'auto','height':'600px','display': 'block','margin-top':'1cm', 'text-align':'left'}),
    html.H2([html.I(className="fa fa-line-chart"), " Mid-Career Percentage Salary"], style={'margin-top': '1cm'}),
    html.Div([
        dcc.Graph(
            id='line-scatter',
            figure=preparation.line_scatter_type(),
            style={'height':'500px'}
        ),
        dcc.Dropdown(
            id='dropdown-value2',
            options=[
                {'label': 'Filter by College Name', 'value': 'type'},
                {'label': 'Filter by Major', 'value': 'degree'},
            ],
            value='type',
            style={'width':'220px','margin-left':'auto','margin-right':'auto','text-align':'left'},
            clearable=False
        )
    ], style={'width': '80%','margin-left':'auto','margin-right':'auto','height':'600px','display': 'block'}),
    html.H2([html.I(className="fa fa-area-chart"), " Median Salary Distribution"], style={'margin':'0'}),
    html.Div([
        dcc.Graph(
            id='bar-chart_college',
            figure=preparation.histogram(),
            style={'width': '70%', 'margin-left': '15%'}
        ),
    ], id="histogram-content"),
    html.H2([html.I(className="fa fa-bar-chart"), " Salary Growth Rate from Starting to Mid-Career (%)"],style={'margin-top':'1cm'}),
    html.Div([
        dcc.Tabs(id="tabs-styled-with-props", value='tab-2', children=[
            dcc.Tab(label='Major', value='tab-2'),
            dcc.Tab(label='College', value='tab-1'),
        ], colors={
            "border": "white",
            "primary": "DeepSkyBlue",
            "background": "white"
        }),
    ], style={'width': '20%', 'display': 'inline-block', 'margin': '20px'}),
    html.Div(id='tabs-content-props',style={'width':'80%','margin':'auto'}),
    html.Div([
        html.P([html.I(className="fa fa-flag"),' Designer: Li Yuanfeng'],style={'font-family':'Avenir','font-size':'24px','font-wight':'bold'}),
        html.Div([html.A([html.I(className="fa fa-github")], href="https://github.com/AiGaoShiBOY/Data-Visualization", style={'color':'rgb(35,103,197)'})], style={'width':'50px','height':'50px','margin':'10px auto',
                                                                     'color':'white','font-size':'50px',
                                                                     'line-height':'50px'}),
        html.P([' 2020.6'],style={'font-family':'Avenir','font-size':'24px','font-wight':'bold'}),

    ],style={'margin-top':'2cm'})

], style={'text-align':'center'},)


@app.callback(Output('tabs-content-props', 'children'),
              Input('tabs-styled-with-props', 'value'),
              suppress_callback_exceptions=True)
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            dcc.RangeSlider(
                id='my-range-slider1',
                min=0,
                max=120,
                step=10,
                value=[40,80],
                marks={
                    0: '0',
                    40: '40',
                    80: '80',
                    120: '120',
                }

            ),
            html.Div(id='output-container-range-slider1', style={'margin':'auto'}),
        ])
    elif tab == 'tab-2':
        return html.Div([
            dcc.RangeSlider(
                id='my-range-slider2',
                min=0,
                max=100,
                step=5,
                value=[30,70],
                marks = {
                    0:'0',
                    20:'20',
                    40:'40',
                    60:'60',
                    80:'80',
                    100:'100'
                }
            ),
            html.Div(id='output-container-range-slider2', style={'margin':'auto'}),
        ])


@app.callback(
    Output('output-container-range-slider1', 'children'),
    Input('my-range-slider1', 'value'),
    suppress_callback_exceptions=True)
def update_output(value):
    return html.Div([
        'Range: {}'.format(value),
        dcc.Graph(
             id='bar-chart_college',
            figure=preparation.bar_chart_college(value)
         ),
    ])


@app.callback(
    Output('output-container-range-slider2', 'children'),
    Input('my-range-slider2', 'value'),)
def update_output(value):
    return html.Div([
        'Rate Range: {}'.format(value),
        dcc.Graph(
             id='bar-chart_degree',
            figure=preparation.bar_chart_degree(value)
         ),
    ])


@app.callback(
    Output('bubble-plot', 'figure'),
    Input('dropdown-value', 'value'))
def update_bubble(value):
    if value == "region":
        return preparation.bubble_plot_region()
    elif value == "type":
        return preparation.bubble_plot_type()
    elif value == "degree":
        return preparation.bubble_plot_degree()

@app.callback(
    Output('line-scatter', 'figure'),
    Input('dropdown-value2', 'value'))
def update_scatter(value):
    if value == "type":
        return preparation.line_scatter_type()
    elif value == "degree":
        return preparation.line_scatter_degree()



if __name__ == '__main__':
    app.run_server(debug=True)
