import pandas as pd
from backtester import BackTester
from main import process_data, strat

# =====================================================
# Load Data
# =====================================================

raw_data = pd.read_csv("BTC_2019_2023_1d.csv")

# =====================================================
# Parameter Grid
# =====================================================

ATR_VALUES = [1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0]

ENTRY_WINDOWS = [10, 15, 20, 25, 30, 35, 40]

EXIT_WINDOWS = [5, 10, 15, 20]

results = []

total_runs = len(ATR_VALUES) * len(ENTRY_WINDOWS) * len(EXIT_WINDOWS)
run = 1

# =====================================================
# Grid Search
# =====================================================

for atr in ATR_VALUES:

    for entry in ENTRY_WINDOWS:

        for exit_ in EXIT_WINDOWS:

            print(f"[{run}/{total_runs}] ATR={atr} ENTRY={entry} EXIT={exit_}")

            run += 1

            try:

                processed = process_data(
                    raw_data.copy(),
                    entry_window=entry,
                    exit_window=exit_
                )

                signals = strat(
                    processed,
                    atr_multiplier=atr
                )

                signals.to_csv("final_data.csv", index=False)

                bt = BackTester(
                    "BTC",
                    signal_data_path="final_data.csv",
                    master_file_path="final_data.csv",
                    compound_flag=1
                )

                bt.get_trades(1000)

                stats = bt.get_statistics()

                results.append({

                    "ATR": atr,
                    "Entry_Window": entry,
                    "Exit_Window": exit_,
                    "Sharpe": stats.get("Sharpe Ratio", 0),
                    "Net_Profit": stats.get("Net Profit", 0),
                    "Drawdown": stats.get("Maximum Drawdown(%)", 999),
                    "Trades": stats.get("Total Trades", 0),
                    "WinRate": stats.get("Win Rate", 0)

                })

            except Exception as e:

                print("FAILED:", e)

# =====================================================
# Save Results
# =====================================================

results = pd.DataFrame(results)

results = results.sort_values(
    by=["Sharpe", "Net_Profit"],
    ascending=False
)

results.to_csv("results.csv", index=False)

print("\n")
print("=" * 70)
print("TOP 10 STRATEGIES")
print("=" * 70)

print(results.head(10))
