import time
import json
from datetime import datetime
from collections import defaultdict

# Simulated data: failed login attempts from users
failed_login_attempts = [
    {"username": "user1", "ip": "192.168.1.10", "timestamp": time.time()},
    {"username": "user1", "ip": "192.168.1.10", "timestamp": time.time() + 10},
    {"username": "user1", "ip": "192.168.1.10", "timestamp": time.time() + 20},
]

# Parameters
ALERT_THRESHOLD = 3  # number of failed attempts before an alert
TIME_WINDOW = 60     # seconds

# Initialize data structure to store alerts
alerts = defaultdict(list)

def detect_and_respond():
    for attempt in failed_login_attempts:
        username = attempt["username"]
        timestamp = attempt["timestamp"]
        
        # Record attempt for the username
        alerts[username].append(timestamp)
        
        # Filter attempts within the TIME_WINDOW
        recent_attempts = [t for t in alerts[username] if timestamp - t <= TIME_WINDOW]
        alerts[username] = recent_attempts
        
        # Trigger alert if threshold is met
        if len(recent_attempts) >= ALERT_THRESHOLD:
            generate_alert(username, recent_attempts)

def generate_alert(username, timestamps):
    # Log alert with a basic incident report
    alert = {
        "incident_time": datetime.now().isoformat(),
        "username": username,
        "attempts": len(timestamps),
        "timestamps": [datetime.fromtimestamp(t).isoformat() for t in timestamps],
        "action_taken": "Account locked for 15 minutes"
    }
    
    print(f"ALERT: Suspicious activity detected for {username}")
    with open("incident_report.json", "w") as file:
        json.dump(alert, file, indent=4)
    print("Incident report generated:", alert)

# Run the detection and response function
detect_and_respond()
