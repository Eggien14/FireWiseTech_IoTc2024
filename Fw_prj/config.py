import os

# Firebase settings are read from environment variables (see README and .env.example).
# Do not write real keys in this file.
FIREBASE_DATABASE_URL = os.getenv("FIREBASE_DATABASE_URL", "")
FIREBASE_CREDENTIALS = os.getenv(
    "FIREBASE_CREDENTIALS",
    "/home/pi/documents/Python/Fw_prj/Utility/firebase-adminsdk.json",  # service-account file, kept out of git
)
FIREBASE_CONFIG = {
    "apiKey": os.getenv("FIREBASE_API_KEY", ""),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN", ""),
    "databaseURL": FIREBASE_DATABASE_URL,
    "projectId": os.getenv("FIREBASE_PROJECT_ID", ""),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET", ""),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID", ""),
    "appId": os.getenv("FIREBASE_APP_ID", ""),
}
START_NETWORK = [
    "plugin network-creator start 1",
    "plugin network-creator-security open-network"    
]
OPEN_NETWORK =["plugin network-creator-security open-network"]
RESET_NETWORK = [
    "network leave",
    "plugin network-creator start 1",
    "plugin network-creator-security open-network"
]
SEND_NODE_ACTION = [""]
MAX_LOG_SIZE_BYTES = 1024 
SERIAL_PORT = "/dev/ttyACM0"

SYSTEM_LOG = "Hệ thống đã được thiết lập"
RISK3_LOG = "Chông báo cháy đang bật"
RISK2_LOG = "Cảnh báo nguy cơ cháy nổ"
RISK1_LOG = "Phát hiện bất thường"
OPEN_NETWORK_LOG = "Hệ thống đang mở mạng"
RESET_NETWORK_LOG = "Hệ thống thiết lập lại"
ERROR_EXE_LOG = "Lỗi thiết lập mạng"
HISTORY_DAYS_LIMIT = 1

PHONES_FILE = '/home/pi/documents/Python/Fw_prj/Utility/phone_numbers.json'

# LED control settings
LED_PIN = 16
LED_BLINK_DURATION = 5
LED_ON_DURATION = 10

LED_RED = 22
LED_BLUE = 27
LED_GREEN= 23