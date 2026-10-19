# FireWise Tech: sensor node firmware

This branch holds the firmware of the FireWise Tech sensor node (IoT Challenge 2024). See the [`main` branch](https://github.com/Eggien14/FireWiseTech_IoTc2024) for the whole system and the other branches.

## Hardware

Silicon Labs xG24 Dev Kit (BRD2601B, EFR32MG24) with:

| Part | Pin | Use |
|---|---|---|
| MQ2 gas and smoke sensor | PA07 (ADC) | Gas index |
| LM393 flame sensor | PC01 | Flame detected or not |
| On-board temperature and humidity sensor | I2C (board) | Temperature, humidity |
| Button 0 | PC03 | Manual alarm (forces level 3) |
| Button 1 | PB02 | Leave and rejoin the Zigbee network |
| Buzzer | PD02 | Local alarm |

## How the node works

- At start-up the node leaves any old network and joins the gateway's network with network steering. If it is not on the gateway's PAN, it tries again every few cycles.
- Every 2 s it sends temperature, humidity, gas index, flame and risk level to the coordinator (node ID 0x0000) by unicast.
- It computes the risk level (0 to 3) itself; the rules are listed in the README of the `main` branch.
- When its level changes, it broadcasts the level to every node in the network. A node sounds its buzzer when its own level, or the level heard from another node, is 2 or higher.

## Main files

| File | Role |
|---|---|
| `app.c` | Main loop: read sensors, drive the buzzer, broadcast level changes |
| `sensor_data.c`, `iadc.c` | Sensor reading, buttons, risk level |
| `zigbee_manager.c` | Network steering, periodic report to the coordinator, broadcast and reception of alarm levels |

## Build

1. Install Simplicity Studio 5 with Gecko SDK 4.4.3 (a copy of the SDK files used is in `gecko_sdk_4.4.3/`).
2. Flash the `bootloader-uart-xmodem` example to the board once.
3. Import this folder as a project (`Fw_Z3gw_Pi_EFR_24_7.slps`), build and flash.
4. To check only the link to the gateway first, use the [`Test_connect_node`](https://github.com/Eggien14/FireWiseTech_IoTc2024/tree/Test_connect_node) branch.
