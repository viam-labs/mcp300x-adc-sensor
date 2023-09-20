"""
This file registers the model with the Python SDK.
"""

from viam.components.sensor import Sensor
from viam.resource.registry import Registry, ResourceCreatorRegistration

from .mcp300x import mcp300x

Registry.register_resource_creator(Sensor.SUBTYPE, mcp300x.MODEL, ResourceCreatorRegistration(mcp300x.new, mcp300x.validate))
