


import os  
import json
import sys

config_path  = os.path.join(os.path.dirname(__file__) , ".." , "config", "configApi.json")

def checkAPI () : 
    resuls = []

    try : 
        with open(config_path , "r") as file : 
            config = json.load(file) 
        

        for key , value in  config.items() : 
            if value == "API-KEY" : resuls.append(key)
        
        return resuls
    except FileNotFoundError : 
        print("[Error]: API config file not found ")
        sys.exit()
