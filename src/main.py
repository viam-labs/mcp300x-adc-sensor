import asyncio

from viam.module.module import Module

# Imported for its side effect: defining mcp3xxx registers the model with the
# registry that run_from_registry serves.
from mcp300x import mcp3xxx  # noqa: F401

if __name__ == "__main__":
    asyncio.run(Module.run_from_registry())
