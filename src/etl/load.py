from sqlalchemy import create_engine
import pandas as pd

def load_to_sql(data):
    # Convert the transformed data to a DataFrame
    df = pd.DataFrame(data)

    # Database connection string
    username = 'your_username'
    password = 'your_password'
    host = 'localhost'
    database = 'your_database_name'

    # Create SQLAlchemy engine
    engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}/{database}')

    # Load data into the SQL database
    df.to_sql('your_table_name', engine, if_exists='replace', index=False)
    print("Data loaded successfully into the SQL database.")
