import pandas as pd
from sklearn.linear_model import LogisticRegression

print("ML project start 🚀")

data = pd.read_csv("data/user_data.csv")

X = data[["time_spent", "clicks", "scroll_depth"]]
y = data["purchase"]

model = LogisticRegression()
model.fit(X, y)

user_input = input("Enter values (time clicks scroll): ")
time_spent, clicks, scroll = map(int, user_input.split())

result = model.predict([[time_spent, clicks, scroll]])

if result[0] == 1:
    print("User is likely to PURCHASE ✅")
else:
    print("User is NOT likely to purchase ❌")