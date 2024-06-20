# -*- coding: utf-8 -*-

"""
test_sensors.py

This module contains unit tests for the SensorModule class
in the rocket_systems.sensors module.

Copyright (c) 2024 Suriyaa Sundararuban
Copyright (c) 2024 Elara Aerospace team
"""

import unittest
from src.rocket_systems.sensors import SensorModule

class TestSensorModule(unittest.TestCase):
    """
    Unit tests for the SensorModule class.
    """

    def test_read_sensors(self):
        """
        Test the read_sensors method to ensure it returns
		data with keys for temperature, pressure, and altitude.
        """
        sensor_module = SensorModule()
        data = sensor_module.read_sensors()
        self.assertIn('temperature', data)
        self.assertIn('pressure', data)
        self.assertIn('altitude', data)

if __name__ == '__main__':
    unittest.main()
