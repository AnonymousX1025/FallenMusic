from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("22286214"))
API_HASH = getenv("8cb579fec7c2a81b0777fc8f745e406d")

BOT_TOKEN = getenv("7548201631:AAEWVbOcWsbXReaffWCVftUau4Xg8XCbg4s", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("7798714693"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("BQFUD4YAGWXt1MYCqBoHFAkcbCIAshedzPgXmFUzNwpTDNeTSjPdUh7y0b3Z-gipmZUfdFz-d30zzUrl2hea-ZWleeWCEK0v6j5hNmt-HPopSrf2PtRyiYP1V6l3L46ziVBxc6K3pbJ0Fl4BpA2pisNZfQaUD88VdpzlsnfN8Ci2XkQkqv8pqLkTsZF8lzp5uw3oXoWXEzu-rVSnyiT-c_yYOVK0WSVeMToY20HqQNNODZFcfSWVegHf4IB3A4C5YOCP8xjnImX_6imyTse6gf31ZWgwe6-kAb9nKfe1VuoWkPo-Sj8MyukVUal-sMYyO6J8aBkM_eO5ZR_9Htigrqv_c00J2wAAAAHBRUi2AA", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/friends_talk_zon")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/uk_meee")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
