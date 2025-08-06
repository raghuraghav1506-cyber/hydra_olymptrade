import time
import random
from datetime import datetime, timedelta
from asset_fetcher import get_available_assets
from price_fetcher import get_live_price

# Config
TRADE_DURATION = 60  # seconds
START_BALANCE = 1000
TRADE_AMOUNT = 100

# State
balance = START_BALANCE
win_count = 0
loss_count = 0

def simulate_trade(asset, direction):
    entry_price = get_live_price(asset)
    if entry_price is None:
        print(f"[TRADE] Skipping {asset} due to missing price.")
        return None

    expiry_time = datetime.now() + timedelta(seconds=TRADE_DURATION)
    print(f"\n[TRADE] {asset} | {direction.upper()} | Entry: {entry_price} | Expiry: {expiry_time.strftime('%H:%M:%S')}")

    time.sleep(TRADE_DURATION)

    exit_price = get_live_price(asset)
    if exit_price is None:
        print(f"[TRADE] Skipping {asset} due to missing exit price.")
        return None

    result = "win" if (direction == "call" and exit_price > entry_price) or (direction == "put" and exit_price < entry_price) else "loss"

    return {
        "asset": asset,
        "direction": direction,
        "entry": entry_price,
        "exit": exit_price,
        "result": result,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def log_trade(trade):
    global balance, win_count, loss_count

    if trade["result"] == "win":
        balance += TRADE_AMOUNT
        win_count += 1
    else:
        balance -= TRADE_AMOUNT
        loss_count += 1

    print(f"[RESULT] {trade['result'].upper()} | Exit: {trade['exit']} | Balance: {balance}")
    print(f"[LOG] {trade['timestamp']} | {trade['asset']} | {trade['direction']} | {trade['entry']} → {trade['exit']} | {trade['result']}")

    with open("trade_log.txt", "a") as log_file:
        log_file.write(
            f"{trade['timestamp']} | {trade['asset']} | {trade['direction']} | Entry: {trade['entry']} | Exit: {trade['exit']} | Result: {trade['result']} | Balance: ₹{balance}\n"
        )

def main():
    assets = get_available_assets()
    if not assets:
        print("[Hydra] No assets fetched. Using fallback.")
        assets = ["EURUSD", "GBPUSD", "USDJPY"]

    for i in range(3):  # Simulate 3 trades
        asset = random.choice(assets)
        direction = random.choice(["call", "put"])
        trade = simulate_trade(asset, direction)
        if trade:
            log_trade(trade)
        time.sleep(5)  # cooldown

    print(f"\n[SUMMARY] Wins: {win_count} | Losses: {loss_count} | Final Balance: ₹{balance}")

if __name__ == "__main__":
    main()
