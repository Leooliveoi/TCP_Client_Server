import socket

try:
    # Protocol UDP == SOCK_DGRAM
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("the target need to open a UDP port\n in netcat a '-lvup' argument")
    alvo = input("Who is a target?\n")
    porta = input("What the port to Connect?\n")
    while True:
        # Sendto == Connect + Send

        msg = input("Message: ") + "\n"
        client.sendto(msg.encode(), (alvo, int(porta)))
        data, sender = client.recvfrom(1024)
        print(sender[0]+":"+data.decode())
except Exception as e:
    print("Error! ", e)
