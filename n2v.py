import argparse
from src.code.banner import get_banner
from src.code.verfier import verify_targets
from src.code.nmapscan import handle_targets
from src.code.vulns import handle_vulns_targets
from src.code.apicheck import checkAPI
from src.code.api import setAPI
from src.code.help import gethelp
import sys

if __name__ == "__main__":
    try:
        get_banner()

        parser = argparse.ArgumentParser(description="Nmap to Vulnerability Scanning Tool", add_help=False)
        parser.add_argument("-t", nargs="+", help="Target(s) (IP addresses, Domain names, CIDR)")
        parser.add_argument("-user-agent", help="Customize the User-Agent HTTP header (must be used with -t)")
        parser.add_argument("-vulners-api", help="Assign a Vulners.com API key (must be used alone)")
        parser.add_argument("-h", action="store_true", help="Display help")

        args = parser.parse_args()

        # Handle -h alone
        if args.h:
            if any([args.t, args.user_agent, args.vulners_api]):
                print("\n[Error]: -h (help) must be used alone!\n")
                sys.exit(1)
            gethelp()
            sys.exit(0)

        # Handle -vulners-api alone
        if args.vulners_api:
            if any([args.t, args.user_agent]):
                print("\n[Error]: -vulners-api must be used alone!\n")
                sys.exit(1)
            setAPI(args.vulners_api)
            sys.exit(0)

        # Handle -user-agent usage rule
        if args.user_agent and not args.t:
            print("\n[Error]: -user-agent must be used with -t!\n")
            sys.exit(1)

        # Handle -t (with or without -user-agent)
        if args.t:
            api = checkAPI()
            if not api:
                targets = verify_targets(targets=args.t, user_agent=args.user_agent)
                scan_result = handle_targets(targets=targets, user_agent=args.user_agent)
                handle_vulns_targets(scan_result=scan_result, user_agent=args.user_agent)
            else:
                print("\n[Error]: Missing required API keys!")
                print("[!] Ensure you have valid API keys for all necessary platforms.")
                print("[>] To set an API key, run: python n2v.py -vulners-api <YOUR-API-KEY>")
                print(f"[!] Missing API keys: {api}\n")
                sys.exit(1)

        # If no valid arguments are provided
        else:
            print("\n[Error]: No valid arguments provided!")
            gethelp()
            sys.exit(1)

    except KeyboardInterrupt:
        print("\n[!] Process interrupted by user. Exiting...")
        sys.exit(1)
