import asyncio
from viam.module.module import Module
from mcp300x import mcp3xxx



if __name__ == "__main__":
    asyncio.run(Module.run_from_registry())
