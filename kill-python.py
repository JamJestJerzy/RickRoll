import subprocess
import os
import time

# Pobierz PID bieżącego procesu
current_pid = os.getpid()

# Zatrzymaj wszystkie procesy uruchomione przez Python, z wyjątkiem bieżącego procesu
subprocess.call(["pkill", "-f", "python", "^-[0-9]+$", "!" + str(current_pid)])

# Poczekaj 1 minutę
time.sleep(60)

# Wznów wszystkie procesy uruchomione przez Python, z wyjątkiem bieżącego procesu
subprocess.call(["pgrep", "-f", "python", "^-[0-9]+$", "!" + str(current_pid)])
