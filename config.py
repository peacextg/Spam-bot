import logging
from telethon import TelegramClient
from RAUSHAN.data import ALTRON

# ------------------ LOGGING ------------------

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.INFO
)

# ------------------ CORE CONFIG ------------------

API_ID = 35411328
API_HASH = "4c8d3c8f5d3483296f5fb530ea2cfcc6"

CMD_HNDLR = "."

OWNER_ID = 8699868928

HEROKU_APP_NAME = ""
HEROKU_API_KEY = ""

# ------------------ USERS ------------------

SUDO_USERS = [6321617217 , 8499276647 , 6339597481 , 7816235846 , 8587611340 , 8762430892 , 8672896246]

for x in ALTRON:
    if x not in SUDO_USERS:
        SUDO_USERS.append(x)

if OWNER_ID not in SUDO_USERS:
    SUDO_USERS.append(OWNER_ID)

# ------------------ BOT TOKENS ------------------

BOT_TOKEN = "8953298308:AAEg9Ugzc5b3C035XjGvwNcsijRkUR8NOMM"
BOT_TOKEN2 = "8786308264:AAGaWL8egSVzk1SSs_ITKjvWm0nd8t5nHko"
BOT_TOKEN3 = "8705417949:AAEcw6uQNCLDa0ovG7yvAHaVt_up2qH_-JI"
BOT_TOKEN4 = "8857420192:AAGopMO5mGgst4nivsl5cUVk26KDHJ4sCUA"
BOT_TOKEN5 = "8549184662:AAHIUlZXe7PmOMKg_25WzR-KciolCsEnBHA"
BOT_TOKEN6 = "8745412754:AAHauso6b3_E1_CIR598Cyfohs6BxMjTsO8"
BOT_TOKEN7 = "8938699227:AAFPYDRxYuXbcuD1jzMA1o1Giz_hGKILFT0"
BOT_TOKEN8 = "8638885960:AAGg0hXOlT_0bjyZVgZ_M_HdHmCMwW8tX9g"
BOT_TOKEN9 = "8727891881:AAFX8HGTr4V_-QX5yI19qNeeYIRBL7lieyM"
BOT_TOKEN10 = "8730008848:AAGwvnLP2wDjWcTWlZmJrZ6cQig75RAMvrQ"

# ------------------ CLIENT HANDLER ------------------

def start_bot(session_name, bot_token):
    try:
        client = TelegramClient(session_name, API_ID, API_HASH)
        client.start(bot_token=bot_token)
        print(f"{session_name} started")
        return client
    except Exception as e:
        print(f"{session_name} failed: {e}")
        return None

# ------------------ START CLIENTS ------------------

X1 = start_bot("X1", BOT_TOKEN)
X2 = start_bot("X2", BOT_TOKEN2)
X3 = start_bot("X3", BOT_TOKEN3)
X4 = start_bot("X4", BOT_TOKEN4)
X5 = start_bot("X5", BOT_TOKEN5)
X6 = start_bot("X6", BOT_TOKEN6)
X7 = start_bot("X7", BOT_TOKEN7)
X8 = start_bot("X8", BOT_TOKEN8)
X9 = start_bot("X9", BOT_TOKEN9)
X10 = start_bot("X10", BOT_TOKEN10)

# ------------------ ACTIVE CLIENTS ------------------

CLIENTS = [x for x in [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10] if x is not None]

print(f"Total Active Bots: {len(CLIENTS)}")
