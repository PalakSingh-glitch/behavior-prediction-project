import streamlit as st
import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
st.set_page_config(page_title="Behavior Predictor", page_icon="🚀", layout="centered")

st.markdown("""
            <style>
            .main {
                background-color: #0e1117;
                color: white;
            }
            </style>
        """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #00ffcc;'>🚀 User Behavior Prediction</h1>", unsafe_allow_html=True)
# load data
data = pd.read_csv("data/user_data.csv")
st.subheader("User Behavior Visualization")

fig, ax = plt.subplots()

ax.scatter(data["time_spent"], data["clicks"])

ax.set_xlabel("Time Spent")
ax.set_ylabel("Clicks")
ax.set_title("Time vs Clicks")

st.pyplot(fig)

X = data[["time_spent", "clicks", "scroll_depth"]]
y = data["purchase"]

model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)
y_pred = model.predict(X)
accuracy = accuracy_score(y, y_pred)

st.subheader("📊 Model Performance")
st.write(f"Accuracy: {accuracy * 100:.2f}%")

st.title("User Behavior Prediction")

st.subheader("Enter User Details")
# user input
time_spent = st.slider("Time Spent", 0, 100, 10)
clicks = st.slider("Clicks", 0, 100, 10)
scroll_depth = st.slider("Scroll Depth", 0, 100, 10)

if st.button("Predict"):
    input_data = [[time_spent, clicks, scroll_depth]]
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        result = "PURCHASE"
        st.success("User is likely to PURCHASE 🛒")
    else:
        result = "NOT PURCHASE"
        st.error("User is NOT likely to purchase ❌")

    # 👇 NEW PART (DATA SAVE)
    new_data = pd.DataFrame({
        "Time_Spent": [time_spent],
        "Clicks": [clicks],
        "Scroll_Depth": [scroll_depth],
        "Prediction": [result]
    })

    file_path = "user_data.csv"

    if os.path.exists(file_path):
        new_data.to_csv(file_path, mode='a', header=False, index=False)
    else:
        new_data.to_csv(file_path, index=False)
    if os.path.exists("user_data.csv"):
        with open("user_data.csv", "rb") as file:
           st.download_button(
               label="📥 Download Data",
               data=file,
               file_name="user_data.csv",
               mime="text/csv"
        )
    result = model.predict([[time_spent, clicks, scroll_depth]])

    if result[0] == 1:
        st.success("User is likely to PURCHASE ✅")
    else:
        st.error("User is NOT likely to purchase ❌")