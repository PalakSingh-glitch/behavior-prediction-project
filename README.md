Overview
This project is a Machine Learning-powered web application that predicts whether a user is likely to make a purchase based on their interaction behavior.
It analyzes key user metrics such as:
 Time Spent on platform
 Number of Clicks
 Scroll Depth
The app uses an advanced Random Forest Classifier to provide accurate predictions and visualize user behavior.
Machine Learning Model
Model Used: Random Forest Classifier 🌳
Type: Supervised Learning (Classification)
Output:
 Likely to Purchase
 Not Likely to Purchase
 Tech Stack
Python 
Streamlit 
Pandas 
Scikit-learn 
Matplotlib 
Features
 Real-time Prediction
 Data Visualization (Scatter Plot)
 User Data Storage (CSV Logging)
 Download User Data
 Model Accuracy Display
 Feature Importance Analysis
 Modern UI (Dark Theme + Sliders + Layout)
 Live Application
 https://behavior-prediction-project-j9rkvd6qoxknc5guyvkgp6.streamlit.app/
 App Preview
Add your screenshot here
�
 How to Run Locally
Bash
git clone https://github.com/your-username/behavior-prediction-project.git
cd behavior-prediction-project
pip install -r requirements.txt
streamlit run app.py
 Project Structure

behavior-prediction-project/
│
├── data/
├── app.py
├── main.py
├── user_data.csv
├── requirements.txt
├── README.md
└── .gitignore
Model Performance
Accuracy: ~95–100% (depending on dataset)
Feature Importance used to analyze key influencing factors Future Improvements
Add more advanced models (XGBoost, Neural Networks)
Improve dataset size and quality
Add dashboard analytics
Deploy with custom domain
 Author
Palak Singh
