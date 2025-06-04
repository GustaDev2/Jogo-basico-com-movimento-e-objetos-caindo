# Pega Pega! (Pygame)

Um jogo simples estilo "desvie dos objetos que caem" desenvolvido em Python com a biblioteca Pygame.

## Descrição

O jogador controla um quadrado preto na parte inferior da tela e deve desviar dos quadrados vermelhos que caem do topo.
A cada objeto desviado, a pontuação aumenta.
A dificuldade do jogo (velocidade e frequência dos objetos) aumenta progressivamente conforme a pontuação sobe.
Se o jogador colidir com um objeto vermelho, o jogo é reiniciado.

## Como Jogar

### Pré-requisitos

*   Python 3.x
*   Pygame

Você pode instalar o Pygame com o pip:
```bash
pip install pygame

Executando o Jogo
Navegue até a pasta do projeto no seu terminal:
cd caminho/para/seu/projeto

Execute o script Python:
python jogo_pega_pega.py

Controles
Seta Esquerda: Mover o jogador para a esquerda.
Seta Direita: Mover o jogador para a direita.

Estrutura do Código
O arquivo principal é jogo_pega_pega.py e contém toda a lógica do jogo, incluindo:

Inicialização do Pygame e da tela.
Definição de cores e configurações do jogador/objetos.
Lógica de jogo principal (movimento, criação de objetos, detecção de colisão, pontuação, aumento de dificuldade).
Desenho dos elementos na tela.
Função para resetar o estado do jogo.


**Para criar o arquivo:**

1.  Abra um editor de texto simples (como o Bloco de Notas, VS Code, Sublime Text, etc.).
2.  Copie e cole o conteúdo acima no editor.
3.  Salve o arquivo com o nome `README.md` dentro da pasta `c:\Users\gusta\OneDrive\Documentos\Python - 2025\projeto 1\`.

Depois de criar o `README.md`, você pode adicioná-lo e comitá-lo ao seu repositório Git:

```bash
cd c:\Users\gusta\OneDrive\Documentos\Python - 2025\projeto 1\
git add README.md
git commit -m "Adiciona README.md com descrição do jogo e instruções"
git push origin main
