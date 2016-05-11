"""
This module contains abstraction for a single robot.

This abstraction contains and allows access to robot parts,
especcially all it's sensors and effectors.
"""

from .sensors import Sensor
from .motor import Motor


class Robot:
    """
    Basically it's a flexible container for all robots parts.
    """

    def __init__(self, simulation, name=None):
        self._name = name
        self.sim = simulation
        self.sensors = dict()
        self.motors = dict()

    def add_sensor(self, name, sensor_type, key=None, *args, **kwargs):
        """
        Add sensor with given name to robot's sensors.

        New sensor is added with given key to sensors of this robot.
        If no key is supplied, then name is used instead.
        Key must be unique per robot.

        Currently sensor types with full support: proximity.

        Note: sharing sensors beetween robots is currently not supported.
        """
        if key is None:
            key = name

        sensor = Sensor.create(simulation=self.sim, typ=sensor_type, name=name, *args, **kwargs)
        self.sensors[key] = sensor

    @property
    def sensor_readings(self):
        """
        Return dictionary containing results from all sensors
        assigned to the robot.
        """
        return {key: self.sensors[key].read for key in self.sensors}

    def add_motor(self, name, key=None):
        """
        Add motor with given name to robot's motor list.

        New motor must have an unique key identifier, if no such is supplied,
        the name will be used.

        Note: One engine should belong to exactly one robot.
        """
        if key is None:
            key = name

        motor = Motor(simulation=self.sim, name=name)
        self.motors[key] = motor

    @property
    def name(self):
        if self.name is not None:
            return self._name
        else:
            return "Unnamed"

    __name = name

    def __str__(self):
        return "<{cls} '{name}'>".format(cls=self.__class__.__name__, name=self.__name)