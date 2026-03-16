from backend.ai.nova_client import analyze_security_event
from backend.utils.mitre_mapper import map_to_mitre


def investigate_incident(iocs, log_content):

    mitre = map_to_mitre(iocs, log_content)

    ai_report = analyze_security_event(iocs)

    return {
        "mitre_attack": mitre,
        "ai_analysis": ai_report
    }