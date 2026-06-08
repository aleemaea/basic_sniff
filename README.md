

## 🚀 Features
* **Live Packet Capturing:** Captures incoming and outgoing network traffic in real-time.
* **Protocol Breakdown:** Automatically identifies and parses common protocols like **TCP** and **UDP**.
* **Detailed Packet Architecture:** Dissects and prints crucial network headers including:
  * **Source IP Address** (Where the traffic started)
  * **Destination IP Address** (Where the traffic is going)
  * **Raw Payload Data** (Encrypted application-layer data or TLS/SSL handshakes)

---

## 🛠️ Requirements & Installation

This project requires a Windows environment with **Python 3.x**, administrative access, and a packet capture driver.

### 1. Prerequisites
* **Npcap:** Ensure you have Npcap installed on your machine to capture raw network packets on Windows.
* **Scapy Library:** Install Scapy via your terminal:
  ```bash
  pip install scapy
  Open your Command Prompt as an Administrator.

Navigate to your project folder:

DOS
cd C:\Users\ADMIN\Desktop\basic_sniff
Execute the script:

DOS
python sniffer.py
Press Ctrl + C at any time to safely terminate the program.
