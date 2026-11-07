#port_report.py
#Check ports and classify them as system, user, or dynamic.

start_port = int(input("Start port:"))
end_port = int(input("End port:"))

Ports_checked = 0

for port in range (start_port,end_port + 1) :

     if port <= 1025: 
      print(f"{port}:system")
      
     elif port <= 49151 :
        print(f"{port}:user")
        
     elif port <=49153:
      print(f"{port}:dynamic")
     

 

Ports_checked +=1
print(f"Ports checked:{Ports_checked}")


