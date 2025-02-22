import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import json

file_path = "car_price_prediction.csv"
data = pd.read_csv(file_path)

data["Mileage"] = pd.to_numeric(data["Mileage"], errors= "coerce")

numeric_data = data.select_dtypes(include=['number'])

correlation_matrix = numeric_data.corr()
correlation_matrix_target = correlation_matrix["Price"].sort_values(ascending=False)

top_features = correlation_matrix_target.index[1:3].to_list()
print("Selected Top Features:")
print(top_features)

selected_data = data[top_features+["Price"]].dropna()
X = selected_data[top_features]
y = selected_data["Price"]

X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(X_train,y_train)

model_path = "model/cpp_model.pkl"
with open(model_path,"wb") as file:
    pickle.dump(model,file)
print(f"cpp_model has been save successfully")

feature_ranges = {
    feature:{
        "min": float(selected_data[feature].min()),
        "max": float(selected_data[feature].max())                           
    }
    for feature in top_features
}

ranges_path = "model/feature_ranges.json"
with open(ranges_path,"w") as file:
    json.dump(feature_ranges,file)

print("feature_ranges succesfully saved")
