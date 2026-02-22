from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, AnomalyLog

app = FastAPI(title="Industrial AI API")

# [EN] Database connection dependency
# [TR] Veritabanı bağlantı bağımlılığı
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/logs")
def get_logs(db: Session = Depends(get_db)):
    """
    [EN] Returns all recorded anomalies from the database.
    [TR] Veritabanındaki tüm anomali kayıtlarını döndürür.
    """
    return db.query(AnomalyLog).all()

@app.post("/log_anomaly")
def log_anomaly(temp: float, vibr: float, press: float, loss: float, report: str, db: Session = Depends(get_db)):
    """
    [EN] Saves a new anomaly entry to the database.
    [TR] Yeni bir anomali kaydını veritabanına kaydeder.
    """
    new_log = AnomalyLog(temperature=temp, vibration=vibr, pressure=press, loss_score=loss, ai_report=report)
    db.add(new_log)
    db.commit()
    return {"message": "Anomaly logged successfully!"}