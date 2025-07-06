from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np

# Dummy data [followers, following, posts, verified, private, name_len, bio_len]
X = np.array([
    [100, 150, 25, 0, 1, 10, 50],  # real
    [50, 2000, 1, 0, 1, 3, 5],      # fake
    [12000, 300, 60, 1, 0, 15, 100],
    [10, 5000, 1, 0, 1, 2, 2]
])
y = [0, 1, 0, 1]  # 0 = real, 1 = fake

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, 'model/fake_account_model.pkl')
print("✅ Model trained and saved.")
