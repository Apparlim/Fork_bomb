#!/usr/bin/env python3

import psutil, os, time, signal, logging, sys

# -------- thresholds --------
CPU_THRESHOLD      = 95      
PROC_THRESHOLD     = 500     
CHECK_INTERVAL_SEC = 2      
# ----------------------------
logging.basicConfig(filename="alerts.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(message)s")

def kill_forkbomb():
    """Kill all bash or sh processes except our own shell/python."""
    this_pid = os.getpid()
    killed   = 0
    for p in psutil.process_iter(['pid','name']):
        try:
            if p.info['pid'] != this_pid and p.info['name'] in ('bash','sh'):
                os.kill(p.info['pid'], signal.SIGKILL)
                killed += 1
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    logging.info(f"Mitigation triggered – killed {killed} bash/sh processes")
    print(f"[+] Mitigation complete – killed {killed} bash/sh processes")

def main():
    print("Monitoring system for fork-bomb attack… (Ctrl-C to stop)")
    while True:
        cpu   = psutil.cpu_percent(interval=1) 
        procs = len(psutil.pids())

        if cpu > CPU_THRESHOLD or procs > PROC_THRESHOLD:
            alert = f"ALERT – CPU {cpu:.1f}%  ProcCnt {procs}"
            logging.info(alert)
            print(f"[!] {alert}")

            kill_forkbomb()
         

        time.sleep(CHECK_INTERVAL_SEC)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\nStopped IDS.")
