# demand_node/client_safe.py
import socket

def send_data_safe(server_ip: str, server_port: int, message: str):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_ip, server_port))
            s.sendall(message.encode())
            response = s.recv(4096)
            print(f"서버 응답: {response.decode()}")
    except ConnectionRefusedError:
        print("서버 연결 실패")
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    send_data_safe("10.0.0.1", 12345, "안전한 전송 테스트")
