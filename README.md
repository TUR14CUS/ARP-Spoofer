# ARP Spoofer

## Introduction

The `arp_spoof.py` script is designed to perform ARP spoofing attacks on a target and a gateway within a local network. ARP spoofing involves sending falsified Address Resolution Protocol (ARP) messages to redirect traffic to a malicious entity.

## Usage

### Prerequisites

Make sure you have the required Python libraries installed:

```bash
pip install scapy
```

### Running the Script

1. Clone the repository:

```bash
git clone https://github.com/TUR14CUS/ARP-Spoofer.git
cd ARP-Spoofer
```

2. Run the script with the following command:

```bash
python arp_spoof.py -t [TARGET_IP] -g [GATEWAY_IP]
```

Replace `[TARGET_IP]` with the IP address of the target victim and `[GATEWAY_IP]` with the IP address of the network gateway.

## Options

- `-t, --target`: Specifies the target IP address.
- `-g, --gateway`: Specifies the IP address of the network gateway.

## Example

```bash
python arp_spoof.py -t 192.168.1.2 -g 192.168.1.1
```

## Important Note

This script is for educational purposes only. Unauthorized use of ARP spoofing or any form of network disruption is illegal. Ensure that you have explicit permission to perform any network-related activities.

## Disclaimer

The project contributors are not responsible for any misuse or damage caused by this script. Use it responsibly and in accordance with applicable laws and regulations.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
