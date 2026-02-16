"""
[TR] Tespit edilen sayısal anomalileri teknik bir bakım raporuna dönüştürür.
[EN] Converts detected numerical anomalies into a technical maintenance report.
"""
import os
from openai import OpenAI
from dotenv import load_dotenv

class MaintenanceReporter:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate_report(self, sensor_values):
        # [TR] LLM'e endüstriyel bir uzman rolü veriyoruz
        # [EN] Giving the LLM an industrial expert persona
        prompt = f"""
        You are a Senior Systems Engineer. An anomaly has been detected in a Generator Set:
        - Temperature: {sensor_values['temperature']:.2f} C
        - Vibration: {sensor_values['vibration']:.2f} mm/s
        - Pressure: {sensor_values['pressure']:.2f} psi

        Task: Provide a professional diagnosis. Explain why these readings are abnormal 
        and suggest 3 immediate technical actions.
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content