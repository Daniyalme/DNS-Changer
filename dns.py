import sys
import json
import subprocess
import time

from utils import *


def main():
    with open("C:\\Users\\mehra\\Documents\\Projects\\DNS\\config.json", "r") as file:
        data = json.load(file)

    dns_options = data["dns_servers"]

    if len(sys.argv) > 1:
        # with argument
        dns_argument = sys.argv[1].lower()

        matched_dns_servers = [
            dns_server
            for dns_server in dns_options
            if dns_server["name"].lower().startswith(dns_argument)
        ]

        selected = None

        if len(matched_dns_servers) < 1:
            print(
                "\n⚠️ Invalid argument. Please run the program again and choose a valid DNS name."
            )
            return

        elif len(matched_dns_servers) > 1:
            print(f'\n📡 Available DNS Servers starting with "{dns_argument}":\n')
            for i, server in enumerate(matched_dns_servers):
                print_dns(server, index=i + 1)

            chosen = input(
                "\n👉 Enter the number of DNS Server you'd like to use: "
            ).strip()

            # Match and display selected server details
            idx = int(chosen) - 1
            if len(matched_dns_servers) > idx >= 0:
                selected = matched_dns_servers[idx]

        else:
            selected = matched_dns_servers[0]

        # Setting the DNS Server
        if selected:
            print("\n✅ You selected:")
            print(f"🔹 Name       : {selected['name']}")
            print(f"🔸 Primary DNS: {selected['primary_dns']}")
            print(f"🔸 Secondary DNS: {selected['secondary_dns']}")

            set_dns([selected["primary_dns"], selected["secondary_dns"]])
        else:
            print(
                "\n⚠️ Invalid selection. Please run the program again and choose a valid DNS name."
            )
            return

    else:
        # without argument
        print("\n📡 Available DNS Servers:\n")
        time.sleep(1)
        for server in data["dns_servers"]:
            print_dns(server)
            time.sleep(0.1)

        print("\n👉 Enter the name of the DNS server you'd like to use ")
        print("Or type 'manual' to enter DNS settings manually: ", end="")

        choice = input("").lower()

        # Manual Entry
        if "manual".startswith(choice):
            primary_dns = input("Enter primary DNS server: ")
            secondary_dns = input("Enter secondary DNS server (leave blank if none): ")
            set_dns([primary_dns, secondary_dns])

        # Matching the dns server name
        else:
            matched_dns_servers = [
                dns_server
                for dns_server in dns_options
                if dns_server["name"].lower().startswith(choice)
            ]

            selected = None

            if len(matched_dns_servers) < 1:
                print(
                    "\n⚠️ Invalid selection. Please run the program again and choose a valid DNS name."
                )
                return

            elif len(matched_dns_servers) > 1:
                print(f'📡 Available DNS Servers starting with "{choice}":\n')
                for i, server in enumerate(matched_dns_servers):
                    print_dns(server, index=i + 1)

                chosen = input(
                    "\n👉 Enter the number of DNS Server you'd like to use: "
                ).strip()

                # Match and display selected server details
                idx = int(chosen) - 1
                if len(matched_dns_servers) > idx >= 0:
                    selected = matched_dns_servers[idx]

            else:
                selected = matched_dns_servers[0]

            # Setting the DNS Server
            if selected:
                print("\n✅ You selected:")
                print(f"🔹 Name       : {selected['name']}")
                print(f"🔸 Primary DNS: {selected['primary_dns']}")
                print(f"🔸 Secondary DNS: {selected['secondary_dns']}")

                set_dns([selected["primary_dns"], selected["secondary_dns"]])
            else:
                print(
                    "\n⚠️ Invalid selection. Please run the program again and choose a valid DNS name."
                )
                return


if __name__ == "__main__":
    main()
