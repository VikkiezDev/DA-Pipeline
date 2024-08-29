from sqlalchemy import create_engine
import pandas as pd

df = pd.read_csv("/home/vignesh-nadar/Desktop/sixtyDays/sprint1/project1/data/processed_data/processed_data.csv")

# Database connection string
username = 'vikkiez'
password = 'Vikky#844'
host = 'localhost'
database = 'test'

# Create SQLAlchemy engine
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}/{database}')

# Load data into the SQL database
df.to_sql('jobsTable', engine, if_exists='replace', index=False)
print("Data loaded successfully into the SQL database.")
