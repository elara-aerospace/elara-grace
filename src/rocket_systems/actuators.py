# -*- coding: utf-8 -*-

"""
actuators.py

This module defines the ActuatorModule class responsible for controlling
the actuators of the rocket system.

Copyright (c) 2024 Suriyaa Sundararuban
Copyright (c) 2024 Elara Aerospace team
"""

# pylint: disable=too-few-public-methods

class ActuatorModule:
    """
    A class used to control the actuators of the rocket system.

    Methods
    -------
    activate_parachute():
        Activates the parachute.
    """
    
    def activate_parachute(self):
        """
        Activates the parachute by sending the appropriate command to the actuator.
        """
        print("Parachute activated!")
