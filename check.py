import os
import requests
from time import sleep

WEBHOOK_URL = "https://discord.com/api/webhooks/1240691603274731615/66sC_zbvsxVvNQt_H7ooQGoDpQqUJA8oCQ6QNdsRKq2CgoX0IsR7LSJ2HE67VFC-yJ2x"
FILE_PATH = "KEYFOUNDKEYFOUND.txt"

def check_file_update():
    global last_modified_time
    global last_content

    current_modified_time = os.path.getmtime(FILE_PATH)

    if current_modified_time != last_modified_time:
        last_modified_time = current_modified_time

        with open(FILE_PATH, "r") as file:
            content = file.read()

        if content != last_content:
            last_content = content
            send_discord_message(f"File Updated!\nNew Content:\n{content}")

def send_discord_message(message):
    payload = {
        "content": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(WEBHOOK_URL, json=payload, headers=headers)
    if response.status_code != 200:
        print("Failed to send message to Discord.")

last_modified_time = os.path.getmtime(FILE_PATH)
last_content = ""

while True:
    check_file_update()
    sleep(5)  # Check every 5 minutes
