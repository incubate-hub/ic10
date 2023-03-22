import pickle
from sklearn.preprocessing import StandardScaler

# Load the model from the .sav file
with open('F:/Hackton/anomaly/anomaly/anomaly_model.sav', 'rb') as f:
    model = pickle.load(f)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
data = pd.read_csv("F:/Hackton/anomaly/anomaly/data.csv")
data = data.drop(['uniq_Op numeric', 'uniqOpnd numeric', 'total_Op numeric',
                 ' total_Opnd numeric', ' branchCount numeric'], axis=1)

X = data.drop(' defects',axis=1)
y = data[" defects"]
X_train, X_test, y_train, y_test = train_test_split(
    data.drop(' defects', axis=1), data[' defects'], test_size=0.2)

scaler = StandardScaler()
X_train_normalized = scaler.fit_transform(X_train)
X_test_normalized = scaler.transform(X_test)

def prediction_model(loc, v, ev, iv, n, v1, l, d, i, e, b, t, loCode_numeric, loComment_numeric, loBlank_numeric, locCodeAndComment_numeric):
    input_data = [loc, v, ev, iv, n, v1, l, d, i, e, b, t, loCode_numeric,
                    loComment_numeric, loBlank_numeric, locCodeAndComment_numeric]
    input_data = scaler.transform([input_data])
    prediction = model.predict(input_data)[0]
    if prediction == 0:
        prediction = "There is no anomaly"
    elif prediction == 1:
        prediction = "There is anomaly."
    else: 
      prediction = "Error"
    return prediction


if __name__ == "__main__":
    prediction_model(1.1,1.4,1.4,1.4,1.3,1.3,1.3,1.3,1.3,1.3,1.3,1.3,2,2,2,2)