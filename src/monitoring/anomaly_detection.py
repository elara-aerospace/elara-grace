# -*- coding: utf-8 -*-

"""
anomaly_detection.py

Copyright (c) 2024 Suriyaa Sundararuban
Copyright (c) 2024 Elara Aerospace team
"""

class AnomalyDetector:
    def detect(self, sensor_data):
        anomalies = {}

        if sensor_data['temperature'] < -40 or sensor_data['temperature'] > 120:
            anomalies['temperature'] = sensor_data['temperature']

        if sensor_data['pressure'] < 5 or sensor_data['pressure'] > 150:
            anomalies['pressure'] = sensor_data['pressure']

        if sensor_data['altitude'] < 0 or sensor_data['altitude'] > 9000:
            anomalies['altitude'] = sensor_data['altitude']

        return anomalies
