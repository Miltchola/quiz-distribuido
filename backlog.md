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