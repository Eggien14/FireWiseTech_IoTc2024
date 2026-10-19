# FireWise Tech: Zigbee fire-risk alert system

FireWise Tech is a team of 5 that took part in IoT Challenge 2024 (FPT Software and Silicon Labs) and was one of the 18 teams in the northern final. This repository holds the system the team built over about 3 months: Zigbee sensor nodes, a Raspberry Pi 4 gateway and a mobile app.

## What the system does

- **Sensor nodes** (Silicon Labs EFR32MG24) read a flame sensor, an MQ2 gas and smoke sensor and the on-board temperature and humidity sensor. Each node computes a fire-risk level from 0 to 3 by itself, sounds its buzzer at level 2 or higher and broadcasts the level over Zigbee, so the other nodes sound their alarm too.
- **Gateway** (Raspberry Pi 4) runs the Zigbee coordinator, receives the node data, shows the reported risk level on an RGB LED, uploads devices and event logs to Firebase Realtime Database, and includes a SIM module driver for phone-call and SMS alerts.
- **Mobile app** (Flutter) lets a user add a system by its ID and admin key, then shows every room with its flame, smoke, temperature and humidity readings and the event log.

```
 Sensor nodes (EFR32MG24)                 Raspberry Pi 4 gateway                     Cloud and app
 flame, MQ2, temp/humidity   Zigbee   ┌───────────────────────────────┐
 buzzer, 2 buttons        ─────────►  │ NCP (EFR32, ncp-uart-hw)       │
        ▲    │                        │   │ UART                       │
        │    │ broadcast risk level   │ Z3Gateway (Silicon Labs host)  │   Firebase     ┌────────────┐
        └────┘ to the other nodes     │   │ pexpect                    │ ──────────►    │ Realtime DB │ ◄── Flutter app
                                      │ Python: devices, logs, LED,    │                └────────────┘
                                      │ buttons, SIM call/SMS          │
                                      └───────────────────────────────┘
```

## Branches

The code of each part lives in its own branch; `main` only holds this overview.

| Branch | Contents |
|---|---|
| [`Full_sensor_node`](https://github.com/Eggien14/FireWiseTech_IoTc2024/tree/Full_sensor_node) | Firmware of the sensor node (Simplicity Studio project, Gecko SDK 4.4.3) |
| [`Test_connect_node`](https://github.com/Eggien14/FireWiseTech_IoTc2024/tree/Test_connect_node) | Node firmware used to check that a node joins the gateway's Zigbee network |
| [`Gateway---RaspberryPi4`](https://github.com/Eggien14/FireWiseTech_IoTc2024/tree/Gateway---RaspberryPi4) | Python gateway that runs on the Raspberry Pi 4 |
| [`App_mobile`](https://github.com/Eggien14/FireWiseTech_IoTc2024/tree/App_mobile) | Flutter mobile app |

## Fire-risk levels (computed on each node)

| Level | Condition |
|---|---|
| 3 | Flame detected together with a temperature jump of 10 °C or more, or with a gas index of 35 or more; or the alarm button is pressed |
| 2 | Gas index of 57 or more, or a temperature jump of 10 °C or more with a gas index of 35 or more |
| 1 | Gas index of 35 or more |
| 0 | Otherwise. A flame signal alone is treated as a possible false alarm caused by infrared light |

The gas index is the MQ2 voltage read by the ADC and scaled in firmware. A node turns its buzzer on when its own level, or the level broadcast by another node, is 2 or higher.

## Getting started

1. **Sensor node.** Install Simplicity Studio 5. Flash the `bootloader-uart-xmodem` example to each EFR32MG24 board, then build and flash the project from `Full_sensor_node`. To check the Zigbee link first, flash `Test_connect_node`: the LED on the node turns green when it has joined the network.
2. **Gateway.** Build the Z3Gateway example for Linux in Simplicity Studio and flash the `ncp-uart-hw` example to one EFR32 board connected to the Raspberry Pi by USB. Then follow the README of the `Gateway---RaspberryPi4` branch to install the Python dependencies and set the Firebase credentials.
3. **Mobile app.** Follow the README of the `App_mobile` branch. You need your own Firebase project and its `google-services.json`.

## Credentials

No Firebase key, service-account file or phone number is stored in this repository. The gateway reads its Firebase settings from environment variables and the app needs its own `google-services.json`; both are described in the README of the matching branch.

## Screenshots

<p>
  <img src="https://raw.githubusercontent.com/Eggien14/FireWiseTech_IoTc2024/App_mobile/assets/screenshot/3.png" width="220" alt="Rooms and sensor readings">
  <img src="https://raw.githubusercontent.com/Eggien14/FireWiseTech_IoTc2024/App_mobile/assets/screenshot/2.png" width="220" alt="Adding a system by ID and admin key">
  <img src="https://raw.githubusercontent.com/Eggien14/FireWiseTech_IoTc2024/App_mobile/assets/screenshot/5.png" width="220" alt="Event log">
</p>

## Team

Team of 5, led by Nguyen Trung Kien ([@Eggien14](https://github.com/Eggien14)), who built the Zigbee sensor nodes and worked on the gateway.
