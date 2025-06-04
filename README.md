# Pega Pega!

"Pega Pega!" é um jogo arcade simples e divertido desenvolvido em **Pygame**. Seu objetivo é controlar um jogador na parte inferior da tela e evitar que os objetos vermelhos que caem o atinjam. A dificuldade do jogo aumenta progressivamente à medida que você pontua!

---

## Funcionalidades Principais

* **Controle Intuitivo:** Mova seu jogador para a **esquerda** e para a **direita** usando as teclas de seta.
* **Objetos Aleatórios:** Objetos vermelhos surgem aleatoriamente no topo da tela e caem em direção ao jogador.
* **Pontuação:** Ganhe um ponto para cada objeto que conseguir passar pela parte inferior da tela sem colidir com o jogador.
* **Dificuldade Dinâmica:** A velocidade dos objetos e a frequência de seu surgimento aumentam gradualmente, tornando o desafio cada vez maior.
* **Reinício Rápido:** Se um objeto colidir com seu jogador, o jogo é instantaneamente reiniciado, e você pode tentar de novo para bater seu recorde!

---

## Como Jogar

1.  **Instalação:** Certifique-se de ter o Pygame instalado. Se não tiver, abra seu terminal e execute:
    ```bash
    pip install pygame
    ```
2.  **Execução:** Salve o código-fonte como um arquivo Python (ex: `pega_pega.py`) e execute-o a partir do seu terminal:
    ```bash
    python pega_pega.py
    ```
3.  **Controles:**
    * **Seta para a Esquerda:** Move o jogador para a esquerda.
    * **Seta para a Direita:** Move o jogador para a direita.
4.  **Objetivo:** Deixe os objetos vermelhos passarem pela parte inferior da tela para acumular pontos. Evite a todo custo colidir com eles!

---

## Configurações do Jogo

Você pode personalizar a experiência de jogo ajustando as variáveis no início do código:

* `LARGURA_TELA` e `ALTURA_TELA`: Definem o tamanho da janela do jogo.
* `TAMANHO_JOGADOR`: Altera o tamanho do seu personagem.
* `velocidade_jogador`: Controla a velocidade de movimento do jogador.
* `velocidade_objeto_base`: A velocidade inicial com que os objetos caem.
* `frequencia_objeto_base`: Determina a frequência de surgimento de novos objetos (valores menores significam mais objetos).
* `incremento_velocidade_objeto`: Quanto a velocidade dos objetos aumenta em cada incremento de dificuldade.
* `decremento_frequencia_objeto`: O quanto a frequência de objetos é reduzida (tornando-os mais comuns) a cada incremento de dificuldade.
* `pontos_para_aumentar_dificuldade`: A quantidade de pontos necessária para que o jogo aumente sua dificuldade.

Experimente mudar esses valores para criar sua própria versão do "Pega Pega!"!
