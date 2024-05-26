import socket
import ast

def check_fizz_buzz(fizz_buzz_list):
    for i, value in enumerate(fizz_buzz_list, start=1):
        if i % 3 == 0 and i % 5 == 0:
            expected_value = "DEADFACE"
        elif i % 3 == 0:
            expected_value = "DEAD"
        elif i % 5 == 0:
            expected_value = "FACE"
        else:
            expected_value = i

        if value != expected_value:
            return False
    return True

def start_server(host='0.0.0.0', port=33000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        
        data = client_socket.recv(4096).decode()
        fizz_buzz_list = ast.literal_eval(data)
        
        if check_fizz_buzz(fizz_buzz_list):
            response = "Correct FizzBuzz"
        else:
            response = "Incorrect FizzBuzz"

        client_socket.send(response.encode())
        client_socket.close()

if __name__ == "__main__":
    start_server()
