import rblxopencloud
from rblxopencloud import Experience, NotFound

# 🔹 Open Cloud Configuration
EXPERIENCE_ID = 7404059538  # Replace with your Experience ID
API_KEY = "4xGLSvoI9EaMKVNsmE/16lWN/Yfbp5yvYMPVHVyWpVuXuLzFZXlKaGJHY2lPaUpTVXpJMU5pSXNJbXRwWkNJNkluTnBaeTB5TURJeExUQTNMVEV6VkRFNE9qVXhPalE1V2lJc0luUjVjQ0k2SWtwWFZDSjkuZXlKaVlYTmxRWEJwUzJWNUlqb2lOSGhIVEZOMmIwazVSV0ZOUzFaT2MyMUZMekUyYkZkT0wxbG1ZbkExZVhaWlRWQldTRlo1VjNCV2RWaDFUSHBHSWl3aWIzZHVaWEpKWkNJNklqZ3hOamd5TVRnM01EUWlMQ0poZFdRaU9pSlNiMkpzYjNoSmJuUmxjbTVoYkNJc0ltbHpjeUk2SWtOc2IzVmtRWFYwYUdWdWRHbGpZWFJwYjI1VFpYSjJhV05sSWl3aVpYaHdJam94TnpReU5qY3hPVEUyTENKcFlYUWlPakUzTkRJMk5qZ3pNVFlzSW01aVppSTZNVGMwTWpZMk9ETXhObjAuWk5kdUU0VWRkWnlGbFh1bXVvZWotN3NhU29zV2sxS2xNZVhKVUlYSldPbklNaUdoQmc1Q1RqVmhSWFhnWElDSlhHeFBObHBhd2dIeDMtdGZvSDlScU92WnpXVGxRclpFUnN3WEI2MlpRdGZwM2k2M0VYOWROWndneDdfZlYyY1dzWXoyS2FsYm1SbUJfdWMyb1FxNDZaNHNRRm12dTlIeS01ejhZSnVpXzJGRXJ5MzhzYld6cGJBUEtxZDhONEVvYXZTUnhPblhPVkpFY0lCRnoyS1F4c0xDYzVfRHpRdHhCV3BIb00zV2lwSlE2bVc2aXpYb1QzSWwxdHVUckZtcDVWOHFZdEY4YnVsQkFhTFM3bXBJUTVSZkxfMFVLVG9DVkkwYmxqRlBnUUN2b2U4TUlGc05DdjdLT3pTd2ZucU5US1JITEZZN1pwXzZiUTExeVpCSjln"  # Replace with a secure Open Cloud API Key

experience = Experience(EXPERIENCE_ID, API_KEY)
datastore = experience.get_datastore("PlayerData4", scope="global")

def set_ban_status(user_id, banned, reason="No reason provided"):
    """Set a player's banned status and reason in the DataStore."""
    key = f"user_{user_id}"

    try:
        # Fetch existing data
        value, info = datastore.get_entry(key)
    except NotFound:
        # If no data, create a new entry
        value = {"Banned": False, "Reason": ""}

    # Update banned status and reason
    value["Banned"] = banned
    value["Reason"] = reason if banned else ""

    # Save back to DataStore
    datastore.set_entry(key, value)
    
    if banned:
        print(f"User {user_id} has been BANNED. Reason: {reason}")
    else:
        print(f"User {user_id} has been UNBANNED.")

# Example Usage:
set_ban_status(8168218704, True, "Exploiting")  # Bans user 8168218704 with a reason
# set_ban_status(8168218704, False)  # Unbans user 8168218704
