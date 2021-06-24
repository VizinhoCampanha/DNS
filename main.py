#!/usr/bin/python3
#Teste mudança GIT

import dns_cpe_v2

list_dns = "/mnt/c/Users/r333369/OneDrive - Telefonica/CYBER/DNS/Docs/Total_DNS.csv"
url_mine = 'https://10.11.178.136/feeds/CSOC_SIEM'
url_virus = "https://www.virustotal.com/ui/search?relationships%5Bcomment%5D=author%2Citem&relationships%5Burl%5D=network_location%2Clast_serving_ip_address&limit=20&query="

# print(len(dns_cpe_v2.clear_list(list_dns)))
# print(dns_cpe_v2.clear_list(list_dns))
# print(list(dns_cpe_v2.dns_count(list_dns))[1:6])
# print(dns_cpe_v2.dns_count(list_dns))
# print(dns_cpe_v2.dns_count_total(list_dns))
# print(dns_cpe_v2.minemeld_download(url))
# print(dns_cpe_v2.mask_mount(url))
# dns_cpe_v2.validation(list_dns, url)
# print(dns_cpe_v2.virus_total(list_dns, url_virus))
dns_cpe_v2.virus_total(list_dns, url_virus)
