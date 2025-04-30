import json
import random
from question_loader import load_questions

class GameManager:
    def __init__(self, category):
        self.category = category
        self.questions = load_questions(category)
        self.total_questions = len(self.questions)
        self.players = {}
        self.current_questions = {}
        
    def add_player(self, player_name, socket):
        player_id = len(self.players) + 1
        player = {
            'id': player_id,
            'name': player_name,
            'socket': socket,
            'score': 0,
            'current_question': 0,
            'answered': 0
        }
        self.players[player_id] = player
        return player
        
    def remove_player(self, player):
        if player['id'] in self.players:
            del self.players[player['id']]
            
    def is_running(self):
        return len(self.players) > 0
        
    def get_next_question(self, player):
        if player['answered'] >= self.total_questions:
            return None
            
        question = self.questions[player['answered']]
        player['current_question'] = player['answered']
        player['answered'] += 1
        
        return {
            'type': 'question',
            'id': question['id'],
            'text': question['text'],
            'options': question['options'],
            'time_limit': 30
        }
        
    def process_answer(self, player, answer_msg):
        question_id = answer_msg['question_id']
        question = self.questions[player['current_question']]
        
        correct = answer_msg['answer'].lower() == question['correct_answer'].lower()
        if correct:
            player['score'] += 1
            
        return {
            'type': 'feedback',
            'correct': correct,
            'score': player['score'],
            'correct_answer': question['correct_answer'],
            'next_question_in': 5
        }
        
    def get_final_results(self, player):
        sorted_players = sorted(self.players.values(), key=lambda x: x['score'], reverse=True)
        
        return {
            'type': 'result',
            'total_score': player['score'],
            'correct_answers': player['score'],
            'wrong_answers': self.total_questions - player['score'],
            'ranking': [{'player': p['name'], 'score': p['score']} for p in sorted_players]
        }