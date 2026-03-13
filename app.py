import os
import streamlit as st
import pandas as pd
import joblib

# ==============================
# Load model and scaler
# ==============================
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# ==============================
# Theme selection
# ==============================
theme = st.selectbox(
    "Select Theme", ["Dark", "Dark Blue", "Red", "Light"], index=0
)

# Apply theme styles
if theme == "Dark":
    st.markdown("""
        <style>
        .stApp { background-color: #0e1117; color: #ffffff; }
        .stSlider>div>div>div { color: #ffffff; }
        .stButton>button { background-color: #4CAF50; color: #ffffff; }
        </style>
        """, unsafe_allow_html=True)

elif theme == "Dark Blue":
    st.markdown("""
        <style>
        .stApp { background-color: #0b1d3a; color: #ffffff; }
        .stSlider>div>div>div { color: #ffffff; }
        .stButton>button { background-color: #1f4fbf; color: #ffffff; }
        </style>
        """, unsafe_allow_html=True)

elif theme == "Red":
    st.markdown("""
        <style>
        .stApp { background-color: #2b0000; color: #ffffff; }
        .stSlider>div>div>div { color: #ffffff; }
        .stButton>button { background-color: #cc0000; color: #ffffff; }
        </style>
        """, unsafe_allow_html=True)

else:  
    st.markdown("""
        <style>
        .stApp { background-color: #e6f0ff; color: #000033; }
        .stTextInput>div>div>input { background-color: #ffffff; color: #000033; }
        .stSlider>div>div>div { color: #000033; }
        .stButton>button { background-color: #0052cc; color: #ffffff; }
        </style>
        """, unsafe_allow_html=True)

# ==============================
# Title
# ==============================
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>🎓 Campus Placement Prediction</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>Fill student details and click Predict</p>",
    unsafe_allow_html=True
)

st.write("---")

# ==============================
# Input Fields
# ==============================
col1, col2 = st.columns(2)

with col1:
    cgpa = st.slider("CGPA", 5.0, 10.0, 7.0)
    internships = st.slider("Internships", 0, 5, 1)
    projects = st.slider("Projects", 0, 6, 2)
    workshops = st.slider("Workshops", 0, 5, 1)

with col2:
    aptitude = st.slider("Aptitude Score", 40, 100, 60)
    softskills = st.slider("Soft Skills (1-10)", 1, 10, 6)
    training = st.selectbox("Placement Training", ["No", "Yes"])

training_encoded = 1 if training == "Yes" else 0

# ==============================
# Prediction
# ==============================
if st.button("🔮 Predict Placement", use_container_width=True):

    input_data = pd.DataFrame(
        [[cgpa, internships, projects, workshops,
          aptitude, softskills, training_encoded]],
        columns=[
            "CGPA",
            "Internships",
            "Projects",
            "Workshops",
            "AptitudeScore",
            "SoftSkills",
            "PlacementTraining"
        ]
    )

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)

    # Probability
    prob = model.predict_proba(input_scaled)[0]
    probability = prob[1]

    # Result
    if prediction[0] == 1:
        st.success("🎉 Placement Status: Placed")
    else:
        st.error("❌ Placement Status: Not Placed")

    # ==============================
    # Probability Visualization
    # ==============================
    st.subheader("📊 Placement Probability")

    st.progress(int(probability * 100))

    st.metric(
        label="Placement Chance",
        value=f"{round(probability*100,2)}%"
    )

    # Chart
    chart_df = pd.DataFrame({
        "Category": ["Not Placed", "Placed"],
        "Probability": prob
    })

    st.bar_chart(chart_df.set_index("Category"))

    # Confidence display
    st.subheader("🎯 Placement Confidence")
    st.write(f"### {round(probability*100,2)}% chance of getting placed")