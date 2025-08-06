import time
from datetime import datetime

# Simulated signal
signal = {
    "asset": "EURUSD",
    "direction": "call",  # or "put"
    "entry_price": 1.1000,
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

print(f"[{signal['timestamp']}] Placing {signal['direction']} trade on {signal['asset']} at {signal['entry_price']}")

# Wait for expiry (e.g., 1 minute)
time.sleep(60)

# Simulate exit price
exit_price = 1.1012  # Replace with real price later

# Determine result
win = (signal["direction"] == "call" and exit_price > signal["entry_price"]) or \
      (signal["direction"] == "put" and exit_price < signal["entry_price"])

result = "WIN" if win else "LOSS"
print(f"Trade result: {result} | Exit price: {exit_price}")
