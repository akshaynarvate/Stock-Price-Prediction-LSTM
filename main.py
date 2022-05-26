import numpy as np
import pandas as pd
import streamlit as st
import pickle
import warnings

warnings.filterwarnings("ignore")
model = pickle.load(open("Model_Reliance_LSTM.pkl","rb")) #loading the created model


st.set_page_config(page_title="Reliance Stock Prediciton Application") #tab title

#prediction function
def predict_status(open, high, low, volume):
    input_data = np.asarray([open, high, low, volume])
    input_data = input_data.reshape(1,-1)
    prediction = model.predict(input_data)
    return prediction[0]

def main():

    # titling your page
    st.title("Reliance Stock Price Prediction App")

    #getting the input
    open = st.number_input("Enter the Open Value")
    high = st.number_input("Enter the High Value")
    low = st.number_input("Enter the Low Value")
    volume = st.number_input("Enter the Volume")

    #predict value
    diagnosis = ""

    if st.button("Predict"):
    
        diagnosis = predict_status(open, high, low, volume)
        if diagnosis:
            st.write("The Closing value is: ", f"__{diagnosis}__")

        else:
            st.error("Please Re-Enter the Values")
            
            
        st.write("Project by Akshay Narvate")
    
            
if __name__=="__main__":
    main()
