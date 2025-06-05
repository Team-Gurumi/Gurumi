import socket

def start_server(ip: str, port: int):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((ip, port))
        s.listen()
        print(f"공급 서버 대기 중: {ip}:{port}")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"연결됨: {addr}")
                data = conn.recv(4096)
                if not data:
                    break
                print(f"수신 데이터: {data.decode()}")
                response = "처리 완료"
                conn.sendall(response.encode())

if __name__ == "__main__":
    start_server("10.0.0.1", 12345)
