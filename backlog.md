## BACKLOG

Portuguese:
Esse arquivo é responsável por trazer um retorno sobre algumas execuções e testes para relatar erros ou execuções com sucesso e seus resultados esperados.
Isso não é obrigatório, porém, para dar mais controle e compartilhar informações sobre o uso do projeto, esse arquivo pode ajudar a entender o comportamento do aplicativo.

English:
This file is responsible to give a return about some runnings and tests to report errors or successfully runnings and your expected results.
This is not obrigatory, but, to give more control and share more information about the use of the project, this file can help to understand the app's behaviour.

## REPORTS / RELATORIOS

Test 1:
- DRIVEN_BY: DANILO SANTANA GARCIA
- RESULT: Partial Success
- NOTES: "O programa apresentou uma primeira falha na tentativa de realizar uma conexão do cliente para o servidor hospedado, sendo este o seguinte erro: 'Erro com cliente ('127.0.0.1', 45628): Expecting value: line 1 column 1 (char 0)', porém, ao tentar realizar novamente, o servidor respondeu a conexão normalmente até um certo tempo, que apresentou o mesmo erro para o servidor, porém, para o cliente apresentou o seguinte erro: 'Erro com cliente ('127.0.0.1', 45628): Expecting value: line 1 column 1 (char 0)'
- NEXT_STEPS: Realizar mais testes persistentes para que se entenda o comportamento anômalo de perda de conexão com o servidor por parte do cliente (Atualmente, entende-se que esse erro se trata de um erro Extra Data)

Test 2:
- DRIVEN_BY: DANILO SANTANA GARCIA
- RESULT: Partial Success
- NOTES: Novamente, o programa apresentou a mesma situação que o teste 1, porém, o programa conseguiu conectar diretamente sem erros dessa vez, representando um avanço de conseguir conexão sem precisar tentar novamente a conexão, porém, está apresentando Extra data. O meu entendimento para esse erro seja que o servidor não tenha capacidade suportar 10 pontuações, já que o erro sempre se apresenta na passagem da resposta da pergunta 6.
- NEXT_STEPS: Realizar mais testes persistentes para que se entenda o comportamento anômalo de perda de conexão com o servidor por parte do cliente (Agora, há levantamento de hipóteses para o eventual erro que ocorre especificamente na pergunta 6)

Test 3:
- DRIVEN_BY: DANILO SANTANA GARCIA
- RESULT: Partial Success
- NOTES: Após 3 testes seguidos realizados, as suspeitas de que é suportado apenas a pontuação 5 se concretiza mais, o que é válida checar trechos do código que realizam os testes de lógica e armazenamento de pontuação que acabam fazendo o cliente retornar erro de Extra data (Dados extras). Para isso, recomendo que seja revisado o código dentro do arquivo "client/src/main.py" (especificamente as linhas 60-65 (função get_player_answer(self))) e o arquivo "server/src/game_manager.py" (talvez tenha alguma relação também com a "server/src/main.py")
- NEXT_STEPS: Com os testes realizados, quase testificando que de fato a aplicação não está suportando mais do que 5 pontos, revisar os códigos e realizar correções para que suporte até pontuação 10