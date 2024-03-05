# `mcp300x-adc-sensor` modular resource

The module provides analog-to-digital conversion capabilities for MCP300x SPI ADCs. Tested on MCP3002, MCP3004, and MCP3008 using a Raspberry Pi. If you are using any other board, check out the go modules that are board agnostic: https://app.viam.com/module/hazalmestci/mcp3001-2 and https://app.viam.com/module/hazalmestci/mcp3004-8. 

For MCP3002, you can get readings for up to 2 sensors from channel 0 and channel 1.
For MCP3004, you can get readings for up to 4 sensors from channel 0 to channel 3.
For MCP3008, you can get readings for up to 8 sensors from channel 0 to channel 7.

Wiring for these sensors is different and you should refer to data sheets for each ADC.

## Build and run

To use this module, follow the instructions to [add a module from the Viam Registry](https://docs.viam.com/registry/configure/#add-a-modular-resource-from-the-viam-registry) and select the `hazalmestci:sensor:mcp300x` model from the [`mcp300x-adc-sensor` module](https://app.viam.com/module/hazalmestci/mcp300x-adc-sensor).

## Configure your `mcp300x-adc-sensor`

> [!NOTE]
> Before configuring your `mcp300x-adc-sensor`, you must [create a machine](https://docs.viam.com/manage/fleet/machines/#add-a-new-machine).

Navigate to the **Config** tab of your machine's page in [the Viam app](https://app.viam.com/).
Click on the **Components** subtab and click **Create component**.
Select the `sensor` type, then select the `hazalmestci:sensor:mcp300x` model.
Click **Add module**, then enter a name for your sensor and click **Create**.

On the new component panel, copy and paste the following attribute template into your sensor’s **Attributes** box:

> [!NOTE]
> For more information, see [Configure a Machine](https://docs.viam.com/manage/configuration/).

```json
{
  "channel_map": {
    "moisture": 0,
    "temperature": 1,
    "humidity": 2
  }
}
```

Save your config.

### Attributes

The following attributes are available for a `mcp300x-adc-sensor` sensor:

| Name    | Type   | Inclusion    | Description |
| ------- | ------ | ------------ | ----------- |
| `channel_map` | string | **Required** | The channel map for moisture, temperature, and humidity. |

### Example configuration

For example, if you have a moisture sensor attached to channel 0, a temperature sensor attached to channel 1, and a humidity sensor attached to channel 2, your config should look like this:

```json
{
    "name": "my-mcp300x",
    "model": "hazalmestci:sensor:mcp300x",
    "type": "sensor",
    "namespace": "rdk",
    "attributes": {
      "channel_map": {
        "moisture": 0,
        "temperature": 1,
        "humidity": 2
      }
    },
    "depends_on": []
}
```

Since you are getting readings from three separate channels, you won't be able to use the MCP3002 sensor for this use case, and will need either an MCP3004 or an MCP3008.

## Next Steps

1. To test your sensor, go to the [**Control** tab](https://docs.viam.com/manage/fleet/robots/#control) and test that you are getting readings.
2. Once you can obtain your readings, configure the data manager to [capture](https://docs.viam.com/data/capture/) and [sync](https://docs.viam.com/data/cloud-sync/) the data from all of your machines.
3. To retrieve data captured with the data manager, you can [query data with SQL or MQL](https://docs.viam.com/data/query/) or [visualize it with tools like Grafana](https://docs.viam.com/data/visualize/).

## License

Copyright 2021-2023 Viam Inc. <br>
Apache 2.0
