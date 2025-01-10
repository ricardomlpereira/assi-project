import threading
import socket
import json
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTP Server class to handle GET and POST requests with path handling
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Check the path and respond accordingly
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"GET request received at the root path")
        elif self.path == "/path":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"GET request received at /path")
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"404 Not Found")

    def do_POST(self):
        # Check the path for POST requests and handle accordingly
        if self.path == "/":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            response_data = {
                "message": "POST request received at the root path",
                "data": post_data.decode()
            }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()  
            self.wfile.write(json.dumps(response_data).encode())
        elif self.path == "/data":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            response_data = {
                "message": "POST request received at /data",
                "data": post_data.decode()
            }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"404 Not Found")

import socket
import base64

def tcp_server():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind(('0.0.0.0', 8081))
    tcp_socket.listen(5)
    print("TCP server listening on port 8081...")
    
    while True:
        try:
            client_socket, client_address = tcp_socket.accept()
            print(f"TCP connection from {client_address}")
            data = client_socket.recv(1024)
            if data:
                print("Attempting to decode TCP data:")
                try:
                    # Attempt UTF-8 decoding
                    decoded_utf8 = data.decode('utf-8')
                    print(f"UTF-8 Decoded Data: {decoded_utf8}")
                except UnicodeDecodeError:
                    print("UTF-8 decoding failed.")
                
                try:
                    # Decode as hexadecimal
                    decoded_hex = data.hex()
                    print(f"Hexadecimal Data: {decoded_hex}")
                except Exception as e:
                    print(f"Hexadecimal decoding failed: {e}")
                
                try:
                    # Decode as Base64
                    decoded_base64 = base64.b64encode(data).decode('utf-8')
                    print(f"Base64 Encoded Data: {decoded_base64}")
                except Exception as e:
                    print(f"Base64 encoding failed: {e}")
                
                # Always log raw binary data
                print(f"Raw Binary Data: {data}")
                
                # Send a response back to the client
                client_socket.sendall(b"TCP data received")
        except Exception as e:
            print(f"Error handling TCP connection: {e}")
        finally:
            client_socket.close()


import socket

import base64

def udp_server():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('0.0.0.0', 8082))
    print("UDP server listening on port 8082...")
    
    while True:
        data, client_address = udp_socket.recvfrom(1024)
        print(f"UDP connection from {client_address}")
        if data:
            try:
                # Attempt UTF-8 decoding
                decoded_data = data.decode('utf-8')
                print(f"Received UDP data (UTF-8): {decoded_data}")
            except UnicodeDecodeError:
                print("Failed to decode as UTF-8. Attempting other formats...")
                try:
                    # Attempt decoding as hexadecimal
                    decoded_data = data.hex()
                    print(f"Received UDP data (hex): {decoded_data}")
                except Exception as e:
                    print(f"Failed to decode as hex: {e}")
                
                try:
                    # Attempt decoding as base64
                    decoded_data = base64.b64encode(data).decode('utf-8')
                    print(f"Received UDP data (base64): {decoded_data}")
                except Exception as e:
                    print(f"Failed to decode as base64: {e}")
                
                # Fallback to raw binary output
                print(f"Received raw UDP data: {data}")
            
            udp_socket.sendto(b"UDP data received", client_address)


def start_http_server():
    http_server = HTTPServer(('0.0.0.0', 8080), SimpleHTTPRequestHandler)
    print("HTTP server listening on port 8080...")
    http_server.serve_forever()

def keepalive_logger():
    while True:
        time.sleep(30)  # Send message every 10 seconds
        print("[INFO] keepalive")

# Create and start the servers in separate threads
def run_servers():
    threading.Thread(target=start_http_server, daemon=True).start()
    threading.Thread(target=tcp_server, daemon=True).start()
    threading.Thread(target=udp_server, daemon=True).start()
    threading.Thread(target=keepalive_logger, daemon=True).start()

if __name__ == "__main__":
    run_servers()
    
    # Keep the main thread running to keep the servers alive
    input("Servers are running. Press Enter to exit...\n")
