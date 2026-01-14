import os
import re
import uuid
from datetime import datetime
from src.database import LogRecord

LOG_FILE_PATH = "real_time_logs.txt"

def parse_log_line(line):
    """
    Parses a raw log line into structured data.
    """
    # Regex to grab: Timestamp, Service, Severity, Message
    # Matches: "2025-01-14 12:00:00 [service-name] ERROR Message..."
    pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(.*?)\] (\w+) (.*)"
    match = re.match(pattern, line)
    
    if match:
        return {
            "timestamp": datetime.strptime(match.group(1), "%Y-%m-%d %H:%M:%S"),
            "service": match.group(2),
            "severity": match.group(3),
            "message": match.group(4).strip()
        }
    return None

def fetch_cloud_logs(db):
    """
    Reads the log file and ingests new errors into the database.
    """
    if not os.path.exists(LOG_FILE_PATH):
        return 0

    # Read the file
    with open(LOG_FILE_PATH, "r") as f:
        lines = f.readlines()

    # Only look at the last 20 lines (Simulating "tail -f")
    recent_lines = lines[-20:]
    count = 0

    for line in recent_lines:
        # Parse the text line into a dictionary
        parsed = parse_log_line(line)
        
        # FILTER: Only save Errors/Warnings (Ignore "INFO" logs)
        if parsed and parsed['severity'] in ['ERROR', 'CRITICAL', 'WARNING']:
            
            # Check if we already saved this exact log message (Prevent Duplicates)
            exists = db.query(LogRecord).filter(LogRecord.message == parsed['message']).first()
            
            if not exists:
                new_log = LogRecord(
                    log_id=str(uuid.uuid4())[:8],
                    timestamp=parsed['timestamp'],
                    service_name=parsed['service'],
                    severity=parsed['severity'],
                    message=parsed['message'],
                    is_resolved=False
                )
                db.add(new_log)
                count += 1
    
    db.commit()
    return count