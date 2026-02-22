from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# [EN] Database file path - SQLite creates a local file
# [TR] Veritabanı dosya yolu - SQLite yerel bir dosya oluşturur
SQLALCHEMY_DATABASE_URL = "sqlite:///./sensor_logs.db"

# [EN] Use 'create_engine' to connect to the database
# [TR] Veritabanına bağlanmak için 'create_engine' kullanıyoruz
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class AnomalyLog(Base):
    """
    [EN] Table model for storing sensor anomalies and AI reports.
    [TR] Sensör anomalilerini ve AI raporlarını saklamak için tablo modeli.
    """
    __tablename__ = "anomaly_logs"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    temperature = Column(Float)
    vibration = Column(Float)
    pressure = Column(Float)
    loss_score = Column(Float)
    ai_report = Column(String)

# [EN] Create the tables defined above
# [TR] Yukarıda tanımlanan tabloları oluştur
Base.metadata.create_all(bind=engine)