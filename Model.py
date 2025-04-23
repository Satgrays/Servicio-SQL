# Import necessary libraries
import json
import pyodbc
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings("ignore")


# Open config from .json file
with open('keys.json') as config_file:
    config = json.load(config_file)

# Extract database connection parameters
server = config['server']
database = config['database']
username = config['username']
password = config['password']

# Define the connection string for SQL Server (Azure)
conn_str = (
    f'DRIVER={{ODBC Driver 18 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password}'
)

# Establish the connection
try:
    conn = pyodbc.connect(conn_str)
    print("Connected to the Azure SQL Database successfully!")

except pyodbc.Error as e:
    print(f"Error connecting to the database: {e}")

# Obtain the data from the database
query = "SELECT * FROM SalesLT.customer"
df = pd.read_sql(query, conn)
conn.close()


# Process and clean the data
data = df[['CompanyName', 'Suffix', 'SalesPerson', 'ModifiedDate']].copy()
data['ModifiedDate_num'] = (data['ModifiedDate'] - data['ModifiedDate'].min()).dt.days


X = data[[ 'CompanyName', 'Suffix', 'SalesPerson']]
X_encoded = pd.get_dummies(X, drop_first=True)
y = data['ModifiedDate_num']

X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

joblib.dump(model, 'model.pkl')