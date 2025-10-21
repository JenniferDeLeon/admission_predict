# Import necessary libraries
import streamlit as st
import pickle
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

password_guess = st.text_input("What is the Password?")

if password_guess != st.secrets["jd-password"]:
    st.stop()

# --- Page Setup ---
st.write("This app predicts the probability of admission to graduate school")
st.title("Graduate Admission Predictor")

# --- Load Pre-trained MAPIE Model ---
with open("reg_admission.pickle", "rb") as f:
    mapie = pickle.load(f)

# --- Sidebar Inputs ---
st.sidebar.header("Input Admission Features")

gre_score = st.sidebar.number_input("GRE Score", value=320)
toefl_score = st.sidebar.number_input("TOEFL Score", value=100)
university_rating = st.sidebar.slider("University Rating", min_value=1, max_value=5)
sop = st.sidebar.slider("Statement of Purpose (SOP)", min_value=1, max_value=5)
lor = st.sidebar.slider("Letter of Recommendation (LOR)", min_value=1, max_value=5)
cgpa = st.sidebar.number_input("CGPA", value=8.00)
research = st.sidebar.selectbox("Research Experience", options=["Yes", "No"])

# --- Encode Research as One-Hot ---
research_yes = 1 if research == "Yes" else 0
research_no = 1 if research == "No" else 0

# --- Prediction Button ---
if st.sidebar.button("Predict Admission Chance"):

    # Prepare features in the correct order
    features = [
        gre_score,
        toefl_score,
        university_rating,
        sop,
        lor,
        cgpa,
        research_no,
        research_yes
    ]

    # Predict with MAPIE using 90% prediction interval
    y_pred, y_pis = mapie.predict([features], alpha=0.10)  # 90% prediction interval

    prediction = y_pred[0, 0]
    lower_bound = y_pis[0, 0, 0]
    upper_bound = y_pis[0, 0, 1]

    # --- Display Prediction ---
    st.subheader("Predicted Admission Chance")
    st.success(f"Predicted Admission Probability: {prediction:.2f}")

    st.subheader("Prediction Interval (90%)")
    st.info(f"Admission probability is likely between {lower_bound:.2f} and {upper_bound:.2f}")

# --- Model Insights Tabs ---
st.subheader("Model Insights")
tab1, tab2, tab3, tab4 = st.tabs(["Feature Importance", "Residuals Histogram", "Predicted vs Actual", "Coverage Plot"])

# Tab 1: Feature Importance 
with tab1:
    st.write("Feature Importance")
    st.image('feature_imp.svg')
    st.caption("Features used in this prediction are ranked by relative importance.")

# Tab 2: Histogram of Residuals
with tab2:
    st.write("Histogram of Residuals")
    st.image('all_residuals.svg')
    st.caption("Histogram of residuals from the model predictions.")

# Tab 3: Predicted vs Actual
with tab3:
    st.write("Predicted vs Actual")
    st.image('predicted_vs_actual.svg')
    st.caption("Comparison of predicted vs actual values.")

# Tab 4: Coverage Plot
with tab4:
    st.write("Coverage Plot")
    st.image('coverage_plot.svg')
    st.caption("Coverage plot of model predictions.")