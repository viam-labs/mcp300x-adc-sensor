"""
This file registers the model with the Python SDK.
"""

from viam.components.sensor import Sensor
from viam.resource.registry import Registry, ResourceCreatorRegistration

from .mcp3xxx import mcp3xxx

Registry.register_resource_creator(Sensor.SUBTYPE, mcp3xxx.MODEL, ResourceCreatorRegistration(mcp3xxx.new, mcp3xxx.validate))
