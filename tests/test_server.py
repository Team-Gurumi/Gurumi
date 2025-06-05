# tests/test_server.py
import unittest
from supply_node.server import start_server

class TestServer(unittest.TestCase):
    def test_server_connection(self):
        # 서버가 정상적으로 연결을 기다리는지 확인
        result = start_server("10.0.0.1", 12345)
        self.assertIsNone(result)  # 기본적으로 서버가 실행되면 None을 반환함

if __name__ == "__main__":
    unittest.main()
