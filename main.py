from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException

# Solicita o email do usuário
nome_usuario = input("Digite o seu email de usuário: ") 
# Solicita a senha do usuário
senha_usuario = input("Digite sua senha de usuário: ") 
# Solicita a quantidade de convites que deseja enviar
quantidade_convites = int(input('Digite a quantidade de convites que deseja ser enviado: '))
#faz uma pesquisa personalizada
print('Você tem duas opções de escolha. A primeira é mais focada em recrutadores de TI, a segunda é em pesquisadores no geral')
pesquisa_personalizada = int(input('Digite 1 (um) para fazer a busca específica em TI, digite 2 (dois) para fazer uma busca mais geral: '))

while pesquisa_personalizada:
    if pesquisa_personalizada == 1:
        pesquisa_personalizada = str('"Technical Recruiter" OR "Talent Acquisition" OR "Developer Recruiter" OR "Hiring Manager"')
        break
    elif pesquisa_personalizada == 2:
        pesquisa_personalizada = str(' "Recruiter" OR "Talent Acquisition" OR "Technical Recruiter" OR "Corporate Recruiter" ')
        break
    else:
        print('Digite ou 1 ou 2')
        pesquisa_personalizada = int(input('Digite 1 (um) para fazer a busca específica em TI, digite 2 (dois) para fazer uma busca mais geral: '))

# Configura o serviço do ChromeDriver
servico = Service(ChromeDriverManager().install())
# Inicializa o navegador Chrome
navegador = webdriver.Chrome(service=servico)

# Acessa a página de login do LinkedIn
navegador.get("https://www.linkedin.com/login/")

# Maximiza a janela do navegador
navegador.maximize_window() 

# Define o tempo máximo de espera para elementos ficarem disponíveis
wait = WebDriverWait(navegador, 15) 

# Espera até o campo de usuário estar clicável e preenche com o email
preencher_usuario = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="username"]')))
preencher_usuario.click()
preencher_usuario.send_keys(nome_usuario)

# Preenche o campo de senha
navegador.find_element(By.XPATH , '//*[@id="password"]').send_keys(senha_usuario)

# Clica no botão de login
navegador.find_element(By.XPATH , '//*[@id="organic-div"]/form/div[4]/button').click()

# Acessa a área de conexões
area_conexao = navegador.find_element(By.XPATH , '//*[@id="global-nav"]/div/nav/ul/li[2]/a')
area_conexao.click()

# Procura a barra de notificaçao
achar_barra_de_pesquisa = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[3]/div[1]/header/div/div/div[1]/div/input')))
achar_barra_de_pesquisa.click()
achar_barra_de_pesquisa.send_keys(pesquisa_personalizada + Keys.ENTER)

# Filtra por pessoa 
filtrar_por_pessoa = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[3]/button')))
filtrar_por_pessoa.click()

# Espera até que pelo menos um botão "Conectar" esteja clicável
conectar_usuario = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, '//button[contains(., "Conectar") or contains(., "Connect")]')
    )
)

# Define o tempo de pausa após rolagem para carregar mais perfis
SCROLL_PAUSE_TIME = 2

# Inicializa o contador de convites enviados
contador_convites = 0

# Loop principal que continua enquanto não atingir a quantidade desejada de convites
while contador_convites < quantidade_convites:
    # Busca todos os botões "Conectar" visíveis na página
    botoes_conectar = navegador.find_elements(By.XPATH, '//button[contains(., "Conectar") or contains(., "Connect")]')

    if botoes_conectar:
        # Itera sobre cada botão encontrado
        for botao in botoes_conectar:
            # Verifica se ainda pode enviar convites
            if contador_convites < quantidade_convites:
                contador_convites += 1
                try:
                    # Rola a página até o botão para garantir que esteja visível
                    navegador.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao)
                    time.sleep(0.5)  # Pequena pausa para estabilidade
                    # Clica no botão "Conectar"
                    botao.click()
                    print("Convite numero " + str(contador_convites) + " enviado!")
                    time.sleep(1)  # Pausa para evitar bloqueios por ações muito rápidas
                except (ElementClickInterceptedException, StaleElementReferenceException) as e:
                    # Caso não consiga clicar, exibe o erro e continua para o próximo botão
                    print(f"Erro ao clicar no botão: {e}, pulando.")
                    continue
            else:
                # Sai do loop se já enviou a quantidade desejada de convites
                break

    # Rola a página para baixo para tentar carregar mais perfis
    navegador.execute_script("window.scrollBy(0, window.innerHeight);")
    print("Rolando a página para carregar perfis...")
    time.sleep(SCROLL_PAUSE_TIME)  # Pausa para o carregamento dos novos perfis



input("Pressione Enter para fechar o navegador...")
