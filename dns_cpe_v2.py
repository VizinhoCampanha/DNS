#!/usr/bin/python3

from collections import Counter
import requests
import re
import ipaddress
import json


def clear_list(file_path):
    lista_dados = []
    with open(file_path) as cpe:
        for dados in cpe:
            dados = dados.split(':')[-1].replace('"', '').replace(
                '[', '').replace(']', '').replace("\n", "").split(',')
            for dns in dados:
                ip = dns.strip().split('.')
                if len(ip) == 4:
                    new_ip = '{}.{}.{}.{}'.format(
                        int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3]))
                    lista_dados.append(new_ip)
    return lista_dados


def dns_count(path):
    dns_sumarizado = Counter(clear_list(path))
    return dns_sumarizado


def dns_count_total(path):
    dns_total = len(dns_count(path))
    return dns_total


def minemeld_download(url_path):
    ip = []
    response = requests.get(url_path, verify=False)
    for dados in response.text.splitlines():
        if re.search("^[0-9]{1,3}.*[0-9]{1,3}$", dados):
            ip.append(dados)
    return ip


def mask(ip1, ip2):
    for rede in ipaddress.summarize_address_range(ipaddress.IPv4Address(ip1),
                                                  ipaddress.IPv4Address(ip2)):
        return str(rede)


def mask_mount(url_path):
    miners = minemeld_download(url_path)
    list_rede = []
    for dados in miners:
        x = dados.split('-')
        list_rede.append(mask(x[0], x[1]))
    return list_rede


def validation(path, url_path):
    dns = list(dns_count(path))
    l_rede = mask_mount(url_path)
    for dados in dns:
        for rede in l_rede:
            if ipaddress.ip_address(dados) in ipaddress.ip_network(rede):
                print(dados)
                break


def virus_total(path, url_path):
#    lista_ip = list(dns_count(path))
    lista_ip = list(dns_count(path))[701:]
    lista_output = []
    for ip in lista_ip:
        url_2 = f'{url_path}{ip}'
        response = requests.get(url_2, verify=False)
        json_obj = json.loads(response.text)
        json_out = json_obj['data'][0]['attributes']['last_analysis_stats']
        json_out['IP'] = ip
        lista_output.append(json_out)
    # output = lista_output
    # output = []
    for i in lista_output:
        if i['malicious'] != 0:
            # output.append(i['IP'] + ', malicious, ' + str(i['malicious']))
            print(i['IP'] + ',malicious,' + str(i['malicious']))
    # return output
