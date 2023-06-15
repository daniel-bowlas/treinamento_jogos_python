# treinamento_jogos_python
Projetos de criacao de mini jogos para praticar na linguagem Python

# Projeto: Jogo de Adivinhação

## Descrição
Este projeto consiste em um jogo de adivinhação em que o jogador deve tentar acertar um número secreto gerado aleatoriamente. O jogador pode escolher o nível de dificuldade do jogo, que determina o número máximo de tentativas. O objetivo é acertar o número secreto com o menor número de tentativas possível e acumular pontos.

## Lógica da Programação
O jogo segue a seguinte lógica de programação:

1. Inicialização: O jogo começa com uma mensagem de boas-vindas e inicializa as variáveis `numero_secreto`, `tentativas` e `pontos`.

2. Escolha do nível de dificuldade: O jogador é solicitado a escolher um nível de dificuldade (1 para fácil, 2 para médio e 3 para difícil). Com base na escolha do jogador, o número máximo de tentativas é definido.

3. Loop de tentativas: O jogo entra em um loop que se repete de acordo com o número máximo de tentativas. Em cada iteração do loop:
   - O número da tentativa atual é exibido.
   - O jogador insere um chute, digitando um número.
   - O chute é comparado ao `numero_secreto` e são feitas as seguintes verificações:
     - Se o chute é menor que 1 ou maior que 100, uma mensagem de erro é exibida.
     - Se o chute é igual ao `numero_secreto`, o jogador acertou e o loop é interrompido.
     - Se o chute é maior que o `numero_secreto`, é exibida uma mensagem informando que o chute foi maior.
     - Se o chute é menor que o `numero_secreto`, é exibida uma mensagem informando que o chute foi menor.
     - A pontuação do jogador é atualizada com base na diferença entre o `numero_secreto` e o chute.
   - Após o loop de tentativas, uma mensagem é exibida informando o número secreto.

4. Fim do jogo: O jogo termina e exibe uma mensagem de encerramento.

## Execução
Para executar o jogo, execute o arquivo `adivinhacao.py`. O jogo será iniciado e você será guiado pelas instruções exibidas no terminal.

# Projeto: Jogo da Forca e Jogo de Adivinhação (Jog

os.py)

## Descrição
Este projeto consiste em um programa que permite ao usuário escolher entre jogar o jogo da Forca ou o jogo de Adivinhação. O programa exibe um menu com as opções de jogo e, com base na escolha do usuário, inicia o jogo correspondente.

## Lógica da Programação
O programa segue a seguinte lógica de programação:

1. Inicialização: O programa exibe uma mensagem de boas-vindas e apresenta um menu com as opções de jogo (Forca e Adivinhação).

2. Escolha do jogo: O usuário é solicitado a escolher o jogo digitando um número correspondente à opção desejada.

3. Execução do jogo escolhido: Com base na escolha do usuário, o programa inicia o jogo correspondente. Se o usuário escolher 1, o jogo da Forca é iniciado. Se o usuário escolher 2, o jogo de Adivinhação é iniciado.

## Execução
Para executar o programa, execute o arquivo `jogos.py`. O programa exibirá o menu de opções e você poderá escolher entre jogar a Forca ou a Adivinhação. Siga as instruções exibidas no terminal para jogar o jogo escolhido.
