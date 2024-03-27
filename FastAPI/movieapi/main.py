from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import requests

from domain.user import user_router

app = FastAPI()

origins = [
    "http://localhost:5173",  # 또는 "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router.router)

@app.get("/fetch_data")
async def fetch_data(title: str = ''):
    base_url = "http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_json2.jsp"
    params = {
        "ServiceKey": "2020049E1D9AI37X32Z3",
        "collection": "kmdb_new2",
        "title": title
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data from the API."}
