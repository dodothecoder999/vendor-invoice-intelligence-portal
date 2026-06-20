import joblib
import pandas as pd

MODEL_PATH ="freight_cost_predict/models/predict_freight_model.pkl"

#Load Trained freight cost prediction model
def load_model(model_path :str = MODEL_PATH):
    with open(model_path,"rb") as f:
        model = joblib.load(f)
    return model

#Predict Freight cost for new vendor invoices
# Parameters   =  imput data :dict , returns : pd.DataFrame with predicted freight cost
def predict_freight_cost(input_data):
    model = load_model()
    input_df = pd.DataFrame(input_data)
    input_df['Predicted_Freight'] = model.predict(input_df).round()
    return input_df

if __name__ == "__main__":

    #Example inference run (local testing)
    sample_data = {
        "Dollars" : [18500,9000]
    }
    prediction = predict_freight_cost(sample_data)
    print(prediction)

   
    