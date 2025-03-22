import argparse 
from banner import get_banner
from  verfier import verify_targets
from ntv  import handle_targets
from vulns import handle_vulns_targets 
from apicheck import checkAPI
import sys
import os

# import  shutil : shutil.get_terminal_size().colcumns




if __name__ == "__main__" : 

    get_banner ()
    parser = argparse.ArgumentParser(description = "Nmap to vulns tool")
    parser.add_argument("-t" ,  nargs="+" , help = "Target(s) (IP addresses ,  Domain names , CIDR)")
    parser.add_argument("-user-agent" , help = "HTTP header customazation")


    args = parser.parse_args() 


    if args.t  : 
        # API verification  ,  for vulns  : 
        api = checkAPI() 
        if not api : 

            targets = verify_targets(targets = args.t  ,  user_agent = args.user_agent) 
            scan_result = handle_targets(targets = targets , user_agent = args.user_agent )
            #handle_vulns_targets(scan_result = scan_result ,user_agent = args.user_agent )
            #print(scan_result)
        else  : 
            
            print("[Error]: API keys not found  ,  make sure to have all the platforms free API keys , check requirements !")
            print(f"[Error]: Missing API keys : {api}")
            sys.exit()
        

