# port_facts.py

# RFC 9293: Source Port and Destination Port are 16 bits each.
# RFC 791: IPv4 addresses are 32 bits.

port_bits = 16
ipv4_bits = 32

possible_ports = 2 ** port_bits
highest_port = possible_ports - 1
possible_ipv4_addresses = 2 ** ipv4_bits

print(f"Possible port numbers: {possible_ports}")
print(f"Highest port number: {highest_port}")
print(f"Possible IPv4 addresses: {possible_ipv4_addresses}")##