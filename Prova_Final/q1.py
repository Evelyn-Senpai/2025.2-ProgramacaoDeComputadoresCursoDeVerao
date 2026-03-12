import socket
rede = socket.gethostbyname_ex(socket.getfqdn()) # ('cnat457271.mshome.net', [], ['172.17.80.1'])
for ipv4 in rede[2]:
    octetol = int(ipv4.split('.')[0])
    if 128 <= octetol <= 191:
        print(f'{octetol} - endereço classe B')
    elif octetol <= 127:
        print(f'{ipv4}, - endereço classe A')
    elif octetol <= 224:
        print(f'{ipv4}, - endereço classe C')
    else:
        print(f'{ipv4}, - outra classe')