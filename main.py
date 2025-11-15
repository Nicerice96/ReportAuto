# This is a automation script to automatically send information from Depenedncy Track (localhost:8080) to email.
import os
import requests
from dotenv import load_dotenv

load_dotenv("local.env")

API_KEY = os.getenv("API_KEY_DEPENDENCY_TRACK")

if not API_KEY:
    raise ValueError("API_KEY is missing...")
else:
    print(API_KEY)

BASE_URL = "http://localhost:8081/api"

PROJECT_URL = f"{BASE_URL}/project"

HEADERS = {
    "X-api-key" : API_KEY,
    "Accept" : "application/json"
}


    