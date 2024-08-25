# pip install pymysql
import sqlalchemy
import pymysql
import pandas as pd

# Replace these with your actual MySQL database credentials
username = "your_username"
password = "your_password"
host = "your_host"
port = "3306"  # Default MySQL port
database = "your_database_name"

# Create the SQLAlchemy engine for MySQL
engine = sqlalchemy.create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

# Load data into MySQL
df.to_sql('your_table_name', engine, if_exists='replace', index=False)

# Query data from MySQL
query = "SELECT * FROM your_table_name"
df = pd.read_sql_query(query, engine)

def load_sql_data(query):
    return pd.read_sql_query(query, engine)

def create_bar_chart(df, x, y, title):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=x, y=y, data=df)
    plt.title(title)
    plt.savefig(f'{title.lower().replace(" ", "_")}.png')
    plt.close()

def create_line_chart(df, x, y, title):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=x, y=y, data=df)
    plt.title(title)
    plt.savefig(f'{title.lower().replace(" ", "_")}.png')
    plt.close()

# Usage
df = load_sql_data("SELECT * FROM your_table_name")
create_bar_chart(df, 'category', 'value', 'Sales by Category')
create_line_chart(df, 'date', 'value', 'Sales Over Time')