import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
import joblib
from utils.feature_extractor import extract_features

# Load dataset
df = pd.read_csv('malicious_phish.csv')  # Place this CSV in the root folder
df['label'] = df['type'].apply(lambda x: 1 if x != 'benign' else 0)

# Feature extraction
features = df['url'].apply(extract_features).apply(pd.Series)
X = features
y = df['label']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'model/xgb_model.pkl')
print("✅ Model saved to model/xgb_model.pkl")
