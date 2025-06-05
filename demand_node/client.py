import socket

def send_data(server_ip: str, server_port: int, message: str):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, server_port))
        s.sendall(message.encode())
        response = s.recv(4096)
        print(f"서버 응답: {response.decode()}")

if __name__ == "__main__":
    send_data("10.0.0.1", 12345, "안녕하세요, 수요 노드입니다!")