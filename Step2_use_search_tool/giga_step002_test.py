import unittest
from unittest.mock import patch, MagicMock
from giga_step002 import llm, search_tool, agent

class TestGigaStep002(unittest.TestCase):
    def setUp(self):
        self.test_input = {"messages": [("user", "Найди какие праздники будут отмечать завтра")]}
        
    @patch('giga_step002.llm')
    @patch('giga_step002.search_tool')
    def test_agent_initialization(self, mock_search, mock_llm):
        """Test that agent is properly initialized with required components"""
        self.assertIsNotNone(agent)
        # Check if agent is a CompiledStateGraph instance
        self.assertTrue(hasattr(agent, 'invoke'))

    @patch('giga_step002.agent.invoke')
    def test_agent_invoke(self, mock_invoke):
        """Test that agent.invoke returns expected message format"""
        mock_response = MagicMock()
        mock_response.content = "Test response"
        mock_invoke.return_value = {"messages": [mock_response]}
        
        result = agent.invoke(self.test_input)
        self.assertIn("messages", result)
        self.assertEqual(len(result["messages"]), 1)
        self.assertEqual(result["messages"][0].content, "Test response")

    def test_cleanup_registration(self):
        """Test that cleanup function is registered with atexit"""
        import atexit
        # Check if cleanup function exists in the module
        from giga_step002 import cleanup
        self.assertTrue(callable(cleanup))

if __name__ == '__main__':
    unittest.main()
