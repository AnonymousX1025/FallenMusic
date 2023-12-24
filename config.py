from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "29535970"))
API_HASH = getenv("API_HASH", "bead7e32f0dcfc317b0b57717d819a14")

BOT_TOKEN = getenv("BOT_TOKEN", "6528153674:AAH2GNkbSdEcbt41goGBXDUQtZD4GrlUjRo")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "5779185981"))

PING_IMG = getenv("PING_IMG", "https://i.postimg.cc/Pqy82pxN/a8417f70-4e09-473b-b8ac-521989f048c5.jpg")
START_IMG = getenv("START_IMG", "https://i.postimg.cc/Pqy82pxN/a8417f70-4e09-473b-b8ac-521989f048c5.jpg")

SESSION = getenv("SESSION", "BQHCruIApls9NvanUjG87IBujQrLyZ37ESXcuAmIKeoRAdm9iHqzN-Dsd9RoTl1yZmw8zADGxUPARt_bMqUiRkHaUKi-uHNiDWWrQPYRQk_Lba0uPR85_Q38WV-cpvPKkAAab2TpkE-SWpswOJv2u_uXJQpP4WrXBHGSf_vr72xHHMchDudicC4bunw2RnQgyWW89s3cSaXc9xRVqBfvOerYAHgg6nVetKu7duYqojmJTye6YgKiEUoBYK4Y0o1CCV78v4cGEVGT-620nleth9f0ZLVeOExvTVkWUxELMv1WAZRPP5ZkIjvDkl22_o7ka34axuARH9aWUucm-cJt6kqKUkfWngAAAABXh0liAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/musicgreat_bott")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Great0623")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://i.postimg.cc/Pqy82pxN/a8417f70-4e09-473b-b8ac-521989f048c5.jpg"
