import socket
i = 0
while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_host = socket.gethostname()
    udp_port = 8080

    if i == 0:
        msga = "00"
        sock.sendto(msga.encode(), (udp_host, udp_port))
        resp = sock.recv(1024)
        print(resp.decode('utf-8'))
        msg = input(" Opção 1: ")
        i = 1

    if msg == "3":
        print("SAINDO...")
        sock.close()
        break

    elif msg != "1" and msg != "2" and msg != "3":
        print("ERRO!!! Código Inválido!")

    else:
        sock.sendto(msg.encode(), (udp_host, udp_port))
        resp = sock.recv(1024)
        print(resp.decode('utf-8'))
        msg2 = input(" Opção 2: ")
        sock.sendto(msg2.encode(), (udp_host, udp_port))
        resp = sock.recv(1024)
        print(resp.decode('utf-8'))
        i = 0