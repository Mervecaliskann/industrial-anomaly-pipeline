import streamlit as st
import pandas as pd
import torch
import torch.optim as optim
import torch.nn as nn
from src.generator import IndustrialDataGenerator
from src.model import AnomalyDetector
from src.reporter import MaintenanceReporter

st.set_page_config(page_title="Industrial Anomaly Lab", layout="wide")
st.title("🏭 Industrial Anomaly Detection & AI Reporting")

# 1. Veri Hazırlığı
gen = IndustrialDataGenerator()
normal_data = gen.generate_normal_data()
test_data = gen.inject_anomalies(normal_data.copy())

st.subheader("📊 Real-time Sensor Streams")
st.line_chart(test_data)

# 2. Model Eğitimi ve Analiz
if st.button("🚀 Run AI Analysis"):
    # Veriyi tensor formatına çeviriyoruz
    train_tensor = torch.FloatTensor(normal_data.values)
    test_tensor = torch.FloatTensor(test_data.values)
    
    model = AnomalyDetector(input_dim=3)
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    criterion = nn.MSELoss()
    
    # [TR] Modeli hızlıca normal veri üzerinde eğitiyoruz (Training)
    # [EN] Training the model quickly on normal data
    with st.spinner("Model is learning normal patterns..."):
        for epoch in range(50):
            preds = model(train_tensor)
            loss = criterion(preds, train_tensor)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
    
    # [TR] Test verisi üzerinde tahmin yapıp hata (loss) hesaplıyoruz
    # [EN] Predicting on test data and calculating reconstruction loss
    reconstructed = model(test_tensor)
    losses = torch.mean((reconstructed - test_tensor)**2, dim=1).detach().numpy()
    
    # Son örnekteki hataya bakıyoruz
    current_loss = losses[-1]
    
    if current_loss > 0.5: # Eşik değer
        st.error(f"🚨 ANOMALY DETECTED! (Loss Score: {current_loss:.4f})")
    
        reporter = MaintenanceReporter()
        last_values = test_data.iloc[-1]
        report = reporter.generate_report(last_values)
        st.info("🤖 AI Diagnostic Report:")
        st.write(report)

        # [EN] NEW: Save the result to the SQLite database via FastAPI logic
        # [TR] YENİ: Sonucu FastAPI mantığı üzerinden SQLite veritabanına kaydet
        from src.database import SessionLocal, AnomalyLog
        
        db = SessionLocal()
        new_log = AnomalyLog(
            temperature=float(last_values['temperature']),
            vibration=float(last_values['vibration']),
            pressure=float(last_values['pressure']),
            loss_score=float(current_loss),
            ai_report=report
        )
        db.add(new_log)
        db.commit()
        db.close()
        st.success("💾 Anomaly saved to database!")