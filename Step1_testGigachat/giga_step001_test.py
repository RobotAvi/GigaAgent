import unittest
from giga_test001 import llm

class TestGigaChat(unittest.TestCase):
    def test_basic_response(self):
        """Test that we get a non-empty response"""
        response = llm.invoke("Привет, как дела?")
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.content)
        self.assertTrue(len(response.content) > 0)

    def test_question_answer(self):
        """Test that we get a meaningful answer to a question"""
        response = llm.invoke("Что такое Python?")
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.content)
        self.assertTrue(len(response.content) > 10)  # Ответ должен быть достаточно длинным
        self.assertTrue("python" in response.content.lower() or "питон" in response.content.lower())

if __name__ == '__main__':
    unittest.main() 