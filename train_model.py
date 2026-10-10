import numpy as np
import pandas as pd
import math
import random

# Generate synthetic dataset
def compute_entropy(length, charset):
    return length * math.log2(charset)

def generate_dataset(samples=2000):
    data = []
    guesses_per_second = 1e9
    for _ in range(samples):
        length = random.randint(6,20)
        charset = random.choice([26,36,52,62,94])
        entropy = compute_entropy(length, charset)
        time_seconds = (2**entropy)/guesses_per_second
        log_time = np.log(time_seconds)
        data.append([length, charset, entropy, log_time])
    return pd.DataFrame(data, columns=["length","charset","entropy","log_time"])

df = generate_dataset()
X = df[["length","charset","entropy"]].values
y = df["log_time"].values.reshape(-1,1)

# Add bias
X = np.hstack((np.ones((X.shape[0],1)), X))

# Linear regression: normal equation
w = np.linalg.inv(X.T @ X) @ X.T @ y

# Save model
np.save("weights.npy", w)
print("Model trained and saved!")