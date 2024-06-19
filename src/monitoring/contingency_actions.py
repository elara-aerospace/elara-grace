# -*- coding: utf-8 -*-

"""
contingency_actions.py

Copyright (c) 2024 Suriyaa Sundararuban
Copyright (c) 2024 Elara Aerospace team
"""

from rocket_systems.actuators import ActuatorModule
from rocket_systems.communications import CommunicationsModule

class ContingencyActions:
    def __init__(self):
        self.actuator = ActuatorModule()
        self.communications = CommunicationsModule()

    def execute(self, anomalies):
        if 'temperature' in anomalies:
            self.communications.send_data(f"High temperature detected: {anomalies['temperature']}")
        
        if 'pressure' in anomalies:
            self.communications.send_data(f"Abnormal pressure detected: {anomalies['pressure']}")
        
        if 'altitude' in anomalies:
            self.communications.send_data(f"Abnormal altitude detected: {anomalies['altitude']}")
            self.actuator.activate_parachute()
