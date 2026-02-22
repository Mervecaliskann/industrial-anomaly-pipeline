# 🏭 Manufacturing AI Pipeline: Anomaly Detection & Reporting

This project is an end-to-end solution for monitoring industrial generators. It finds mechanical problems using Deep Learning and writes technical reports using AI.

## 🚀 How it Works
1. **Data Generation:** The system creates synthetic sensor data (Temperature, Vibration, Pressure).
2. **Deep Learning:** A **PyTorch Autoencoder** monitors the data. It calculates a "Loss Score" to find anomalies.
3. **Database Logging:** Every detected anomaly is saved to an **SQLite database** using **SQLAlchemy**.
4. **AI Reporting:** GPT-4o-mini analyzes the numbers and writes a maintenance guide for engineers.

---

## 📊 Performance & Insights
When the system finds a problem (like high vibration), it flags it immediately.

**Key Metric (Reconstruction Loss):**
$$Loss = \frac{1}{n} \sum_{i=1}^{n} (x_i - \hat{x}_i)^2$$

* **Low Loss:** Machine is working normally.
* **High Loss:** Potential failure detected (e.g., 115.14 loss score).

---

## 🛠️ Tech Stack
- **AI/ML:** PyTorch (Autoencoder), OpenAI API
- **Backend:** FastAPI, SQLAlchemy (ORM)
- **Database:** SQLite
- **Frontend:** Streamlit

## 📂 Project Structure
- `src/model.py`: The brain of the system (Autoencoder).
- `src/database.py`: SQL table definitions for logging.
- `src/api.py`: FastAPI endpoints to access data.
- `main.py`: The main dashboard application.