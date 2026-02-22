# 🏭 Manufacturing AI Pipeline: Anomaly Detection & Reporting

This project is a professional end-to-end solution designed for monitoring industrial generators. It combines **Deep Learning** for anomaly detection and **Generative AI** for automated technical maintenance reporting.

---

## 📊 Live System Dashboard
The system monitors real-time sensor streams (Temperature, Vibration, Pressure) and identifies critical failures using a **PyTorch Autoencoder**.

![Industrial Dashboard](assets/demo_preview.png)
*Figure 1: Real-time monitoring dashboard showing a captured anomaly with a high Loss Score (221.6644).*

---

## 🚀 How it Works
1.  **Data Generation:** Simulates factory environments by creating synthetic sensor data with added Gaussian noise to represent real-world interference.
2.  **Data Validation Layer:** The system applies **Z-Score** validation to ensure data integrity before deep learning analysis.
3.  **Deep Learning (Autoencoder):** The model learns the "normal" state of the machine. It calculates a **Reconstruction Loss**; a high score indicates a mechanical failure or technical anomaly.
4.  **AI Reporting:** GPT-4o-mini analyzes the specific abnormal sensor readings and generates an immediate technical diagnosis for field engineers.
5.  **Database Logging:** Every anomaly is stored in an **SQLite database** using **SQLAlchemy (ORM)** to ensure full traceability and history tracking.

---

## 🧠 AI Diagnostic & Traceability
When the system flags an anomaly, it provides actionable technical advice and logs the event permanently for engineering audits.

![AI Report and Database Notification](assets/demo_preview2.png)
*Figure 2: AI-generated diagnosis highlighting high temperature/vibration and the "Saved to Database" confirmation.*

### 🗄️ Database Logs (Traceability)
The system ensures that every failure event is recorded. Below are the historical logs stored in the SQLite database:

![SQLite Database Logs](assets/demo_preview_showdata.png)
*Figure 3: Historical logs showing timestamps, raw sensor values, loss scores, and full AI reports.*

---

## 📊 Performance Metrics
The system uses **Mean Squared Error (MSE)** to measure the deviation from normal operations.

$$Loss = \frac{1}{n} \sum_{i=1}^{n} (x_i - \hat{x}_i)^2$$

* **Normal State:** Loss < 0.5.
* **Anomalous State:** Loss > 100+ (In recent tests, we captured a score of **221.6644** during a simulated failure).

---

## 🛠️ Tech Stack
* **AI/ML:** PyTorch (Autoencoder), OpenAI API (GPT-4o-mini).
* **Backend:** FastAPI (Microservice ready), SQLAlchemy (ORM).
* **Database:** SQLite (Local storage for IoT environments).
* **Frontend:** Streamlit.

## 📂 Project Structure
* `src/model.py`: The Deep Learning brain (Autoencoder).
* `src/database.py`: Database models and SQLAlchemy connection.
* `src/api.py`: FastAPI endpoints for external data access.
* `src/reporter.py`: Generative AI logic for technical reporting.
* `main.py`: The primary Streamlit dashboard.