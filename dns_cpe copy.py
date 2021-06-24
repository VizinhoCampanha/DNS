#!/usr/bin/python3

lista_DNS = open(
    "/mnt/c/Users/r333369/OneDrive - Telefonica/CYBER/DNS/Total_DNS.csv")
dados = lista_DNS.read()
lista_DNS.close()
lista_campos = []

for campos in dados.splitlines():
    valor = lista_campos.append(campos.split(';')[4].split(
        ':')[-1].replace('"', '').replace('[', '').replace(']', ''))
    valor = valor.split(',')

# set_dns = set(lista_campos)
# dict_dns = {}
# for ip in set_dns:
#     dict_dns[ip] = lista_campos.count(ip)


print(valor)
