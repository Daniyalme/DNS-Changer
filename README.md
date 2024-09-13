# DNS Changer

This repository contains a Python script that allows users to automatically change their OS's DNS server to one of several well-known providers. It simplifies the process of switching between different DNS servers, making it easier to enhance security, privacy, or improve internet performance.

## Supported DNS Providers

The script supports the following DNS providers:

- **Cloudflare**
- **Google**
- **Shecan**
- **Electro**
- **Radar**
- **403**
- **Automatic (DHCP assigned DNS Server)**

## How to Use

### Direct Python Execution
You can directly run the Python script using:

```bash
python dns.py <dns_provider>
```

Replace `<dns_provider>` with the name (or partial name) of one of the supported DNS servers listed above. For example, to switch to Google's DNS, you can run:

```bash
python dns.py google
```

You can also run the script without arguments and input the DNS provider name interactively:

```bash
python dns.py
```

Then, type the DNS provider name (or part of it) when prompted, and the script will match it to the closest provider.

### Using the .bat File

First, replace `{PLACE YOUR DIRECTORY HERE}` in `dns.bat` with the absolute path of the `dns.py` file, then try running the batch file.
\
\
For easier usage, you can add the provided `.bat` file to your system's environment variables. This allows you to call the program directly from the command line using the command `dns`:

```bash
dns <dns_provider>
```

This method functions similarly to running the Python file, allowing you to specify the DNS provider by name or partial name.

### Example

To change the DNS server to Google, you can run:

```bash
dns google
```

Or just:

```bash
dns goog
```
And the code will automatically match the entered name

### Notes

- This script currently only works on Windows OS.
- The script supports partial matches for DNS provider names, making it more convenient to quickly switch DNS servers.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/DNS-Changer.git
   cd dns-changer
   ```

2. Add the `.bat` file to your environment variables for easy access (optional).
   
## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
