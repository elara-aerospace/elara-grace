# -*- coding: utf-8 -*-

"""
communications.py

This module defines the CommunicationsModule class responsible for handling
the communication operations of the rocket system.

Copyright (c) 2024 Suriyaa Sundararuban
Copyright (c) 2024 Elara Aerospace team
"""

# pylint: disable=too-few-public-methods

class CommunicationsModule:
    """
    A class used to handle communication operations of the rocket system.

    Methods
    -------
    send_data(data):
        Sends data to the communication system.
    """

    def send_data(self, data):
        """
        Sends data to the communication system.

        Parameters
        ----------
        data : str
            The data to be sent.
        """
        print(f"Sending data: {data}")
