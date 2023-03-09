import streamlit as st
import pickle
import numpy as np

def load_model():
    with open("saved_steps.pk1" ,"rb") as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
labelEncode_country = data["labelEncode_country"]
labelEncode_education = data["labelEncode_education"]

def show_predict_page():
    st.title("Software Engineer Salary Prediction")
    st.write("""#### Below information is required to predict the salary""")
    countries = (
        "United States of America",                               
        "Germany" ,                                               
        "United Kingdom of Great Britain and Northern Ireland" ,   
        "India" ,                                                  
        "Canada" ,                                                 
        "France" ,                                                 
        "Brazil" ,                                                 
        "Spain"  ,                                                 
        "Netherlands" ,                                            
        "Australia" ,                                              
        "Italy" ,                                                  
        "Poland" ,                                                 
        "Sweden" ,                                                
        "Russian Federation" ,                                     
        "Switzerland"
    )

    education = (
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
        "Less than a Bachelors"
    )

    country = st.selectbox("Country" , countries)
    educationLevel = st.selectbox("Education Level", education)

    experience = st.slider("Years of Experience", 0, 50, 3)

    response = st.button("Calculate Salary")
    if response:
        x = np.array([[country, educationLevel, experience]])
        x[:,0] = labelEncode_country.transform(x[:,0])
        x[:,1] = labelEncode_education.transform(x[:,1])
        x = x.astype(float)
    
        salary = regressor.predict(x)
        st.subheader(f" The estimated salary is ${salary[0]:.2f}")