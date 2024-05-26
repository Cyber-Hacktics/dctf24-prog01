import socket

def generate_fizz_buzz(n):
    fizz_buzz_list = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            fizz_buzz_list.append("DEADFACE")
        elif i % 3 == 0:
            fizz_buzz_list.append("DEAD")
        elif i % 5 == 0:
            fizz_buzz_list.append("FACE")
        else:
            fizz_buzz_list.append(i)
    return fizz_buzz_list

def send_fizz_buzz(fizz_buzz_list, host='localhost', port=33000):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    data = str(fizz_buzz_list)
    client_socket.send(data.encode())

    response = client_socket.recv(4096).decode()
    print("Server response:", response)

    client_socket.close()

if __name__ == "__main__":
    fizz_buzz_list = generate_fizz_buzz(100)  # You can adjust the range as needed
    send_fizz_buzz(fizz_buzz_list)
