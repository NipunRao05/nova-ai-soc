def map_to_mitre(iocs, log_content):

    techniques = []

    if "powershell" in log_content.lower():
        techniques.append({
            "id": "T1059",
            "name": "Command and Scripting Interpreter",
            "reason": "PowerShell execution detected"
        })

    if len(iocs.get("ips", [])) > 0:
        techniques.append({
            "id": "T1071",
            "name": "Application Layer Protocol",
            "reason": "Suspicious outbound network connection"
        })

    if "reg add" in log_content.lower():
        techniques.append({
            "id": "T1547",
            "name": "Boot or Logon Autostart Execution",
            "reason": "Registry persistence command detected"
        })

    return techniques