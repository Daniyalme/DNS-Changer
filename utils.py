import sys
import json
import subprocess


def set_dns(servers, interface="Wi-Fi"):
    if "dhcp" in servers or "DHCP" in servers:
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


def print_dns(dns_dict, index=None):
    if index:
        print(f"\t{index}. Name       : {dns_dict['name']}")
    else:
        print(f"\t🟢 Name       : {dns_dict['name']}")

    print(f"\t   📄 Description: {dns_dict['description']}")
    print(f"\t   🌍 Origin     : {dns_dict['origin']}")
    print("\t", end="")
    print("-" * 80)
