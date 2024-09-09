import sys
import subprocess


def set_dns(servers):
    interface = "Wi-Fi"  # Change to your specific network interface name if different
    if servers == "dhcp":
        command = f'netsh interface ip set dns "{interface}" dhcp'
        subprocess.run(command, shell=True)
    else:
        primary_dns = servers[0]
        secondary_dns = servers[1] if len(servers) > 1 else ""
        command = f'netsh interface ip set dns "{interface}" static {primary_dns}'
        subprocess.run(command, shell=True)
        if secondary_dns:
            command = (
                f'netsh interface ip add dns "{interface}" {secondary_dns} index=2'
            )
            subprocess.run(command, shell=True)

    print("DNS settings updated successfully.")
    show_dns(interface)


def show_dns(interface):
    command = f'netsh interface ip show dns "{interface}"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)


def main():
    dns_options = {
        "cloudflare": ["1.1.1.1", "1.0.0.1"],
        "google": ["8.8.8.8", "8.8.4.4"],
        "shecan": ["178.22.122.100", "185.51.200.2"],
        "403": ["10.202.10.202", "10.202.10.102"],
        "electro": ["78.157.42.100", "78.157.42.101"],
        "radar": ["10.202.10.10", "10.202.10.11"],
        "auto": "dhcp",
    }

    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        for key in dns_options.keys():
            if key.startswith(arg):
                set_dns(dns_options[key])
                return
        print("Invalid argument. Please provide a valid DNS option.")
    else:
        print("Please choose an option from the following:")
        for key in dns_options.keys():
            print(f"  {key}")
        print("Or type 'manual' to enter DNS settings manually.")

        choice = input("Enter your choice: ").lower()
        if "manual".startswith(choice):
            primary_dns = input("Enter primary DNS server: ")
            secondary_dns = input("Enter secondary DNS server (leave blank if none): ")
            set_dns([primary_dns, secondary_dns])
        else:
            for key in dns_options.keys():
                if key.startswith(choice):
                    set_dns(dns_options[key])
                    return
            else:
                print("Invalid choice. Exiting.")


if __name__ == "__main__":
    main()
