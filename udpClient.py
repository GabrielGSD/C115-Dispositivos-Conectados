import socket

while True:

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_host = socket.gethostname()
    udp_port = 12000

    msg = input("\nBom dia,\nclique 1 para crédito \nClique 2 para débito\n ")
    
    if msg == "3":
        print("ERRO!! SAINDO...")
        sock.close()
        break
    else:
        sock.sendto(msg.encode(), (udp_host, udp_port))
        resp = sock.recv(1024)
        print(resp.decode('utf-8'))
        msg2 = input("\nOpção 2: ")
        sock.sendto(msg2.encode(), (udp_host, udp_port))
        resp = sock.recv(1024)
        print(resp.decode('utf-8'))