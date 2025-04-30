import socket
import json
import argparse
from threading import Thread
from game_manager import GameManager

class QuizServer:
    def __init__(self, category, port):
        self.game = GameManager(category)
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(('0.0.0.0', port))
        self.server_socket.listen(5)
        
    def handle_client(self, client_socket, address):
        try:
            data = client_socket.recv(1024).decode('utf-8')
            connect_msg = json.loads(data)
            
            player_name = connect_msg.get('player_name')
            player = self.game.add_player(player_name, client_socket)
            
            welcome_msg = {
                'type': 'welcome',
                'status': 'success',
                'message': f'Bem-vindo ao Quiz de {self.game.category}',
                'total_questions': self.game.total_questions
            }
            client_socket.send(json.dumps(welcome_msg).encode('utf-8'))
            
            while self.game.is_running():
                question = self.game.get_next_question(player)
                if not question:
                    break
                    
                client_socket.send(json.dumps(question).encode('utf-8'))
                
                answer_data = client_socket.recv(1024).decode('utf-8')
                answer_msg = json.loads(answer_data)
                
                feedback = self.game.process_answer(player, answer_msg)
                client_socket.send(json.dumps(feedback).encode('utf-8'))
                
            results = self.game.get_final_results(player)
            client_socket.send(json.dumps(results).encode('utf-8'))
            
        except Exception as e:
            print(f"Erro com cliente {address}: {e}")
        finally:
            client_socket.close()
            self.game.remove_player(player)
            
    def start(self):
        print(f"Servidor iniciado na porta {self.port} para o tema {self.game.category}")
        while True:
            client_socket, address = self.server_socket.accept()
            Thread(target=self.handle_client, args=(client_socket, address)).start()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--category", required=True, help="Categoria do quiz")
    parser.add_argument("--port", type=int, default=12345, help="Porta do servidor")
    args = parser.parse_args()
    
    server = QuizServer(args.category, args.port)
    server.start()