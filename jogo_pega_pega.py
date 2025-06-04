import pygame
import random

# Inicializar o Pygame
pygame.init()

# --- Configurações da Tela ---
LARGURA_TELA = 800
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Pega Pega!")

# --- Cores ---
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)

# --- Configurações do Jogador ---
TAMANHO_JOGADOR = 50
COR_JOGADOR = PRETO
velocidade_jogador = 7
jogador_x_inicial = (LARGURA_TELA - TAMANHO_JOGADOR) // 2
jogador_y_inicial = ALTURA_TELA - TAMANHO_JOGADOR - 10

# --- Configurações dos Objetos ---
TAMANHO_OBJETO = 30
COR_OBJETO = VERMELHO

# --- Configurações de Jogo e Dificuldade ---
score = 0
fonte = pygame.font.Font(None, 36) # Fonte para o score

# Dificuldade Base
velocidade_objeto_base = 4
frequencia_objeto_base = 35 # A cada X frames um novo objeto (maior = menos frequente)

# Modificadores de Dificuldade
incremento_velocidade_objeto = 0.5
decremento_frequencia_objeto = 3 # Reduz este valor da frequência (torna mais frequente)
pontos_para_aumentar_dificuldade = 5

# Variáveis de estado do jogo
jogador_x = jogador_x_inicial
jogador_y = jogador_y_inicial
objetos = [] # Lista para armazenar as coordenadas [x, y] dos objetos
contador_frames_para_novo_objeto = 0

# Valores atuais de dificuldade (iniciam com os base)
velocidade_objeto_atual = velocidade_objeto_base
frequencia_objeto_atual = frequencia_objeto_base
proximo_limite_score_para_dificuldade = pontos_para_aumentar_dificuldade

# --- Loop Principal do Jogo ---
rodando = True
clock = pygame.time.Clock()
FPS = 60

def resetar_jogo():
    """Reseta o estado do jogo para o início."""
    global jogador_x, jogador_y, score, objetos
    global velocidade_objeto_atual, frequencia_objeto_atual, proximo_limite_score_para_dificuldade
    global contador_frames_para_novo_objeto

    jogador_x = jogador_x_inicial
    jogador_y = jogador_y_inicial
    score = 0
    objetos = []
    contador_frames_para_novo_objeto = 0

    velocidade_objeto_atual = velocidade_objeto_base
    frequencia_objeto_atual = frequencia_objeto_base
    proximo_limite_score_para_dificuldade = pontos_para_aumentar_dificuldade

resetar_jogo() # Configura o estado inicial do jogo

while rodando:
    # --- Processamento de Eventos ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # --- Lógica de Jogo ---

    # Movimento do Jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jogador_x -= velocidade_jogador
    if teclas[pygame.K_RIGHT]:
        jogador_x += velocidade_jogador

    # Manter jogador dentro da tela
    if jogador_x < 0:
        jogador_x = 0
    if jogador_x > LARGURA_TELA - TAMANHO_JOGADOR:
        jogador_x = LARGURA_TELA - TAMANHO_JOGADOR

    # Criar novos objetos
    contador_frames_para_novo_objeto += 1
    if contador_frames_para_novo_objeto >= frequencia_objeto_atual:
        contador_frames_para_novo_objeto = 0
        novo_objeto_x = random.randint(0, LARGURA_TELA - TAMANHO_OBJETO)
        novo_objeto_y = -TAMANHO_OBJETO # Começa um pouco acima da tela
        objetos.append(pygame.Rect(novo_objeto_x, novo_objeto_y, TAMANHO_OBJETO, TAMANHO_OBJETO))

    # Mover objetos, checar colisão e pontuação
    jogador_rect = pygame.Rect(jogador_x, jogador_y, TAMANHO_JOGADOR, TAMANHO_JOGADOR)
    
    objetos_na_tela_apos_frame = [] # Lista para guardar objetos que continuam
    for objeto_rect in objetos:
        # Mover objeto para baixo
        objeto_rect.y += velocidade_objeto_atual

        # Checar colisão com o jogador
        if jogador_rect.colliderect(objeto_rect):
            resetar_jogo()
            break # Interrompe o processamento de objetos neste frame, pois o jogo reiniciou
        
        # Se o objeto ainda está na tela (não passou do fundo)
        if objeto_rect.top < ALTURA_TELA:
            objetos_na_tela_apos_frame.append(objeto_rect)
        else: # Objeto passou da tela por baixo - marcar ponto
            score += 1
            # Checar e aumentar dificuldade
            if score >= proximo_limite_score_para_dificuldade:
                velocidade_objeto_atual += incremento_velocidade_objeto
                frequencia_objeto_atual = max(5, frequencia_objeto_atual - decremento_frequencia_objeto) # Frequência mínima
                proximo_limite_score_para_dificuldade += pontos_para_aumentar_dificuldade
    else: # Este 'else' pertence ao 'for objeto_rect in objetos'. Executa se o 'break' não foi chamado.
        objetos = objetos_na_tela_apos_frame


    # --- Desenhar na Tela ---
    tela.fill(BRANCO) # Limpa a tela

    # Desenhar jogador
    pygame.draw.rect(tela, COR_JOGADOR, jogador_rect)

    # Desenhar objetos
    for objeto_rect in objetos:
        pygame.draw.rect(tela, COR_OBJETO, objeto_rect)

    # Desenhar score
    texto_score_surface = fonte.render(f"Score: {score}", True, PRETO)
    tela.blit(texto_score_surface, (10, 10))

    # Atualizar a tela
    pygame.display.flip()

    # Controlar FPS
    clock.tick(FPS)

# Finalizar o Pygame
pygame.quit()
