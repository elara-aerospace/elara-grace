# -*- coding: utf-8 -*-

"""
main.py

Copyright (c) 2024 Suriyaa Sundararuban
Copyright (c) 2024 Elara Aerospace team
"""

import logging
from rocket_systems.sensors import SensorModule
from monitoring.anomaly_detection import AnomalyDetector
from monitoring.contingency_actions import ContingencyActions

logging.basicConfig(filename='logs/rocket_monitor.log', level=logging.INFO)

def main():
    sensor_module = SensorModule()
    anomaly_detector = AnomalyDetector()
    contingency_actions = ContingencyActions()

    while True:
        sensor_data = sensor_module.read_sensors()
        anomalies = anomaly_detector.detect(sensor_data)

        if anomalies:
            logging.warning(f"Anomalies detected: {anomalies}")
            contingency_actions.execute(anomalies)

if __name__ == "__main__":
    main()
