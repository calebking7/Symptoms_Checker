import streamlit as st
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv('symptoms_dataset.csv')

# Prepare features and target
X = df.drop('TYPE', axis=1)
y = df['TYPE']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Streamlit app
st.set_page_config(page_title="Symptom Checker", page_icon="🩺")

st.title("🩺 Basic Symptom Checker")
st.markdown("### Check your symptoms to get a quick diagnosis!")

# Add a sidebar
st.sidebar.header("Select Your Symptoms")

# Create checkboxes for each symptom
symptoms = X.columns
user_input = []

for symptom in symptoms:
    user_input.append(st.sidebar.checkbox(symptom.replace("_", " ").title()))

# Convert user input to numpy array
user_input = np.array(user_input).reshape(1, -1)

# Predict the condition
if st.button("Predict"):
    if not user_input.any():
        st.error("Please select at least one symptom to get a prediction.")
    else:
        prediction = model.predict(user_input)
        st.markdown(f"## Predicted Condition: **{prediction[0]}**")

st.text("")
st.markdown("""---""")
st.markdown("### Usage")
st.write("""
1. Select your symptoms from the sidebar.
2. Click the "Predict" button to receive a potential diagnosis.
3. Ensure at least one symptom is selected to avoid errors.""")
st.markdown("""---""")
st.markdown("### Introduction")
st.write("""
This Streamlit application is a basic web-based tool designed to quickly predict minor illnesses based on user-selected symptoms. 
By using a Decision Tree Classifier, it analyzes the symptoms you select and provides a potential diagnosis. 
This can be particularly useful for individuals seeking initial insights into their health concerns. However, this is just a ***small demo***
how to implement Machine Learning into evaluating the results of healthcare system, which could deliver real valuable information in the future.

### About the Dataset
The model is trained on a dataset of various symptoms and their corresponding conditions, allowing it to make informed predictions based on the input provided. 
You can also find out the dataset in the code repository below.

### Portfolio
For more projects and insights, please visit my [portfolio](https://kimnguyen2002.github.io/Portfolio/).

### Code Repository
You can find the complete code for this application in my GitHub repository [here](https://github.com/kimnguyen2002/Symptoms_Checker).
""")

# Add some style
st.markdown(
    """
    <style>
    .reportview-container {
        background: #f0f2f6;
    }
    .sidebar .sidebar-content {
        background: #dfe6f0;
    }
    </style>
    """,
    unsafe_allow_html=True
)
