# -*- coding: utf-8 -*-

"""
contingency_actions.py

Copyright (c) 2024 Suriyaa Sundararuban
Copyright (c) 2024 Elara Aerospace team
"""

# pylint: disable=E0401
# pylint: disable=too-few-public-methods

from rocket_systems.actuators import ActuatorModule
from rocket_systems.communications import CommunicationsModule

class ContingencyActions:
    """
    A class used to execute contingency actions based on detected anomalies.
    """

    def __init__(self):
        """
        Initializes the ContingencyActions with instances of ActuatorModule
        and CommunicationsModule.
        """
        self.actuator = ActuatorModule()
        self.communications = CommunicationsModule()

    def execute(self, anomalies):
        """
        Executes the appropriate actions based on the detected anomalies.
        """
        if 'temperature' in anomalies:
            self.communications.send_data(f"High temperature detected: {anomalies['temperature']}")

        if 'pressure' in anomalies:
            self.communications.send_data(f"Abnormal pressure detected: {anomalies['pressure']}")

        if 'altitude' in anomalies:
            self.communications.send_data(f"Abnormal altitude detected: {anomalies['altitude']}")
            self.actuator.activate_parachute()
