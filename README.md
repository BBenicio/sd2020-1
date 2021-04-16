# Repositório de notas com RPC

Trabalho Prático da disciplina Sistemas Distribuitos, 2020.1

Alunos: Bruno Benicio e Lucas Nunes

A proposta do trabalho é fazer um programa cliente/servidor usando RPC. A descrição completa do trabalho está no arquivo trabalho.pdf

Foi utilizada a biblioteca rpyc para realizar a conexão entre o cliente e o servidor. Mais detalhes sobre a biblioteca em https://rpyc.readthedocs.io/en/latest/

As validações feitas foram apenas para verificar se as notas são valores [0, 10] e para verificar se a matricula é um valor numérico

Para executar, basta iniciar o client.py e realizar a operação se baseando pelo menu de opções apresentado. 

Feito apenas para python3.
Testado no Linux e Windows 10 apenas.

## Servidor

Para a implementação do servidor utilizamos uma classe auxiliar para armazenar
as notas cadastradas em um arquivo JSON. Tendo isso, criamos então a
classe `MyService` que herda da classe `Service` da biblioteca, conforme
necessário para a criação de um servidor.

Na biblioteca usada, as funções que serão expostas ao cliente devem pertencer a
uma classe `Service` e ter como prefixo `exposed_`. Qualquer outra função não
será exposta ao cliente. Após definidas a classe e as funções que serão
expostas basta iniciar o servidor para ouvir em alguma porta para aguardar por
conexões de clientes.

Em todas as chamadas realizamos primeiramente algumas validações sobre os dados
passados pelo cliente, caso algum seja inválido será retornada uma mensagem de
erro descrevendo o que está inválido.

## Cliente

O cliente tenta se conectar ao servidor pela porta 12345. Após a conexão ser
efetivada, podemos começar a chamar as funções expostas pelo servidor. Estas
chamadas se dão por meio do objeto retornado da chamada de conexão. Caso este
objeto esteja numa variável `conn`, podemos chamar a função por meio de 
`conn.root.consultar_cr(matricula)` por exemplo.

O cliente implementado apresenta um menu para o usuário pelo terminal, onde o
usuário pode interagir entrando com números de 0-4, e após seguindo as
instruções da opção selecionada. O cliente chamará a função apropriada do
servidor e apresentará ao usuário o resultado retornado pelo servidor.
