import socket
rede = socket.gethostbyname_ex(socket.getfqdn()) # ('cnat457271.mshome.net', [], ['172.17.80.1'])
for ipv4 in rede[2]:
    octetol1 = int(ipv4.split('.')[0])
    octetol2 = int(ipv4.split('.')[1])
    if octetol1 == 10:
        print(f'{ipv4} -> classe A privado')
    elif octetol1 == 127:
        print(f'{ipv4} -> loopback')
    elif octetol1 == 169 and octetol2 == 254:
        print(f'{ipv4} -> APIPA privado')
    elif octetol1 == 172 and 16 <= octetol2 <= 31:
        print(f'{ipv4} -> classe B privado')
    elif octetol1 == 192 and octetol2 == 168:
        print(f'{ipv4} -> classe C privado')
    else:
        print(f'{ipv4}, -> endereço público')