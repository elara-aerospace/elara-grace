# -*- coding: utf-8 -*-

"""
main.py

Copyright (c) 2024 Suriyaa Sundararuban
Copyright (c) 2024 Elara Aerospace team
"""

# Disable 
# pylint: disable=E0401

import logging
from rocket_systems.sensors import SensorModule
from monitoring.anomaly_detection import AnomalyDetector
from monitoring.contingency_actions import ContingencyActions

logging.basicConfig(filename='logs/rocket_monitor.log', level=logging.INFO)

def main():
    """
    Main function to read sensor data, detect anomalies,
    and execute contingency actions.
    """
    sensor_module = SensorModule()
    anomaly_detector = AnomalyDetector()
    contingency_actions = ContingencyActions()

    while True:
        sensor_data = sensor_module.read_sensors()
        anomalies = anomaly_detector.detect(sensor_data)

        if anomalies:
            logging.warning("Anomalies detected: %s", anomalies)
            contingency_actions.execute(anomalies)

if __name__ == "__main__":
    main()
