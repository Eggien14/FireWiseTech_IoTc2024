# FireWise Tech: connection test firmware

This branch holds a variant of the sensor node firmware used to check that a node joins the gateway's Zigbee network before the full firmware is flashed. See the [`main` branch](https://github.com/Eggien14/FireWiseTech_IoTc2024) for the whole system and the [`Full_sensor_node`](https://github.com/Eggien14/FireWiseTech_IoTc2024/tree/Full_sensor_node) branch for the full node firmware.

## What it does

- Same board, sensors and reports as the full node (xG24 Dev Kit, BRD2601B).
- After each report sent to the coordinator, the LED on PB00 is turned on if the report was delivered and off if it failed or the node is not on the gateway's network. The node logs the PAN ID and send status on the serial console.
- Button 1 (PB02) makes the node leave and rejoin the network; after several failed reports it starts network steering again by itself.

## Use

1. Start the gateway (branch `Gateway---RaspberryPi4`) and open its network with the gateway button.
2. Import `Fw_Z3gw_Pi_EFR_24_7_copy1.slcp` in Simplicity Studio 5 (Gecko SDK 4.4.3), build and flash.
3. When the LED stays on, the node is connected; flash the full node firmware.
