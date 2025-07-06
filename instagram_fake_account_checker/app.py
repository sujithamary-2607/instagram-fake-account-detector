from flask import Flask, render_template, request
import requests
import joblib

app = Flask(__name__)

# ✅ Load trained ML model
model = joblib.load('model/fake_account_model.pkl')

# ✅ Instagram API configuration
API_URL = "https://instagram-premium-api-2023.p.rapidapi.com/v1/user/by/username"
HEADERS = {
    "x-rapidapi-host": "instagram-premium-api-2023.p.rapidapi.com",
    "x-rapidapi-key": "15a6d3deb3msh22eadc3669e394ep18e4d6jsnefaf0f5ff847"
}

# ✅ Convert Instagram data to ML features
def extract_features(data):
    return [
        int(data.get("follower_count", 0)),
        int(data.get("following_count", 0)),
        int(data.get("media_count", 0)),
        int(data.get("is_verified", False)),
        int(data.get("is_private", False)),
        len(data.get("full_name", "")),
        len(data.get("biography", ""))
    ]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/fetch', methods=['POST'])
def fetch():
    username = request.form['username']
    response = requests.get(f"{API_URL}?username={username}", headers=HEADERS)

    try:
        data = response.json()
        profile = data.get("profile", data)

        if "username" not in profile:
            return render_template("index.html", error="❌ Invalid username or no profile data found.")

        # Extract features for prediction
        features = extract_features(profile)
        prediction = model.predict([features])[0]
        status = "Fake" if prediction == 1 else "Real"

        return render_template("index.html", profile=profile, prediction=status)

    except Exception as e:
        return render_template("index.html", error=f"❌ Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
