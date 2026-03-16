from backend.utils.ioc_extractor import extract_iocs
from backend.agents.threat_intel_agent import check_ip_reputation
from backend.ai.nova_client import analyze_security_event


def autonomous_investigation(log_content):

    investigation_steps = []

    # Step 1 — IOC Extraction
    iocs = extract_iocs(log_content)

    investigation_steps.append({
        "agent": "IOC Agent",
        "action": "Extracted indicators",
        "result": iocs
    })

    # Step 2 — Threat Intelligence
    ip_results = []

    for ip in iocs.get("ips", []):
        try:
            reputation = check_ip_reputation(ip)
        except Exception:
            reputation = {"status": "lookup_failed"}

        ip_results.append({
            "ip": ip,
            "reputation": reputation
        })

    investigation_steps.append({
        "agent": "Threat Intelligence Agent",
        "action": "Checked IP reputation",
        "result": ip_results
    })

    # Step 3 — AI Investigation
    try:
        ai_analysis = analyze_security_event(iocs)
    except Exception:
        ai_analysis = "Possible suspicious activity detected"

    investigation_steps.append({
        "agent": "AI Investigation Agent",
        "action": "Analyzed attack behavior",
        "result": ai_analysis
    })

    # Summary message
    if iocs.get("ips"):
        summary = "⚠️ Suspicious network activity detected"
    else:
        summary = " No major indicators detected"

    return {
        "summary": summary,
        "final_assessment": ai_analysis,
        "investigation_steps": investigation_steps
    }