import requests
from bs4 import BeautifulSoup
import psycopg2

# Define the database connection parameters
database = "your_database"
username = "your_username"
password = "your_password"
host = "192.168.1.100"  # replace with the IP address of the machine running the database
port = 5432

# Define the URL to scrape
url = "https://www.example.com"

# Connect to the database
conn = psycopg2.connect(
    dbname=database,
    user=username,
    password=password,
    host=host,
    port=port
)
cur = conn.cursor()

# Send a request to the URL and get the HTML response
response = requests.get(url)
html = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Extract the data you want from the HTML
data = []
for tag in soup.find_all('h2'):
    data.append(tag.text.strip())

# Insert the data into the database
cur.executemany("INSERT INTO your_table (column_name) VALUES (%s)", data)

# Commit the changes and close the database connection
conn.commit()
cur.close()
conn.close()
