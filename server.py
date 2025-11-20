import json
from fastapi import FastAPI


app = FastAPI(name="iCORP Test Server")


@app.post("/callback")
async def callback_data(data: dict):
    with open("received_data.json", "w") as f:
        json.dump(data, f)
