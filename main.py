import os

output_dir = "/output"
os.makedirs(output_dir, exist_ok=True)

entry_text = "Pump.fun Replay Sprint Paper Bot real ranking strategy: maximize PnL above cash baseline across final house window every fee survived bot holds earned place prize rolls over"

entry_path = os.path.join(output_dir, "entry.txt")
with open(entry_path, "w") as f:
    f.write(entry_text)