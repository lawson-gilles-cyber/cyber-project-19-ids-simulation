# IDS Detection Engine

def analyze_traffic(log):

    # Detect port scan (multiple ports)
    if "SCAN" in log:
        return "[IDS ALERT] Port scanning activity detected"

    # Detect brute force
    if "FAILED LOGIN" in log:
        return "[IDS ALERT] Possible brute force attack"

    # Detect suspicious IP
    if "45.33.32.1" in log:
        return "[IDS ALERT] Known suspicious IP detected"

    return None
