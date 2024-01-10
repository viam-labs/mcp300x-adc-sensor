# mcp300x-adc-sensor

The module provides analog-to-digital conversion capabilities for MCP300x SPI ADCs. Tested on MCP3002, MCP3004, and MCP3008 using a Raspberry Pi. If you are using any other board, check out the go modules that are board agnostic: https://app.viam.com/module/hazalmestci/mcp3001-2 and https://app.viam.com/module/hazalmestci/mcp3004-8. 

For MCP3002, you can get readings for up to 2 sensors from channel 0 and channel 1.
For MCP3004, you can get readings for up to 4 sensors from channel 0 to channel 3.
For MCP3008, you can get readings for up to 8 sensors from channel 0 to channel 7.

Wiring for these sensors is different and you should refer to data sheets for each ADC.

The sensors should be declared in the sensor configuration in the Viam app. For example, if you have a moisture sensor attached to channel 0, a temperature sensor attached to channel 1, and a humidity sensor attached to channel 2, your channel_map in the config should look like this:

  "channel_map": {
    "moisture": 0,
    "temperature": 1,
    "humidity": 2
  }

Since you are getting readings from three separate channels, you won't be able to use the MCP3002 sensor for this use case, and will need either an MCP3004 or an MCP3008.
