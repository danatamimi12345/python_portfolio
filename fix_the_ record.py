# fix_the_record.py
#  # This program prints a short record about a network device.

device_name = "edge-router"
#syntax error: variable name cannot start with a numbar .
backup_ip = "192.0.2.1"
#syntax error: variable name (class) is a resave kayword
device_type = "router"
# runtime error: invalid integer string
port = int("22")
#syntax erroe:forgetting a letter
print("Device:", device_name)

print("Backup IP:", backup_ip)

print("Type:", device_type)

print("Port:", port)