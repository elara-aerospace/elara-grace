# -*- coding: utf-8 -*-

"""
sensors.py

This module defines the SensorModule class responsible
for reading sensor data from the rocket system.

Copyright (c) 2024 Suriyaa Sundararuban
Copyright (c) 2024 Elara Aerospace team
"""

# pylint: disable=too-few-public-methods

import random

class SensorModule:
    """
    A class used to read sensor data from the rocket system.
    """
    
    def read_sensors(self):
        """
        Reads the real-time values from the sensors.
        """
        data = {
            'temperature': random.uniform(-50, 150),
            'pressure': random.uniform(0, 200),
            'altitude': random.uniform(0, 10000)
        }
        return data
