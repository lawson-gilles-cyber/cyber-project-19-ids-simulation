# IDS Simulation

from core.ids_engine import analyze_traffic

# Load traffic logs
with open("data/traffic_logs.txt", "r") as file:
    logs = file.readlines()

print("=== IDS Analysis ===\n")

# Analyze traffic
for log in logs:
    log = log.strip()

    alert = analyze_traffic(log)

    if alert:
        print(alert)

        # Save alert
        with open("alerts/alerts.log", "a") as f:
            f.write(alert + "\n")
