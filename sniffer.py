from scapy.all import sniff, IP, TCP, UDP, Raw

def process_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        
        protocol_name = "Other"
        if proto == 6:
            protocol_name = "TCP"
        elif proto == 17:
            protocol_name = "UDP"

        print(f"\n[+] --- New Packet Captured ---")
        print(f"    Source IP:      {src_ip}")
        print(f"    Destination IP: {dst_ip}")
        print(f"    Protocol:       {protocol_name}")

        if packet.haslayer(Raw):
            payload = packet[Raw].load
            print(f"    Payload (Data): {payload[:100]}...")

def main():
    print("==================================================")
    print("          CODEALPHA BASIC NETWORK SNIFFER          ")
    print("==================================================")
    print("[*] Monitoring network traffic... Press Ctrl+C to stop.")
    
    sniff(filter="ip", prn=process_packet, store=False)

if __name__ == "__main__":
    main()