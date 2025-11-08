import streamlit as st 
import numpy as np
import pickle
import pandas as pd 

with open("C:/Users/Top10/Desktop/Quiz/model.pkl","rb") as f:
    model = pickle.load(f)
st.title("airline passenger satisfaction prediction")
st.header("entre passenger details")
Gender = st.selectbox("Gender",["Male","Female"])
Customer_type = st.selectbox("customer type",["loyal customer","disloyal customer"])
Type_of_travel = st.selectbox("Type of travel",["personal travel","business travel"])
Class = st.selectbox("Class",["Eco","Eco plus","Business"])
Age = st.slider("Age",10,90,25)
Flight_distance = st.number_input("Flight distance",0,5000,1000)
Inflight_wifi_service = st.slider("Inflight wifi service",0,5,3)
Online_boarding = st.slider("Online boarding",0,5,3)
Seat_comfort = st.slider("Seat comfort", 0, 5, 3)
Inflight_entertainment = st.slider("Inflight entertainment", 0, 5, 3)
Ease_of_online_booking = st.slider("Ease of online booking", 0, 5, 3)
Cleanliness = st.slider("Cleanliness", 0, 5, 3)
Leg_room_service = st.slider("Leg room service", 0, 5, 3)

def encode_inputs(Gender, Customer_Type, Type_of_Travel, Class):
    gender = 1 if Gender == "Male" else 0            
    customer = 0 if Customer_Type == "Loyal Customer" else 1
    travel = 0 if Type_of_Travel == "Business Travel" else 1
    if Class == "Eco":
        cls = 0
    elif Class == "Eco Plus":
        cls = -1
    else: 
        cls = 1
    return gender, customer, travel, cls

gender, customer, travel, cls = encode_inputs(Gender, Customer_type, Type_of_travel, Class)

input_data = np.array([[
    Inflight_wifi_service,
    Online_boarding,
    cls,                       
    travel,                    
    Seat_comfort,
    Inflight_entertainment,
    Ease_of_online_booking,
    customer,                  
    Age,
    Cleanliness,
    Leg_room_service,
    Flight_distance
]], dtype=float)


if st.button("Predict Satisfaction"):
   
        pred = model.predict(input_data)
        if pred[0] == 1:
            st.success("✅ Passenger is Satisfied")
        else:
            st.info("ℹ️ Passenger is Neutral or Dissatisfied")
        



