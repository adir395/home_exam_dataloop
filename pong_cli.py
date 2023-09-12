import requests
import sys

def send_command_to_server(server_url, command, data=None):
    try:
        if data:
            response = requests.post(server_url + command, json=data)
        else:
            response = requests.post(server_url + command)

        print(response.json())  # Print the entire response JSON
    except requests.RequestException:
        print(f"Failed to send {command} command to {server_url}")


def main():
    if len(sys.argv) < 2:
        print("Please provide a valid command.")
        return

    command = sys.argv[1]

    if command == "start":
        pong_time_ms = int(sys.argv[2])
        # You'll need to modify the URLs based on your server setup
        send_command_to_server("http://localhost:8000", f"/start/http://localhost:8001/{pong_time_ms}")
    elif command == "pause":
        send_command_to_server("http://localhost:8000", "/pause")
    elif command == "resume":
        send_command_to_server("http://localhost:8000", "/resume")
    elif command == "stop":
        send_command_to_server("http://localhost:8000", "/stop")

if __name__ == "__main__":
    main()