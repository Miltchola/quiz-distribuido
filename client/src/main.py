import socket
import json
import argparse

class QuizClient:
    def __init__(self, host, port, player_name):
        self.host = host
        self.port = port
        self.player_name = player_name
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def start(self):
        try:
            self.socket.connect((self.host, self.port))
            
            connect_msg = {
                'type': 'connect',
                'player_name': self.player_name,
                'version': '1.0'
            }
            self.socket.send(json.dumps(connect_msg).encode('utf-8'))
            
            welcome_data = self.socket.recv(1024).decode('utf-8')
            welcome_msg = json.loads(welcome_data)
            print(f"\n{welcome_msg.get('message')}")
            print(f"Total de perguntas: {welcome_msg.get('total_questions')}\n")
            
            while True:
                question_data = self.socket.recv(4096).decode('utf-8')
                question = json.loads(question_data)
                
                if question['type'] == 'question':
                    self.display_question(question)
                    answer = self.get_player_answer()
                    answer_msg = {
                        'type': 'answer',
                        'question_id': question['id'],
                        'answer': answer
                    }
                    self.socket.send(json.dumps(answer_msg).encode('utf-8'))
                    
                    feedback_data = self.socket.recv(1024).decode('utf-8')
                    feedback = json.loads(feedback_data)
                    self.display_feedback(feedback)
                    
                elif question['type'] == 'result':
                    self.display_results(question)
                    break
                    
        except Exception as e:
            print(f"Erro na conexão: {e}")
        finally:
            self.socket.close()
            
    def display_question(self, question):
        print(f"\nPergunta {question['id']}: {question['text']}")
        for key, value in question['options'].items():
            print(f"  {key}) {value}")
            
    def get_player_answer(self):
        while True:
            answer = input("Sua resposta (a/b/c): ").strip().lower()
            if answer in ['a', 'b', 'c']:
                return answer
            print("Por favor, digite a, b ou c")
            
    def display_feedback(self, feedback):
        if feedback['correct']:
            print("✅ Resposta correta!")
        else:
            print(f"❌ Resposta incorreta. A correta era: {feedback['correct_answer']}")
        print(f"Pontuação atual: {feedback['score']}\n")
        
    def display_results(self, results):
        print("\n=== RESULTADOS FINAIS ===")
        print(f"Pontuação total: {results['total_score']}")
        print(f"Respostas corretas: {results['correct_answers']}")
        print(f"Respostas erradas: {results['wrong_answers']}")
        
        print("\n🏆 Ranking:")
        for i, entry in enumerate(results['ranking'], 1):
            print(f"{i}. {entry['player']}: {entry['score']} pontos")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1", help="Endereço do servidor")
    parser.add_argument("--port", type=int, default=12345, help="Porta do servidor")
    parser.add_argument("--player", required=True, help="Nome do jogador")
    args = parser.parse_args()
    
    client = QuizClient(args.host, args.port, args.player)
    client.start()