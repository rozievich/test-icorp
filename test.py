import os
import json
import requests


url = "https://test.icorp.uz/interview.php"

def request_part1(host_url, callback_url):
    response = requests.post(host_url, json={"msg": "Salom, iCORP! Bu rozievich tomonidan iCORP uchun yaratilgan matn!", "url": callback_url})
    if response.status_code == 200:
        data = response.json()
        return data.get("part1")
    return None


if __name__ == "__main__":
    part1_data = request_part1(host_url=url, callback_url="https://ad5c47ff677a.ngrok-free.app/callback")
    if part1_data:
        if os.path.exists("received_data.json"):
            with open("received_data.json", "r") as f:
                received_data = json.loads(f.read())

        part2 = received_data.get("part2")
        code = part1_data + part2

        response = requests.get(url=url, params={"code": code})
        if response.status_code == 200:
            data = response.json()
            print(data.get("msg"))
    else:
        print("1-qism ma'lumotlarini olishda xatolik yuz berdi.")
