import socket
import json
import struct

def generate_fizz_buzz(n):
    fizz_buzz_list = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 7 == 0:
            fizz_buzz_list.append("TURBOTACTICAL")
        elif i % 3 == 0:
            fizz_buzz_list.append("TURBO")
        elif i % 7 == 0:
            fizz_buzz_list.append("TACTICAL")
        else:
            fizz_buzz_list.append(i)
    return fizz_buzz_list

def connect_to_server(host='147.182.225.243', port=33002):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Receive the initial challenge message from the server
    challenge_message = client_socket.recv(4096).decode()
    print("Server Challenge:", challenge_message)

    # Generate the FizzBuzz list based on the challenge
    fizz_buzz_list = generate_fizz_buzz(500)

    # Convert list to JSON string
    data = json.dumps(fizz_buzz_list).encode()

    # Send the length of the data first (as 4-byte integer)
    data_len = struct.pack('>I', len(data))
    client_socket.sendall(data_len)

    # Send the actual FizzBuzz data
    client_socket.sendall(data)

    # Receive the server's response
    response = client_socket.recv(4096).decode()
    print("Server response:", response)

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    connect_to_server()
