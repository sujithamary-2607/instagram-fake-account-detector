# Instagram Fake Account Detector

This is a Flask-based web application that uses a Machine Learning model to predict whether an Instagram account is real or fake based on profile data.

## 📌 Project Objective

The goal of this project is to identify potentially fake Instagram accounts by analyzing profile features such as follower count, following count, post count, etc., using a trained ML model.

## ⚙️ Technologies Used

- **Frontend**: HTML, CSS (Jinja templates via Flask)
- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn
- **Model**: Trained using Logistic Regression / Random Forest
- **API**: RapidAPI (for fetching Instagram profile data)

## 📁 Project Structure

```
instagram-fake-account-detector/
│
├── app.py                # Main Flask backend
├── model.pkl             # Trained ML model file
├── templates/            # HTML pages
│   ├── index.html        # Input form
│   └── result.html       # Prediction result
├── static/               # Optional: CSS or image files
├── requirements.txt      # Python libraries needed
└── README.md             # Project overview
```

## 🚀 How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/instagram-fake-account-detector.git
   cd instagram-fake-account-detector
   ```

2. **Install the Requirements**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App**
   ```bash
   python app.py
   ```

4. **Visit in Browser**
   - Open: `http://127.0.0.1:5000`

## 🧠 Machine Learning Model

- Input Features:
  - Follower count
  - Following count
  - Number of posts
  - Biography length
  - Profile picture availability
- Output:
  - Prediction: Real or Fake Account

## 🎯 Future Scope

- Improve model with deep learning
- Add profile image analysis using CV
- Expand to other social media platforms

## 👩‍💻 Developed By

**T. Sujitha Mary**  
B.Tech Artificial Intelligence and Data Science  
St. Joseph College of Engineering  
