#!/usr/bin/python3

import requests
import json

url = "https://www.virustotal.com/ui/search?relationships%5Bcomment%5D=author%2Citem&relationships%5Burl%5D=network_location%2Clast_serving_ip_address&limit=20&query="


def virus_total(url_path):
    lista_ip = ['198.23.194.210', '69.162.107.66', '216.146.35.35']
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

# print(virus_total(url))
virus_total(url)