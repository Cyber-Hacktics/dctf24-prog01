import socket
import json
import struct
import threading

def check_fizz_buzz(fizz_buzz_list, n=500):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 7 == 0:
            expected_value = "TURBOTACTICAL"
        elif i % 3 == 0:
            expected_value = "TURBO"
        elif i % 7 == 0:
            expected_value = "TACTICAL"
        else:
            expected_value = i

        if i-1 >= len(fizz_buzz_list) or fizz_buzz_list[i-1] != expected_value:
            return False
    return True

def receive_full_data(client_socket, size):
    buffer_size = 4096
    data = b""
    while len(data) < size:
        part = client_socket.recv(buffer_size)
        if not part:
            break
        data += part
    return data.decode()

def handle_client(client_socket, client_address):
    print(f"Connection from {client_address}")
    try:
        # Receive the first 4 bytes to get the length of the incoming data
        raw_msg_len = client_socket.recv(4)
        if not raw_msg_len:
            raise ValueError("No data received")
        msg_len = struct.unpack('>I', raw_msg_len)[0]

        # Now receive the full data based on the received length
        data = receive_full_data(client_socket, msg_len)

        # Use JSON to decode the received data
        fizz_buzz_list = json.loads(data)

        # Ensure the received data is a list
        if not isinstance(fizz_buzz_list, list):
            raise ValueError("Expected a list")

        if check_fizz_buzz(fizz_buzz_list):
            response = "Correct! Here's the flag: flag{c0d3_wh1z_f1zzbuzz}"
        else:
            response = "Incorrect FizzBuzz"

    except (ValueError, json.JSONDecodeError) as e:
        response = f"Error: Invalid data format -- {str(e)}"

    client_socket.send(response.encode())
    client_socket.close()

def start_server(host='0.0.0.0', port=33000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Listen for up to 5 concurrent connections
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        # Start a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    start_server()
