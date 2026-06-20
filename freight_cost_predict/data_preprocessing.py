import sqlite3
from sklearn.model_selection import train_test_split
import pandas as pd

#Load Vendor Invoice Data From SQLite Database
def load_vendor_invoice_data(db_path: str):
    conn = sqlite3.connect(db_path)
    query = "SELECT * FROM vendor_invoice"
    df = pd.read_sql_query(query,conn)
    conn.close()
    return df

#Select features and target variable
def prepare_features(df: pd.DataFrame):
    X = df[["Quantity","Dollars"]]
    y = df["Freight"]
    return X,y

#Split Dataset into traning and testing
def split_data(X,y,test_size = 0.2 , random_state = 42):
    return train_test_split(
        X, y, test_size=test_size, random_state=random_state 
    )