exemplo = "10.0.0.1->192.168.1.1 10.0.0.2->192.168.1.1 10.0.0.1->192.168.1.1 192.168.1.1->10.0.0.1"
logs = exemplo.split()
contagem = {}
for log in logs:
    origem, destino = log.split('->')
    if destino in contagem:
        contagem[destino] += 1
    else:
        contagem[destino] = 1
servidor = max(contagem, key=contagem.get)
print(f'O servidor que mais recebeu foi {servidor} com {contagem[servidor]} conexões.')
