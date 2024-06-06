import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

model = load_model('kfall_os.keras')

st.title('FALL PREDICTION WITH KFALL DATASET')

st.header('Enter Sensor Data:')
t_sin_s = st.number_input('t_sin_s', value=0.0, format="%.4f")
t_cos_s = st.number_input('t_cos_s', value=0.0, format="%.4f")
t_sin_m = st.number_input('t_sin_m', value=0.0, format="%.4f")
t_cos_m = st.number_input('t_cos_m', value=0.0, format="%.4f")
AccX = st.number_input('AccX', value=0.0, format="%.4f")
AccY = st.number_input('AccY', value=0.0, format="%.4f")
AccZ = st.number_input('AccZ', value=0.0, format="%.4f")
GyrX = st.number_input('GyrX', value=0.0, format="%.4f")
GyrY = st.number_input('GyrY', value=0.0, format="%.4f")
GyrZ = st.number_input('GyrZ', value=0.0, format="%.4f")
EulerX = st.number_input('EulerX', value=0.0, format="%.4f")
EulerY = st.number_input('EulerY', value=0.0, format="%.4f")
EulerZ = st.number_input('EulerZ', value=0.0, format="%.4f")

input_data = np.array([[t_sin_s, t_cos_s, t_sin_m, t_cos_m, AccX, AccY, AccZ, GyrX, GyrY, GyrZ, EulerX, EulerY, EulerZ]])
input_data = input_data.reshape((input_data.shape[0], 1, input_data.shape[1]))

prediction = model.predict(input_data)
predicted_class = np.argmax(prediction)

st.sidebar.subheader('Prediction:')
prediction_text = ""
if predicted_class == 0:
    prediction_text = "No Fall"
elif predicted_class == 1:
    prediction_text = "Pre Impact Fall"
elif predicted_class == 2:
    prediction_text = "Fall"

st.sidebar.text(prediction_text)
