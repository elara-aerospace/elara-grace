# -*- coding: utf-8 -*-

"""
sensors.py

Copyright (c) 2024 Suriyaa Sundararuban
Copyright (c) 2024 Elara Aerospace team
"""

import random

class SensorModule:
    def read_sensors(self):
        data = {
            'temperature': random.uniform(-50, 150),
            'pressure': random.uniform(0, 200),
            'altitude': random.uniform(0, 10000)
        }
        return data
