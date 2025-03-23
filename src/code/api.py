import json  
import os 
import sys

config_path = os.path.join(os.path.dirname(__file__), "..", "config", "configApi.json")

def setAPI(apikey=None):
    if apikey is None:  
        print("[Error]: Missing argument <API-KEY>")  
        sys.exit(1)

    try:  
        with open(config_path, "r") as file:
            config = json.load(file)
        
        config["Vulns"] = apikey  

        with open(config_path, "w") as file:
            json.dump(config, file, indent=4)

        print("[Success]: API key set successfully!")
        sys.exit()

    except FileNotFoundError as e:  
        print(f"[Error]: Error occurred while assigning API key: {e}")  
        sys.exit()
