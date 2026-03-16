import requests

def check_ip_reputation(ip):

    # Placeholder reputation check
    # (You can later connect to AbuseIPDB or VirusTotal)

    if ip.startswith("185.") or ip.startswith("45."):
        return {
            "ip": ip,
            "reputation": "suspicious",
            "confidence": "medium"
        }

    return {
        "ip": ip,
        "reputation": "unknown",
        "confidence": "low"
    }