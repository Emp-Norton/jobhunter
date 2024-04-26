import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px

from django_plotly_dash import DjangoDash

from jobhunter.apps.jobhunt.models import Application, CoverLetter, Company

# Set up the Dash app
app = DjangoDash('Job Application Dashboard', serve_locally=True)

# Define the data preparation functions
def get_data():
    applications = Application.objects.all()
    data = []
    for app in applications:
        data.append({
            'Company': app.company.name,
            'CoverLetter': app.coverletter.text,  # You might want to use a shorter representation
            'Application Id': app.id,
        })
    return data

def get_count_data():
    return [
        {'Company': appl.company.name, 'Count': CoverLetter.objects.filter(application=appl).count()}
        for appl in Application.objects.all()
    ]

df = get_data()
# Create the Dash layout
app.layout = html.Div(children=[
    html.H1(children='Job Application Dashboard'),

    dcc.Graph(
        id='applications-count-graph',
        figure={
            'data': [
                go.Bar(x=[entry['Company'] for entry in get_count_data()],
                       y=[entry['Count'] for entry in get_count_data()],
                       marker_color='rgb(0, 128, 0)',
                       name='Count of Applications')
            ],
            'layout': go.Layout(
                title='Number of Applications by Company',
                xaxis={'title': 'Company'},
                yaxis={'title': 'Count'},
                barmode='group'
            )
        }
    ),

    dcc.Graph(
        id='applications-by-cover-letter',
        figure={
            'data': [
                go.Scatter(x=df['Application Id'], y=df['Company'], text=df['CoverLetter'],
                           mode='markers', marker_size=12, hoverinfo='text')
            ],
            'layout': go.Layout(
                title='Applications by Cover Letter',
                xaxis={'title': 'Application ID'},
                yaxis={'title': 'Company'},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)