Relatório do Projeto: Quiz Distribuído

Matéria: Sistemas Distribuídos e Programação Paralela
Docente: Edson Mota da Cruz
Discentes:Danilo Santana, Diego Perpétuo, Luccas Pino & Milton Kiefer

Este projeto consiste em uma aplicação distribuída de quiz com arquitetura cliente-servidor, onde múltiplos jogadores podem se conectar a servidores especializados em diferentes categorias de perguntas. O sistema foi desenvolvido com foco na interoperabilidade entre diferentes implementações.

Arquitetura do Sistema
Componentes Principais

Servidor (QuizServer)
   Gerencia as regras do jogo
  Controla o fluxo de perguntas e respostas
  Mantém a pontuação dos jogadores
  Fornece feedback e resultados finais

Cliente (QuizClient)
  Conecta-se ao servidor
  Exibe perguntas aos jogadores
  Coleta respostas e envia ao servidor
  Mostra feedback e resultados

GameManager
  Lógica central do jogo
  Gerencia jogadores e questões
  Calcula pontuações e rankings

Protocolo de Comunicação
O sistema utiliza um protocolo baseado em JSON sobre sockets TCP, com mensagens padronizadas para garantir interoperabilidade:

Mensagens do Cliente para o Servidor
connect: Inicia conexão com nome do jogador

answer: Envia resposta a uma pergunta

disconnect: Finaliza conexão

Mensagens do Servidor para o Cliente
welcome: Confirmação de conexão e informações iniciais

question: Envio de nova pergunta

feedback: Resposta sobre acerto/erro

result: Resultados finais do quiz

error: Mensagens de erro

COMO RODAR O CÓDIGO

PRIMEIRO PASSO:
Abra um terminal na pasta server/src e execute:

python main.py --category tecnologia --port 12345
(A categoria pode ser alterada nesse comando do código)

SEGUNDO PASSO:
Executar o Cliente (em outro terminal)
Abra um novo terminal na pasta client/src e execute:

python main.py --host 127.0.0.1 --port 12345 --player "Seu Nome"
(Substitua seu"Seu Nome" pelo nome do jogador)

exemplo: 

cd server/src
Escolha algum entre os temas:
python main.py --category tecnologia --port 12345
python main.py --category filmes --port 12345
python main.py --category jogos --port 12345

Crie um novo terminal:
cd client/src
python main.py --host 127.0.0.1 --port 12345 --player "Ed"

Requisitos
Python 3.x
Bibliotecas padrão (socket, json, threading)

Formato das Perguntas
As perguntas são armazenadas em arquivos JSON no formato:

 "text": "Qual diretor dirigiu 'Pulp Fiction' e 'Kill Bill'?",
    "options": {
      "a": "Martin Scorsese",
      "b": "Quentin Tarantino",
      "c": "Steven Spielberg"
    },
    "correct_answer": "b"


Interoperabilidade
O sistema foi projetado para permitir que:
  Clientes de diferentes equipes conectem-se a servidores de outras equipes
  Servidores de diferentes categorias operem de forma independente
  A comunicação ocorra através de um protocolo padronizado
