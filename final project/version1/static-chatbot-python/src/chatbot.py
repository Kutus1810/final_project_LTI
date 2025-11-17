from flask import jsonify
import pandas as pd

class Chatbot:
    def __init__(self, csv_file):
        self.data = self.load_data(csv_file)

    def load_data(self, csv_file):
        return pd.read_csv(csv_file)

    def get_commands(self, query):
        keywords = self.data['Keyword'].tolist()
        commands = self.data['Commands'].tolist()
        
        for keyword, command in zip(keywords, commands):
            if keyword in query.lower():
                return command.split('\n')
        
        return ["Sorry, I couldn't find any commands for your query."]

# Example usage:
# chatbot = Chatbot('data/keyword_commandsfianl.csv')
# response = chatbot.get_commands('get pods')