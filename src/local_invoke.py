import os
import sys
import json
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from src.generate_horoscope.handler import handler
event = {
    "Details": {
        "Parameters": {
            "sign": "Aries",
            "question": "Should I change jobs?"
        }
    }
}
response = handler(event, {})
print(json.dumps(response, indent=2))