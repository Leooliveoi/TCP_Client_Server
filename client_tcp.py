import socket
try:
    # SOCK STEAM == TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1) #Timeout de 1 segundo
    #Conectar ao servidor
    #PAssando uma tupla onde o 1º é uma tupla em 2º a Porta
    client.connect(("google.com", 80))
    # Enviar Informações
    # Espera como argumento bites b ou .encode
    # HTTP 1.1 e 2.0 Possuem requisitos diferentes
    client.send(b"GET / HTTP/1.1 \nHost: www.google.com\n\n\n")

    # Receber resposta
    # Argumanto a quantidade de bite que queremos receber
    pacotes_recv = client.recv(10048).decode()

    print(pacotes_recv)


    '''Uasando o netcar por exemplo se torna possivel fazer essa conexão'''
except:
    print("Erro!")

