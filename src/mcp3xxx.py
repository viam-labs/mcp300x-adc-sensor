from typing import ClassVar, Mapping, Sequence, Any, Dict, Optional, Tuple, Final, List, cast
from typing_extensions import Self

from viam.module.types import Reconfigurable
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName, Vector3
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily

from viam.components.sensor import Sensor
from viam.logging import getLogger

#import time
#import asyncio
import viam
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP3008
import adafruit_mcp3xxx.mcp3004 as MCP3004
from adafruit_mcp3xxx.analog_in import AnalogIn
from .utils import get_gpio_from_pin
# import RPi.GPIO as GPIO

LOGGER = getLogger(__name__)

class mcp3xxx(Sensor, Reconfigurable):
    # Here is where we define our new model's colon-delimited-triplet
    MODEL: ClassVar[Model] = Model(ModelFamily("viamlabs", "sensor"), "mcp3xxx")

    # create any class parameters here
    sensor_pin: int

    # Constructor
    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        sensor = cls(config.name)
        sensor.reconfigure(config, dependencies)
        return sensor

    # Validates JSON Configuration
    @classmethod
    def validate(cls, config: ComponentConfig):
        # here we validate config, the following is just an example and should be updated as needed
        sensor_pin = config.attributes.fields["sensor_pin"].number_value
        # channel_map = config.attributes.fields["channel_map"].number_value
        channel_map = config.attributes.fields["channel_map"].struct_value
        
        channel_amount = config.attributes.fields["channel_amount"].number_value

        if sensor_pin == "":
            raise Exception("A sensor_pin must be defined")
        
        #check map not defined ???
        # if channel_map == 0:
        #     raise Exception("A channel_map must not be empty")
        
        if channel_amount == "":
            raise Exception("A channel_amount must be defined, differentiating between different mcp300x's")

        return

    # Handles attribute reconfiguration
    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        # here we initialize the resource instance, the following is just an example and should be updated as needed
        self.sensor_pin = int(config.attributes.fields["sensor_pin"].number_value)

        self.channel_map = dict(config.attributes.fields["channel_map"].struct_value)
        # input = int(config.attributes.fields["channel_map"].number_value)

        LOGGER.info(f'TYPE fo channel map is {type(self.channel_map)}')
        LOGGER.info(f"CHANNEL MAP IS {self.channel_map}")

        self.channel_amount = int(config.attributes.fields["channel_amount"].number_value)
        return

    """ Implement the methods the Viam RDK defines for the Sensor API (rdk:components:sensor) """
    # Implement the Viam Sensor API's get_readings() method
    async def get_readings(
        self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Mapping[str, Any]:
        """
        Obtain the measurements/data specific to this sensor.
        Returns:
            Mapping[str, Any]: The measurements. Can be of any type.
        """

        #dictionary 
        readings = {}

        # SENSOR PIN LOGIC
        # Create the SPI bus
        spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

        # Create the cs (chip select) with a gpio pin variable, we are using 22 gpio 25
        my_pin = f"D{get_gpio_from_pin(self.sensor_pin)}"
        
        cs = digitalio.DigitalInOut(getattr(board, my_pin))

        # cs = digitalio.DigitalInOut(board.D25)
        # Create the MCP3008 object
        # mcp = MCP.MCP3008(spi, cs)

        # Create the MCP300x object
        mcp_type= f"MCP300{self.channel_amount}"
        # if self.channel_amount == 8:
        #     mcp = MCP.MCP3008(spi, cs)
        #this is currently overriding
        mcp = MCP3004.MCP3004(spi, cs)
        mcp = MCP3008.MCP3008(spi, cs)
        # mcp = getattr(MCP,mcp_type)
        LOGGER.error(f"MCP IS {mcp}")
        LOGGER.error(f"type of mcp is {type(mcp)}")
        # mcp(spi, cs)

        # Iterating over values
        for label, channel in self.channel_map.items():
            LOGGER.info(f"int he loop chamnnmel is {channel}")
            LOGGER.info(f"in the loop label is {label}")
            # Create an analog input channel on Pin ?
            chan = int(channel)
            my_chan = f"P{chan}"
            if chan ==0:
                LOGGER.error("REACHED 0")
                chanchan = AnalogIn(mcp, MCP3008.P0)
                LOGGER.warn(f"READING from channel 0 is {chanchan.value}")
            if chan ==1:
                LOGGER.error("REACHED 1")
                chanchan = AnalogIn(mcp, MCP3008.P1)
                LOGGER.warn(f"READING from channel 1 is {chanchan.value}")
            readings[label] = chanchan.value
      
        # Return readings
        return readings
