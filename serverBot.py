import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_host = socket.gethostname()
udp_port = 12000
sock.bind((udp_host, udp_port))

i = 0

while True:
    
    data, addr = sock.recvfrom(1024)
    Data = data.decode()
    
    print(Data)

    if Data == "1" and i == 0:
        respo = "\nPara extrato das faturas tecle 1 \n Para valor fatura tecle 2 \n Para encerrar tecle 3"
        sock.sendto(respo.encode('utf-8'), addr)
        i = 1
        Data = "0"
    else:
        if Data == "2" and i == 0:
            respo = "\nPara extrato tecle 1 \n Para transferencia tecle 2 \n Para encerrar tecle 3"
            sock.sendto(respo.encode('utf-8'), addr)
            i = 2
            Data = "0"

    if Data == "1" and i == 1:
        respo = "\nSeu saldo é de R$1000,00"
        sock.sendto(respo.encode('utf-8'), addr)
        i = 0
        Data = "0"
    else:
        if Data == "2" and i == 1:
            respo = "Sua fatura é de R$ 600,57"
            sock.sendto(respo.encode('utf-8'), addr)
            i = 0
            Data = "0"
    
    if Data == "1" and i == 2:
        respo = "\nSeu saldo é de R$1000,00"
        sock.sendto(respo.encode('utf-8'), addr)
        i = 0
        Data = "0"
    else:
        if Data == "2" and i == 2:
            respo = "Não é possível tranferir no momento. Tente mais tarde!"
            sock.sendto(respo.encode('utf-8'), addr)
            i = 0
            Data = "0"