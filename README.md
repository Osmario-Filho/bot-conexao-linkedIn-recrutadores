# Bot de Envio de Convites no LinkedIn

Este projeto é um script em Python que automatiza o envio de convites de conexão no LinkedIn utilizando a biblioteca Selenium para controlar o navegador Chrome. O diferencial deste bot é permitir buscas personalizadas por recrutadores de TI ou recrutadores em geral, facilitando a expansão da sua rede de contatos de forma segmentada e eficiente.

---

## Funcionalidades

- Login automático no LinkedIn com credenciais fornecidas pelo usuário.
- Pesquisa personalizada por recrutadores de TI ou recrutadores em geral.
- Navegação até a área de conexões do LinkedIn.
- Filtro automático para mostrar apenas perfis de pessoas.
- Envio automático de convites para os usuários encontrados na pesquisa.
- Controle da quantidade de convites enviados, conforme definido pelo usuário.
- Rolagem automática da página para carregar mais perfis quando necessário.
- Tratamento de exceções comuns durante a interação com elementos da página.
- Mensagens de progresso exibidas no console para acompanhamento.

---

## Tecnologias Utilizadas

- Python 3.x
- Selenium WebDriver
- WebDriver Manager para gerenciamento automático do ChromeDriver
- Google Chrome (navegador)

---

## Pré-requisitos

Antes de executar o script, certifique-se de ter instalado:

- Python 3.x ([Download](https://www.python.org/downloads/))
- Google Chrome instalado no seu sistema.
- Bibliotecas Python necessárias:
pip install selenium webdriver-manager

---

## Como usar

1. Clone este repositório ou baixe os arquivos.

2. Abra o terminal na pasta do projeto.

3. Execute o script com o comando:

python nome_do_seu_script.py


4. Insira as informações solicitadas pelo script:

   - Seu e-mail de usuário do LinkedIn.
   - Sua senha do LinkedIn.
   - A quantidade de convites que deseja enviar.
   - O tipo de busca:  
     - Digite `1` para buscar recrutadores de TI.  
     - Digite `2` para buscar recrutadores em geral.

5. O script abrirá o navegador, fará login, realizará a busca personalizada e começará a enviar os convites automaticamente para os usuários encontrados.

6. Acompanhe as mensagens no console para ver o progresso.

7. Ao final, pressione Enter para fechar o navegador.

---

## Atenção e Responsabilidade

- O idioma padrão do LinkedIn deve ser **português** para melhor funcionamento do script.
- Para que o script funcione corretamente, **é necessário desabilitar a verificação em duas etapas (autenticação de dois fatores)** na sua conta do LinkedIn, pois o script não consegue lidar com essa etapa extra de verificação.
- Use este script com responsabilidade e respeite as políticas do LinkedIn para evitar bloqueios ou restrições na sua conta.
- O LinkedIn pode limitar ou bloquear ações automatizadas que violem seus termos de uso.
- Este script é fornecido para fins educacionais e de automação pessoal.

---

## Estrutura do Código

O script realiza as seguintes etapas principais:

- Solicita as credenciais, a quantidade de convites e o tipo de pesquisa.
- Inicializa o ChromeDriver automaticamente.
- Realiza login no LinkedIn.
- Navega até a seção de conexões.
- Executa a busca personalizada conforme a opção escolhida.
- Filtra os resultados para mostrar apenas pessoas.
- Envia convites clicando nos botões "Conectar" dos usuários encontrados na pesquisa.
- Rola a página para carregar mais perfis conforme necessário.
- Trata exceções comuns para evitar falhas durante a execução.

---

## Possíveis melhorias

- Implementar autenticação via OAuth para maior segurança.
- Adicionar suporte a múltiplas contas.
- Melhorar o tratamento de erros e logs.
- Automatizar o login com autenticação em duas etapas.
- Criar interface gráfica para facilitar o uso.
- Permitir envio de mensagens personalizadas junto ao convite.

---

## Contato

Para dúvidas, sugestões ou contribuições, entre em contato:

- Email: osmarioslfilho@gmail.com  
- GitHub: https://github.com/Osmario-Filho

---

Obrigado por usar este projeto! 🚀

