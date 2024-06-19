# -*- coding: utf-8 -*-

"""
test_sensors.py

Copyright (c) 2024 Suriyaa Sundararuban
Copyright (c) 2024 Elara Aerospace team
"""

import unittest
from src.rocket_systems.sensors import SensorModule

class TestSensorModule(unittest.TestCase):
    def test_read_sensors(self):
        sensor_module = SensorModule()
        data = sensor_module.read_sensors()
        self.assertIn('temperature', data)
        self.assertIn('pressure', data)
        self.assertIn('altitude', data)

if __name__ == '__main__':
    unittest.main()
