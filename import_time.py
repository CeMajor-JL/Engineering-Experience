import time
import hashlib
from pathlib import Path
from datetime import datetime

def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def watch(file_path: str, interval: float = 1.0):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(file_path)

    last_hash = file_hash(path)
    last_size = path.stat().st_size

    print(f"Watching: {path.resolve()}")
    print("Press Ctrl+C to stop\n")

    try:
        while True:
            time.sleep(interval)

            current_hash = file_hash(path)
            current_size = path.stat().st_size

            if current_hash != last_hash:
                diff = current_size - last_size
                ts = datetime.now().strftime("%H:%M:%S")

                print(f"[{ts}] Changed | Δsize: {diff:+} bytes")

                last_hash = current_hash
                last_size = current_size

    except KeyboardInterrupt:
        print("\nStopped.")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python file_watch.py <file> [interval]")
        exit(1)

    watch(
        sys.argv[1],
        float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
    )