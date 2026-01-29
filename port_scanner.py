import socket

# Configurações
alvo = "bancocn.com"
ports = [21, 22, 23, 25, 53, 80, 443, 445, 3306, 3389, 5900, 8080, 8443]
timeout = 0.3

print(f"[+] Iniciando port scan em: {alvo}\n")

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(timeout)

    resultado = client.connect_ex((alvo, port))

    if resultado == 0:
        print(f"[+] Porta {port} ABERTA")
    else:
        print(f"[-] Porta {port} fechada")

    client.close()
