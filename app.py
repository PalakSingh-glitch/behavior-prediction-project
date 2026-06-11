import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

st.title("User Behavior Prediction App 🚀")

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

model = LogisticRegression()
model.fit(X, y)

# user input
time_spent = st.number_input("Time Spent")
clicks = st.number_input("Clicks")
scroll = st.number_input("Scroll Depth")

if st.button("Predict"):
    result = model.predict([[time_spent, clicks, scroll]])

    if result[0] == 1:
        st.success("User is likely to PURCHASE ✅")
    else:
        st.error("User is NOT likely to purchase ❌")