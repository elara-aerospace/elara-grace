# -*- coding: utf-8 -*-

"""
anomaly_detection.py

Copyright (c) 2024 Suriyaa Sundararuban
Copyright (c) 2024 Elara Aerospace team
"""

# pylint: disable=too-few-public-methods

class AnomalyDetector:
    """
    A class used to detect anomalies in sensor data.
    """

    def detect(self, sensor_data):
        """
        Analyzes the sensor data and detects any anomalies
        based on predefined thresholds.
        """
        anomalies = {}

        if sensor_data['temperature'] < -40 or sensor_data['temperature'] > 120:
            anomalies['temperature'] = sensor_data['temperature']

        if sensor_data['pressure'] < 5 or sensor_data['pressure'] > 150:
            anomalies['pressure'] = sensor_data['pressure']

        if sensor_data['altitude'] < 0 or sensor_data['altitude'] > 9000:
            anomalies['altitude'] = sensor_data['altitude']

        return anomalies
