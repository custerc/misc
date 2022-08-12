import os
import psycopg2
from psycopg2 import Error


# Run the following command in the command line to set the environment variable with your CockroachDB connection string
# export DATABASE_URL="your_connection_string_goes_here"

def create_table():
    try:
        #create the connection
        connection = psycopg2.connect(os.environ["DATABASE_URL"])
        cursor = connection.cursor()
       
        # SQL query to create a new table
        create_table_query = "CREATE TABLE IF NOT EXISTS bikes (id INT PRIMARY KEY, title STRING, price INT);"
        cursor.execute(create_table_query)
        
        # commit the query and print result
        connection.commit()
        print("Table created successfully in CockroachDB ")
    
    except (Exception, Error) as error:
        print("Error creating table.", error)

create_table()