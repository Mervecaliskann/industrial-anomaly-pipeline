"""
[TR] Bu sınıf, endüstriyel sensörlerden gelen normal ve anomali verilerini istatistiksel olarak simüle eder.
[EN] This class statistically simulates normal and anomaly sensor data from industrial equipment.
"""
import numpy as np
import pandas as pd

class IndustrialDataGenerator:
    def __init__(self, n_samples=1000):
        self.n_samples = n_samples

    def generate_normal_data(self):
        """[TR] Normal çalışma koşullarını (75°C civarı) üretir.
           [EN] Generates normal operating conditions (around 75°C)."""
        np.random.seed(42)
        
        # [TR] Gerçekçi gürültü eklenmiş sensör verileri
        # [EN] Realistic sensor data with added Gaussian noise
        temp = 75 + np.random.normal(0, 2, self.n_samples)
        vibr = 2 + np.random.normal(0, 0.5, self.n_samples)
        press = 100 + np.random.normal(0, 5, self.n_samples)
        
        return pd.DataFrame({'temperature': temp, 'vibration': vibr, 'pressure': press})

    def inject_anomalies(self, df):
        """[TR] Verinin son kısmına yapay bir arıza (sıcaklık artışı) ekler.
           [EN] Injects an artificial fault (temperature spike) into the last part of the data."""
        # [TR] Son 50 örnekte sensör değerlerini anormal seviyeye çıkarıyoruz
        # [EN] Raising sensor values to abnormal levels in the last 50 samples
        df.loc[self.n_samples-50:, 'temperature'] += 20 
        df.loc[self.n_samples-50:, 'vibration'] += 3
        return df