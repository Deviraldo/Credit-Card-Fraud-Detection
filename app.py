import streamlit as st
import numpy as np
import pickle # or import joblib

# --- STEP 1: LOAD THE MODEL ---
# Replace 'credit_card_model.pkl' with your actual filename
model = pickle.load(open('credit_card_model.pkl', 'rb')) 

st.title("Credit Card Fraud Detection")
input_df = st.text_input("Enter All Required Features Values")

# --- STEP 2: SPLIT THE INPUT ---
# Using the standard .split() method
input_df_splited = input_df.split(",")

submit = st.button("Submit")

if submit:
    # --- STEP 3: USE THE SPLIT LIST ---
    # Reference the variable name 'input_df_splited' exactly as defined above
    np_df = np.asarray(input_df_splited, dtype=np.float64)
    
    prediction = model.predict(np_df.reshape(1, -1))

    if prediction[0] == 0:
        st.write("Legitimate Transaction")
    else:
        st.write("Fraud Transaction")
