import re

IP_PATTERN = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
DOMAIN_PATTERN = r'\b(?:[a-zA-Z0-9-]+\.)+(com|net|org|io|ru|cn|co|info)\b'
HASH_PATTERN = r'\b[a-fA-F0-9]{32,64}\b'


def extract_iocs(text):

    ips = re.findall(IP_PATTERN, text)
    domains = re.findall(DOMAIN_PATTERN, text)
    hashes = re.findall(HASH_PATTERN, text)

    ips = list(set(ips))
    domains = list(set(domains))
    hashes = list(set(hashes))

    return {
        "ips": ips,
        "domains": domains,
        "hashes": hashes
    }