import psutil
import socket
import requests

class SystemMonitor:
    def __init__(self):
        pass

    @staticmethod
    def check_disk_usage():
        disk_usage = psutil.disk_usage('/')
        return disk_usage.percent > 20

    @staticmethod
    def check_cpu_utilization():
        cpu_utilization = psutil.cpu_percent()
        return cpu_utilization < 75

    @staticmethod
    def check_localhost():
        try:
            socket.create_connection(("localhost", 80), timeout=1)
            return True
        except (socket.error, ConnectionError):
            return False

    @staticmethod
    def check_internet_access():
        try:
            requests.get("http://www.google.com", timeout=1)
            return True
        except requests.ConnectionError:
            return False

def main():
    system_monitor = SystemMonitor()

    disk_check = system_monitor.check_disk_usage()
    cpu_check = system_monitor.check_cpu_utilization()
    localhost_check = system_monitor.check_localhost()
    internet_check = system_monitor.check_internet_access()

    if not (disk_check and cpu_check):
        print("ERROR! Disk usage or CPU usage failed.")
    elif not (localhost_check and internet_check):
        print("Network checks failed. Localhost or internet access is not operational.")
    else:
        print("Everything is OK.")

# Test Case
def test_system_monitor():
    system_monitor = SystemMonitor()

    assert system_monitor.check_disk_usage() == True  # Assuming disk usage is always above 20%
    assert system_monitor.check_cpu_utilization() == True  # Assuming CPU utilization is always below 75%
    assert system_monitor.check_localhost() == True  # Assuming localhost is always reachable
    assert system_monitor.check_internet_access() == True  # Assuming internet access is always available

if __name__ == "__main__":
    main()
    test_system_monitor()
