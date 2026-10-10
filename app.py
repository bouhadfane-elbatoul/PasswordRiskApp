import streamlit as st
import numpy as np
import math
import re

# Load model
w = np.load("weights.npy")

# Charset detection
def detect_charset(password):
    charset = 0
    if re.search(r"[a-z]", password): charset += 26
    if re.search(r"[A-Z]", password): charset += 26
    if re.search(r"[0-9]", password): charset += 10
    if re.search(r"[^a-zA-Z0-9]", password): charset += 32
    return charset

# Predict time
def predict_time(password):
    length = len(password)
    charset = detect_charset(password)
    if charset == 0: return 0
    entropy = length * math.log2(charset)
    X_input = np.array([1, length, charset, entropy]).reshape(1,-1)
    log_time = X_input @ w
    return np.exp(log_time[0][0])

# Readable format
def readable_time(seconds):
    if seconds < 60: return f"{seconds:.2f} seconds"
    elif seconds < 3600: return f"{seconds/60:.2f} minutes"
    elif seconds < 86400: return f"{seconds/3600:.2f} hours"
    elif seconds < 31536000: return f"{seconds/86400:.2f} days"
    else: return f"{seconds/31536000:.2f} years"

# Risk category
def risk_category(seconds):
    if seconds < 3600: return "🔴 Critical"
    elif seconds < 86400: return "🟠 High"
    elif seconds < 31536000: return "🟡 Moderate"
    else: return "🟢 Strong"

# Streamlit UI
st.title("🔐 Digital Bank Password Risk Predictor")
password = st.text_input("Enter Password", type="password")
if password:
    seconds = predict_time(password)
    st.subheader("Estimated Crack Time")
    st.success(readable_time(seconds))
    st.subheader("Security Level")
    st.write(risk_category(seconds))