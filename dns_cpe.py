#!/usr/bin/python3

lista_DNS = open(
    "/mnt/c/Users/r333369/OneDrive - Telefonica/CYBER/DNS/Total_DNS.csv").read()
lista_total_dns = []
dicionario_dns = {}

for dns in lista_DNS.splitlines():
    valor = dns.split(':')[-1].replace('"',
                                       '').replace('[', '').replace(']', '')
    valor = valor.split(',')
    for i in valor:
        lista_total_dns.append(i)


for count in lista_total_dns:
    ip = count.strip().split('.')
    if len(ip) == 4:
        novo_ip = '{}.{}.{}.{}'.format(
            int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3]))
    if dicionario_dns.get(novo_ip):
        dicionario_dns[novo_ip] += 1
    else:
        dicionario_dns[novo_ip] = 1


total_dns = len(lista_total_dns)
print(dicionario_dns)
