# tests/test_client.py
import unittest
from demand_node.client import send_data

class TestClient(unittest.TestCase):
    def test_send_data(self):
        # 서버가 정상적으로 응답을 받을 수 있는지 확인하는 테스트
        response = send_data("10.0.0.1", 12345, "Test Data")
        self.assertIn("처리 완료", response)

if __name__ == "__main__":
    unittest.main()
