🎓 Campus Placement Prediction
A Machine Learning web application that predicts whether a student will get placed based on academic performance, internships, projects, aptitude score, and soft skills.

The project uses a Random Forest Classifier and is deployed as an interactive Streamlit web application.

📌 Features
Predicts placement status (Placed / Not Placed)
Shows placement probability
Interactive Streamlit UI
Multiple theme options
Visualization of placement probability
Real-time predictions
🧠 Machine Learning Model
Algorithm used:

Random Forest Classifier
Libraries used:

Scikit-learn
Pandas
NumPy
Joblib
Model workflow:

Data preprocessing
Train-Test split
Model training
Model evaluation
Model serialization using joblib
📊 Input Features
The model predicts placement based on the following features:

Feature	Description
CGPA	Student CGPA
Internships	Number of internships
Projects	Number of academic/industry projects
Workshops	Number of workshops attended
AptitudeScore	Aptitude test score
SoftSkills	Soft skills rating (1–10)
PlacementTraining	Whether student took placement training
🖥️ Application Interface
The Streamlit app allows users to:

Enter academic details
Select placement training status
Predict placement result instantly
View probability and visualization
📈 Model Evaluation
Metrics used:

Accuracy Score
Confusion Matrix
Classification Report
The model predicts placement with high accuracy based on academic performance and training features.

🌐 Deployment
This project can be deployed using:

Streamlit Cloud
🛠️ Technologies Used
Python
Streamlit
Scikit-learn
Pandas
NumPy
Joblib
Git
GitHub
