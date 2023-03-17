import snowflake.connector
import pandas as pd
import numpy as np

# USER CREDENTIALS
USER = ''
ACCOUNT = ''
PASSWORD = os.environ.get('PASSWORD')
# The preferred account identifier includes the name of the account along with its organization (e.g. myorg-account123)
# Find this info in your dashboard > Admin ( Left side bar ) > Accounts
# The ORG will be listed at the top above all the accounts
# The account will be the value in the column 'ACCOUNT' for the account you wish to use. 

# Setting the connection to the snowflake warehouse
WAREHOUSE = 'COMPUTE_WH'
DATABASE = 'SNOWFLAKE_SAMPLE_DATA'
SCHEMA = 'TPCDS_SF100TCL'

# Creates the connection 
conn = snowflake.connector.connect(
    user=USER,
    password=PASSWORD,
    account=ACCOUNT,
    warehouse=WAREHOUSE,
    database=DATABASE,
    schema=SCHEMA
    )

# Cursor to use for executions
cur = conn.cursor()

# Query Data
# Select all values from inventory table where the quantity of items is below 50 units
cur.execute("SELECT * FROM INVENTORY WHERE INV_QUANTITY_ON_HAND<1")

# Export to pandas dataframe
df = cur.fetch_pandas_all()

# Close Connection from snowflake
conn.close()


# Execute pandas operations
# Simple Overview
print(len(df.index))