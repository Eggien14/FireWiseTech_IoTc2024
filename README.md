# FireWise Tech: Raspberry Pi 4 gateway

This branch holds the gateway of the FireWise Tech fire-risk alert system (IoT Challenge 2024). See the [`main` branch](https://github.com/Eggien14/FireWiseTech_IoTc2024) for the whole system and the other branches.

## What the gateway does

- Starts the Silicon Labs **Z3Gateway** host program, which talks to an EFR32 board flashed with `ncp-uart-hw` (USB, `/dev/ttyACM0`), and creates an open Zigbee network.
- Parses the messages of each sensor node (flame, gas index, temperature, humidity, risk level) and shows the reported risk level on an RGB LED (green 1, blue 2, red 3).
- Uploads each device and an event log to Firebase Realtime Database under `Systems/<Raspberry Pi serial number>`; the mobile app reads the same tree.
- The button on GPIO 5 opens the Zigbee network so that new nodes can join.
- `sim_com.py` drives a SIM module with AT commands (`/dev/ttyUSB0`) to call or text the phone numbers saved for the system in Firebase. The SIM thread is switched off in `main.py` by default.

## Files

| Path | Role |
|---|---|
| `Fw_prj/main.py` | Entry point: starts the button, Zigbee and Firebase threads |
| `Fw_prj/zigbee_manager.py` | Runs Z3Gateway through `pexpect`, sends network commands and parses node messages |
| `Fw_prj/data_analyst.py` | Risk handling: LED colour, event log, SIM alerts |
| `Fw_prj/firebase_service.py` | Firebase Realtime Database access |
| `Fw_prj/sim_com.py` | SIM module (AT commands) |
| `Fw_prj/button_reader.py`, `Fw_prj/led_RGB.py` | Button and RGB LED |
| `Fw_prj/config.py` | Network commands, pins, log messages and Firebase settings read from environment variables |
| `Fw_prj/auto.sh` | Start-up script for `crontab @reboot` |

## Setup on the Raspberry Pi

1. Build the Z3Gateway example for Linux in Simplicity Studio and copy the binary to `/home/pi/Z3gateway_2` (the path used in `zigbee_manager.py`).
2. Copy this branch to `/home/pi/documents/Python/` and create the virtual environment:

   ```bash
   cd /home/pi/documents/Python
   python3 -m venv --system-site-packages myenv
   myenv/bin/pip install -r requirements.txt
   ```

3. Firebase credentials are not in the repository. In your Firebase project, create a service-account key (Project settings, Service accounts) and save it as `Fw_prj/Utility/firebase-adminsdk.json`. Then copy `Fw_prj/.env.example` to `Fw_prj/.env` and set `FIREBASE_DATABASE_URL`. Both files are git-ignored.
4. Run `Fw_prj/auto.sh`, or add it to `crontab -e` as `@reboot /home/pi/documents/Python/Fw_prj/auto.sh`. The script loads `Fw_prj/.env` and starts `main.py`.
