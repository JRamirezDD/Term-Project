import socket

def connectivity_test_me(target_ip, target_port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)  # Set a timeout for the connection attempt
            s.connect((target_ip, target_port))
        print(f"Success! Port {target_port} on {target_ip} is open.")
    except Exception as e:
        print(f"Failed to connect to port {target_port} on {target_ip}.")
        print(e)


target_ip = "10.30.13.53"
target_port = 56658
    
    
connectivity_test_me(target_ip,target_port)