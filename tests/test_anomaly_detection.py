# -*- coding: utf-8 -*-

"""
test_anomaly_detection.py

This module contains unit tests for the AnomalyDetector
class in the anomaly_detection module.

Copyright (c) 2024 Suriyaa Sundararuban
Copyright (c) 2024 Elara Aerospace team
"""

import unittest
from src.monitoring.anomaly_detection import AnomalyDetector

class TestAnomalyDetector(unittest.TestCase):
    """
    Unit tests for the AnomalyDetector class.
    """

    def test_detect(self):
        """
        Test the detect method to ensure it correctly
		identifies anomalies in sensor data.
        """
        anomaly_detector = AnomalyDetector()
        sensor_data = {
            'temperature': 130,
            'pressure': 10,
            'altitude': 1000
        }
        anomalies = anomaly_detector.detect(sensor_data)
        self.assertIn('temperature', anomalies)
        self.assertEqual(anomalies['temperature'], 130)

if __name__ == '__main__':
    unittest.main()
