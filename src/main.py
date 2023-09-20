import asyncio

from viam.components.sensor import Sensor
from viam.module.module import Module
from .mcp300x import mcp300x

async def main():
    """This function creates and starts a new module, after adding all desired resources.
    Resources must be pre-registered. For an example, see the `__init__.py` file.
    """
    module = Module.from_args()
    module.add_model_from_registry(Sensor.SUBTYPE, mcp300x.MODEL)
    await module.start()

if __name__ == "__main__":
    asyncio.run(main())
