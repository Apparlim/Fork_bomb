
![Screenshot 2025-04-29 192547](https://github.com/user-attachments/assets/99934a38-1e8c-4064-aeb9-e72da1b00f6f)

# Fork Bomb Slayer – IDS Powered by Python

Welcome to **Fork Bomb Slayer**, where we simulate chaos and counter it like Guts from Berserk. This showcase how a bash fork bomb attack can be detected and stopped in real time using a Python-based Intrusion Detection and Prevention System (IDPS).

## 🔧 What’s Inside:
- `fork_bomb.sh`: Bash script that launches an infinite number of processes to simulate a DoS attack.
- `ids_forkbomb.py`: Python script that monitors your system’s CPU and process count, kills rogue processes, and logs alerts.
- `alerts.log`: Automatically generated log file storing CPU spikes and excessive process warnings.

##  How to Use:
⚠️ Do all of this inside a **virtual machine** – never on your main PC.

Open two terminal windows and run:

### Terminal 1:
```bash
python3 ids_forkbomb.py
```

### Terminal 2:
```bash
bash fork_bomb.sh
```

Watch your Python guardian monitor CPU and process count. If processes exceed 500 or CPU hits 95%+, it kicks in with real-time alerts and terminates the attack.

##  Sample Output (`alerts.log`):
```
[2025-04-29 02:01:44.898503] ALERT: High CPU usage detected: 94.1%
[2025-04-29 02:01:44.898880] ALERT: High process count detected: 5920
[2025-04-29 03:52:11.234247] ALERT: High process count detected: 6354
```

##  Why This Project?
Because defending systems should be just as thrilling as attacking them. This is a lightweight, real-time, host-based defense system that gives beginners and learners a hands-on way to understand CPU exhaustion attacks.

> "You should enjoy the little detours. Sometimes they’re the most important part of the journey." – Guts 🗡️


