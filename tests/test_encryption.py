# tests/test_encryption.py
import unittest
from demand_node.encryption import encrypt, decrypt

class TestEncryption(unittest.TestCase):
    def test_encryption_decryption(self):
        original = "비밀 메시지"
        encrypted = encrypt(original)
        decrypted = decrypt(encrypted)
        self.assertEqual(original, decrypted)  # 원본과 복호화된 데이터 비교

if __name__ == "__main__":
    unittest.main()
