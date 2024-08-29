# pip install pymysql
import sqlalchemy
import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Replace these with your actual MySQL database credentials
# Database connection string
username = 'vikkiez'
password = 'Vikky#844'
host = 'localhost'
database = 'test'
port = "3306"

# Create the SQLAlchemy engine for MySQL
engine = sqlalchemy.create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

# Function to access data from MySQL table
def load_sql_data(query):
    try:
        df = pd.read_sql_query(query, engine)
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to generate a bar plot
def barplot(query):
    df = load_sql_data(query)
    location_counts = df['location'].value_counts().reset_index()
    location_counts.columns = ['location', 'job_count']
    plt.figure(figsize=(10, 6))
    sns.barplot(x='location', y='job_count', data=location_counts)
    plt.xticks(rotation=45, ha='right')
    plt.title('Job Distribution by Location')
    plt.xlabel('Location')
    plt.ylabel('Number of Jobs')
    plt.tight_layout()
    plt.savefig('/home/vignesh-nadar/Desktop/sixtyDays/sprint1/project1/visualization/job_distribution_by_location_bar.png')
    plt.close()

barplot("SELECT location FROM jobsTable")