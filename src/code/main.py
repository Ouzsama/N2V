import argparse 
from banner import get_banner
from  verfier import verify_targets

# import  shutil : shutil.get_terminal_size().columns




if __name__ == "__main__" : 

    get_banner ()
    parser = argparse.ArgumentParser(description = "Nmap to vulns tool")
    parser.add_argument("-t" ,  nargs="+" , help = "Target(s) (IP addresses ,  Domain names , CIDR)")
    parser.add_argument("-user-agent" , help = "HTTP header customazation")


    args = parser.parse_args() 


    if args.t  : 
        verify_targets(targets = args.t  ,  user_agent = args.user_agent) 
