# 🚀 AI Student Performance Predictor

> An end-to-end Machine Learning web application that predicts student academic performance from study habits and academic indicators, with secure authentication, cloud database integration, analytics, and production deployment.

🌐 **Live Demo:**  
https://student-analytics-qv2d.onrender.com

🐙 **GitHub Repository:**  
https://github.com/sourabhchetan/student-analytics

---

## 📌 Overview

**AI Student Performance Predictor** is a full-stack Machine Learning application designed to help students understand and analyze their academic performance.

The application takes key student-related inputs such as:

- 📚 Study Hours
- 📅 Attendance Percentage
- 😴 Sleep Hours
- 📊 Previous Marks

and uses a trained Machine Learning model to estimate the student's expected marks.

Each prediction is stored in **MongoDB Atlas**, allowing users to review their previous predictions through an interactive analytics dashboard.

The project demonstrates an end-to-end workflow:

**Frontend → Flask API → Machine Learning Model → MongoDB Atlas → Analytics Dashboard**

---

# ✨ Current Features

### 🔐 Authentication

- User Signup
- User Login
- User Logout
- Session-based authentication
- Password hashing
- User-specific prediction history

### 🤖 Machine Learning

- Student performance prediction
- Scikit-learn based ML model
- Model trained using student performance data
- Automated prediction from multiple academic/behavioral features
- Saved trained model using Pickle

### 📊 Analytics Dashboard

- Prediction history
- Predicted marks visualization
- Study hours analysis
- Interactive charts
- User-specific analytics

### 👤 User Profile

- User profile page
- Authenticated user information
- Personalized application experience

### 🗄️ Database

- MongoDB Atlas integration
- Separate users collection
- Separate predictions collection
- User-specific prediction storage
- MongoDB indexes for username uniqueness

### ☁️ Production Deployment

- Deployed on Render
- Gunicorn WSGI server
- MongoDB Atlas cloud database
- Environment variable based configuration
- Production-ready Flask deployment structure

---

# 🧠 How It Works

```text
                  ┌─────────────────────┐
                  │       Student       │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │   Web Interface     │
                  │   HTML/CSS/JS       │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │   Flask Backend     │
                  │   Authentication    │
                  │   API Routes        │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │   ML Prediction     │
                  │   Scikit-learn      │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │   MongoDB Atlas     │
                  │ Users + Predictions│
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Analytics Dashboard │
                  │ Charts + History    │
                  └─────────────────────┘
