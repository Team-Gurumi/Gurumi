from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
from encryption import encrypt

key = b'ThisIsA16ByteKey'  # 16 bytes key for AES

def encrypt(message: str) -> str:
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv + ":" + ct

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

def send_data(server_ip: str, server_port: int, message: str):
    encrypted_message = encrypt(message)  # 암호화된 데이터
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, server_port))
        s.sendall(encrypted_message.encode())
        response = s.recv(4096)
        print(f"서버 응답: {response.decode()}")