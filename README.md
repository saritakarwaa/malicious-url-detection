Malicious URL Detection

This project uses Machine Learning to detect whether a given URL is benign, phishing, malware, or defacement. It provides a user-friendly interface built with Streamlit to test URLs and visualize predictions in real-time.

Features
- Detects malicious URLs using lexical, host-based, and content-based features
- Trained using LightGBM (LGBMClassifier) for fast and accurate predictions
- Integrated frontend using Streamlit for ease of testing and deployment
- Supports classification into:
  - 🟢 Safe
  - 🔴 Phishing
  - 🟠 Malware
  - 🟣 Defacement


Tech Stack
Machine Learning & Model Training
- Python
- Pandas, NumPy
- Scikit-learn
- LightGBM
- XGBoost, Random Forest, SVM (for comparison)
- Matplotlib, Seaborn (for evaluation & plotting)

Feature Engineering
- Lexical features (URL length, number of dots, special characters)
- Host-based features (domain age, IP presence)
- Content-based features (redirections, JavaScript, iFrames)
- Blacklist cross-checking

Web Frontend
- Streamlit(for interactive URL checking)
- JSON for result communication

Others
- VS Code (for development)
- Git & GitHub (for version control)
- `malicious_phish.csv` dataset (not uploaded to GitHub for security reasons)



Installation

### Clone the repository
git clone https://github.com/saritakarwaa/malicious-url-detection.git
cd malicious-url-detection

Install required libraries : pip install -r requirements.txt
Running the Streamlit App : streamlit run app.py
