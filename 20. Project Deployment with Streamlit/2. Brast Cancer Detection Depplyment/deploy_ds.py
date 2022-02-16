import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np

def train_model():
    from sklearn.datasets import load_breast_cancer
    from keras.models import Sequential
    from keras.layers import Dense
    data = load_breast_cancer()
    feature = data['data']
    label = data['target']
    scale = StandardScaler()
    feature = scale.fit_transform(feature)
    df_frt = pd.DataFrame(feature , columns = data['feature_names'])
    df_lbl = pd.DataFrame(label , columns = ['label'])
    df = pd.concat([df_frt, df_lbl], axis=1)
    feature = df.values[ : , : 30]
    label = df.values[ : ,30: ]
    X_train = feature[:]
    y_train = label[:]
    model = Sequential()
    model.add(Dense(32, activation = 'relu', input_dim = 30))
    model.add(Dense(64, activation = 'relu'))
    model.add(Dense(128, activation = 'relu'))
    model.add(Dense(64, activation = 'relu'))
    model.add(Dense(32, activation = 'relu'))
    model.add(Dense(1, activation = 'sigmoid'))
    model.compile( loss = 'binary_crossentropy' , optimizer = 'adam' , metrics = ['accuracy'])
    model.fit( X_train , y_train, epochs = 10, batch_size = 5)
    return model


@st.cache
def expensive_computation(features,length):
    outcome = []
    model= train_model()
    for i in range(length):
        sample = np.reshape(features[i], (1,30))
        if (model.predict(sample)[0][0] > 0.5):
            outcome.append(["Test_Case_{}".format(i+1),"Benign"])
        else:
            outcome.append(["Test_Case_{}".format(i+1),"Malignant"])

    return outcome



st.title('Breast Cancer Model Deployemnt Portal')
uploaded_file = st.file_uploader("Choose a CSV file with 30 input parameters to make predictions.")
if uploaded_file is not None:
     # Can be used wherever a "file-like" object is accepted:
     dataframe = pd.read_csv(uploaded_file)
     st.header('Your uploaded Test set')
     st.write(dataframe)
     scale = StandardScaler()
     feature = scale.fit_transform(dataframe)
     len_test_dataset = len(feature)
     outcomes = expensive_computation(feature,len_test_dataset)
     st.header('Predictions from our Model. Expand to View')
     st.write(outcomes)





    






