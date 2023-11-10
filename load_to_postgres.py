import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# Define the database connection parameters
db_params = {
 'host': 'localhost'
, 'database': 'postgres'
, 'user': 'your user name inserted here'
, 'password': 'your password here'
}

# Function to create a new database
def create_database(db_params):
    try:
        # Create connection to Postgres server
        with psycopg2.connect(
        host=db_params['host'],
        database=db_params['database'],
        user=db_params['user'],
        password=db_params['password']
        ) as conn:
            conn.set_session(autocommit=True)
        with conn.cursor() as cur:
            # Check if the database already exists
            db_params['database'] = 'repos'
            cur.execute("SELECT * FROM pg_catalog.pg_database WHERE datname = %s", (db_params['database'],))
                       
            exists = cur.fetchall()
            for row in exists:
                print(row)
            if not exists:
            # Create the database
                cur.execute(f"CREATE DATABASE {db_params['database']}")
                print(f"Database {db_params['database']} created successfully.")
            else:
                print(f"Database {db_params['database']} already exists.")
    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
        
# Call the function to create the database
create_database(db_params)

# connect to the repos database
engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}/{db_params["database"]}')

# define the file paths for your CSV files
csv_files = {
'repository_data': 'commit_data.csv' # Replace with the correct path
}

# load and display the contents of each CSV file to check
for table_name, file_path in csv_files.items():
    print(f"Contents of '{table_name}' CSV file:")
    df = pd.read_csv(file_path)
    display(df.head()) # display the first few rows of the DataFrame
    print("\n")
    
# Loop through the CSV files and import them into PostgreSQL
for table_name, file_path in csv_files.items():
    df = pd.read_csv(file_path)
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    with psycopg2.connect(
        host=db_params['host'],
        database=db_params['database'],
        user=db_params['user'],
        password=db_params['password']
        ) as conn:
            conn.set_session(autocommit=True)
    with conn.cursor() as cur:
            # Check if the database already exists
            db_params['database'] = 'repos'
            cur.execute("SELECT * FROM repository_data LIMIT 5", (db_params['database'],))
                       
            exists = cur.fetchall()
            for row in exists:
                print(row) #check to see if it worked