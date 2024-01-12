import scapy.all as scapy

# Create an ARP request packet.
arp_request = scapy.ARP(pdst="broadcast")
print(arp_request)
input()
# Send the ARP request packet to the network.
arp_responses = scapy.srp1(arp_request)

# Get the IP addresses of all devices that responded to the ARP request.
ip_addresses = []
for response in arp_responses:
    ip_addresses.append(response[0][1].psrc)

# Print the IP addresses of all devices in the network.
print(ip_addresses)