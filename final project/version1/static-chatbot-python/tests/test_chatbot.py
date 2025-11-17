import unittest
from src.chatbot import Chatbot

class TestChatbot(unittest.TestCase):
    def setUp(self):
        self.chatbot = Chatbot('data/keyword_commandsfianl.csv')

    def test_fetch_commands_valid_keyword(self):
        response = self.chatbot.fetch_commands('get')
        self.assertIn('oc get pv', response)
        self.assertIn('oc get pods', response)

    def test_fetch_commands_invalid_keyword(self):
        response = self.chatbot.fetch_commands('invalid_keyword')
        self.assertEqual(response, "No commands found for the given keyword.")

    def test_fetch_commands_empty_keyword(self):
        response = self.chatbot.fetch_commands('')
        self.assertEqual(response, "No commands found for the given keyword.")

if __name__ == '__main__':
    unittest.main()