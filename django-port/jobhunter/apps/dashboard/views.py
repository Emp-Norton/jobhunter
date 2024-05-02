# dashboard/views.py
from dash import html, dcc, Output, Input
from django.db.models import Count
from django_plotly_dash import DjangoDash
from jobhunter.apps.jobhunt.models import Application

import plotly.express as px

# Create a Django Dash app instance
app = DjangoDash('Dashboard', external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
# Dashboard layout
app.layout = html.Div(children=[
    html.H1(children='Application Dashboard'),

    dcc.Graph(id='applications-by-company'),
    dcc.Interval(id='interval-component', interval=5000, n_intervals=0)
])


# Define callbacks to update the graphs
@app.callback(
    Output('applications-by-company', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_applications_graph(n):
    # Get the data and create the visualization
    data = Application.objects.all().values('company__name').annotate(Count('id')).order_by('company__name')

    fig = px.bar(data, x='company__name', y='id__count', title='Applications by Company')
    return fig


def index(request):
    return render(request, 'dashboard/index.html', {'app': app})


from django.shortcuts import render

# Create your views here.
