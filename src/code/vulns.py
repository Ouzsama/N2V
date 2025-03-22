import sys 
import requests
import os
import json 



def n2vulns(nr, apikey) : 

    for r in nr  : 
        print(r)

def getAPI () : 
    try : 
        config_api_path = os.path.join(os.path.dirname(__file__) , ".." , "config" , "configApi.json")
        with open(config_api_path , "r") as file : 
            config = json.load(file) 

        API_KEY = config["Vulns"]
        return API_KEY
    except FileNotFoundError : 
        print("\n[Error]: Api configuration file is not found ! ")
        sys.exit()
    


def handle_vulns_targets (scan_result = None , user_agent = None) : 
    if scan_result is None  : 
        
        sys.exit()
    
    if user_agent is not None  : 
        requests.Session().headers.update({"User-Agent" : user_agent})

    
    try : 
        API_KEY = getAPI()

            
        # check if vulns platfrom is reachable : 
        r = requests.get("https://vulns.com") 
        if r.status_code < 400 : 
            n2vulns(scan_result , apikey)
            


        
        else : 
            print("[Info]: Vulns.com is not reachable now !")
            sys.exit()
    except Exception : 
        print ("[Error]: error occured with vulns.com")
        sys.exit()
