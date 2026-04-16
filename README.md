# 🚀 AI Student Performance Predictor

> 🎯 A full-stack Machine Learning web app that predicts student performance based on study habits — with authentication, analytics, and live deployment.

---

## 🌐 Live Demo

👉 https://student-analytics-qv2d.onrender.com

---

## ✨ Features

✔️ User Signup & Login (Authentication System)
✔️ ML-based Prediction Engine
✔️ Interactive Analytics Dashboard (Charts)
✔️ Data stored in MongoDB Atlas (Cloud DB)
✔️ Fully deployed on cloud (Render)

---

## 🧠 How It Works

1. User logs into the system
2. Inputs:

   * Study Hours
   * Attendance
   * Sleep Hours
   * Previous Marks
3. ML model processes input
4. Predicts expected marks
5. Stores result in database
6. Dashboard visualizes trends

---

## 🛠️ Tech Stack

| Layer      | Technology            |
| ---------- | --------------------- |
| Frontend   | HTML, CSS, JavaScript |
| Backend    | Flask (Python)        |
| Database   | MongoDB Atlas         |
| ML Model   | Scikit-learn          |
| Deployment | Render                |

---

## 📊 Architecture

User → Flask Backend → ML Model → MongoDB Atlas → Dashboard UI

---

## 📸 Screenshots

### 🔐 Login Page


<img width="1876" height="885" alt="login" src="https://github.com/user-attachments/assets/ba9712f8-858e-4b53-9a34-720c9342bb18" />


### 🎯 Prediction Page


<img width="1849" height="864" alt="Prediction" src="https://github.com/user-attachments/assets/aba82b69-fb9f-41aa-8773-3738247e2076" />


### 📊 Dashboard


<img width="1854" height="883" alt="dashboard" src="https://github.com/user-attachments/assets/44268496-a792-42ea-8d4a-36b89a8fd249" />


---

## ⚙️ Run Locally

```bash
git clone https://github.com/sourabhchetan/student-analytics.git
cd student-analytics
pip install -r requirements.txt

# Windows
set MONGO_URI=your_connection_string

# Mac/Linux
export MONGO_URI=your_connection_string

python run.py
```

---

## 🔐 Environment Variables

| Variable   | Description                     |
| ---------- | ------------------------------- |
| MONGO_URI  | MongoDB Atlas connection string |
| SECRET_KEY | Flask session secret            |

---

## 📈 Future Enhancements

* 📊 Advanced filters in dashboard
* 📱 Mobile responsive UI
* 🤖 Better ML model accuracy
* 👨‍💼 Admin panel
* 📡 REST API support

---

## 🧪 Project Highlights

* End-to-end ML integration
* Real-time data storage
* Secure authentication system
* Production deployment

---

## 👨‍💻 Author

**Sourabh Chetan**
🎓 MCA Student
💻 Full Stack Developer | ML Enthusiast

---

## ⭐ Support

If you like this project:
👉 Give it a ⭐ on GitHub
👉 Share with others

---

## 🧾 License

This project is open-source and free to use.
