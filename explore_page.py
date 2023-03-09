import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def shorten_categories(categories, cutoff):
    categoryMap = {}
    for i in range(len(categories)):
        if(categories.values[i] >= cutoff):
            categoryMap[categories.index[i]] = categories.index[i]
        else:
            categoryMap[categories.index[i]] = 'Other'
    return categoryMap

def convertExperienceToNum(x):
    if x == 'More than 50 years':
        return 50
    elif x == 'Less than 1 year':
        return 0.5
    return float(x)

def simplifyEducationLeve(x):
    if "Bachelor’s degree" in x:
        return "Bachelor’s degree"
    elif "Master’s degree" in x:
        return "Master’s degree"
    elif "Professional degree" in x or "Other doctoral degree" in x:
        return "Post grad"
    return "Less than a Bachelors"

@st.cache_data
def load_data():
    df = pd.read_csv("survey_results_public.csv")
    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedCompYearly"]]
    df = df.rename({"ConvertedCompYearly": "Salary"}, axis=1)
    df = df[df["Salary"].notnull()]
    df = df.dropna()
    df.isnull().sum()
    df = df[df["Employment"] == "Employed, full-time"]
    df = df.drop("Employment", axis=1)
    
    country_map = shorten_categories(df.Country.value_counts(), 400)
    df["Country"] = df["Country"].map(country_map)
    df = df[df["Salary"] <= 350000]
    df = df[df["Salary"] >= 10000]
    df = df[df["Country"] != 'Other']

    df["YearsCodePro"] = df["YearsCodePro"].apply(convertExperienceToNum)
    df["EdLevel"] = df["EdLevel"].apply(simplifyEducationLeve)
    
    return df

df = load_data()

def show_explore_page():
    st.title("Explore Software Engineer Salaries")
    st.write( """  #### Stack Overflow Developer Survey 2022 """)
    data = df["Country"].value_counts()

    ## Plot pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=False, startangle=90, textprops={'fontsize': 5, 'weight': 'bold'})
    ax1.axis("equal") # Equal ratio ensures that pie chart in circle

    st.write("""###### Number of Data collected from different countries """)
    st.pyplot(fig1)


    ## Plot bar graph
    st.write(""" ##### Mean Salary Based on Country""")
    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    ## Plot Line chart
    st.write( """ #### Mean Salary Based on Experience """)
    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending= True)
    st.line_chart(data)


