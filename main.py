# This is a automation script to automatically send information from Depenedncy Track (localhost:8080) to email.
import os
import requests
from dotenv import load_dotenv
import json

from json_parse import parse_json_component_data

load_dotenv("local.env")

API_KEY = os.getenv("API_KEY_DEPENDENCY_TRACK")

if not API_KEY:
    raise ValueError("API_KEY is missing...")
else:
    print(API_KEY)
 
BASE_URL = "http://localhost:8081/api"

PROJECT_URL = f"{BASE_URL}/v1/project"


HEADERS = {
    "X-api-key" : API_KEY,
    "Accept" : "application/json"
}

def fetch_general_project_data():
    response = requests.get(PROJECT_URL, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def fetch_project_metadata(project_uuid):
    COMPONENT_URL=f"{BASE_URL}/v1/component/project/{project_uuid}"
    response = requests.get(COMPONENT_URL, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def write_to_file(json_data, filename):
    
    try:
        
        
        with open(filename, 'w') as f:
            json.dump(json_data, f, indent=4)
    except Exception as e:
        print("JSON write has been unsuccessful!", e)



if __name__ == "__main__":
    write_to_file(fetch_general_project_data(), "Project_Data/project_high_level_metadata.json")
    
    
    write_to_file(
        fetch_project_metadata("9c7a2e49-c2e2-4ca2-870a-dd98e8224cab"),
        "Component_Data/project_component_data.json"
                  )
    
    # Returns name + version and latest version...
    parse_json_component_data("Component_Data/project_component_data.json")
    
    
    
    

    