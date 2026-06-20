import joblib
import pandas as pd

MODEL_PATH = "models/predict_flag_invoice.pkl"

#Load Trained freight cost prediction model
def load_model(model_path :str = MODEL_PATH):
    with open(model_path,"rb") as f:
        model = joblib.load(f)
    return model 

#Predict Invoice cost for new vendor invoices
# Parameters   =  imput data :dict , returns : pd.DataFrame with predicted invoice cost
def predict_invoice_flag(input_data):
    model = load_model()
    input_df = pd.DataFrame(input_data)
    input_df['Predicted_Flag'] = model.predict(input_df).round()
    return input_df

if __name__ == "__main__":
    pass

   
    