import uuid
import random
from datetime import datetime, timedelta
from faker import Faker
from sqlalchemy.orm import Session
from src.database import LogRecord

fake = Faker()

# Pre-defined "Real" DevOps Errors
ERROR_SCENARIOS = [
    {
        "service": "aws-lambda-payment",
        "severity": "ERROR",
        "msg": "Runtime.ImportModuleError: Unable to import module 'app': No module named 'requests'"
    },
    {
        "service": "rds-postgres-primary",
        "severity": "CRITICAL",
        "msg": "FATAL: remaining connection slots are reserved for non-replication superuser connections"
    },
    {
        "service": "k8s-ingress-nginx",
        "severity": "ERROR",
        "msg": "UpstreamTimedOut: upstream request timeout while connecting to upstream client: 10.244.0.12"
    },
    {
        "service": "auth-service-node",
        "severity": "WARNING",
        "msg": "TokenExpiredError: jwt expired at 2024-01-09T10:00:00.000Z"
    }
]

def fetch_cloud_logs(db: Session, count=3):
    """
    Simulates fetching logs from AWS CloudWatch/GCP.
    In a real app, you would replace this logic with `boto3.client('logs').get_log_events(...)`
    """
    new_logs = []
    
    for _ in range(count):
        scenario = random.choice(ERROR_SCENARIOS)
        
        # Check if we already have this fake log to avoid duplicates in demo
        unique_id = f"aws-log-{uuid.uuid4().hex[:8]}"
        
        log_entry = LogRecord(
            log_id=unique_id,
            timestamp=datetime.now() - timedelta(minutes=random.randint(1, 120)),
            service_name=scenario["service"],
            severity=scenario["severity"],
            message=scenario["msg"],
            is_resolved=False
        )
        
        db.add(log_entry)
        new_logs.append(log_entry)
    
    db.commit()
    return len(new_logs)