from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
from encryption import decrypt

key = b'ThisIsA16ByteKey'  # 16 bytes key for AES

def decrypt(enc_message: str) -> str:
    iv, ct = enc_message.split(":")
    iv = base64.b64decode(iv)
    ct = base64.b64decode(ct)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode()

if __name__ == "__main__":
    encrypted = encrypt("비밀 메시지")
    print("암호화:", encrypted)
    decrypted = decrypt(encrypted)
    print("복호화:", decrypted)


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
                decrypted_data = decrypt(data.decode())  # 복호화된 데이터
                print(f"수신된 데이터: {decrypted_data}")
                response = "처리 완료"
                conn.sendall(response.encode())
