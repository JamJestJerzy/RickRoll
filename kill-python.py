import subprocess
import time

# Zatrzymaj wszystkie procesy uruchomione przez Python
subprocess.call(["pkill", "-f", "python"])

# Poczekaj 1 minutę
time.sleep(60)

# Wznów wszystkie procesy uruchomione przez Python
subprocess.call(["pgrep", "-f", "python"])
