🛡️ Cybersecurity Lab: Malware Simulator (Python)

Este repositório contém o projeto desenvolvido para o desafio de Cibersegurança da DIO. O objetivo é demonstrar, de forma prática e em ambiente 100% controlado, o funcionamento de ameaças digitais comuns: Ransomware e Keylogger.

[!CAUTION]
AVISO ÉTICO: Este software foi criado estritamente para fins educacionais e de pesquisa. O uso dessas ferramentas para atividades maliciosas é ilegal e antiético. O desenvolvedor não se responsabiliza pelo uso indevido deste código.

💻 Sobre o Projeto
O projeto utiliza uma interface gráfica moderna desenvolvida com CustomTkinter para gerenciar as simulações.

🔒 Ransomware Simulado
Utiliza criptografia simétrica via biblioteca cryptography (Fernet) para sequestrar arquivos em um diretório alvo.

Ação: Criptografa arquivos .txt e gera uma Nota de Resgate automática.

Recuperação: Demonstra o processo de descriptografia utilizando a chave gerada localmente (chave.key).

⌨️ Keylogger Simulado
Monitora as entradas do teclado utilizando a biblioteca pynput.

Captura: Registra teclas pressionadas e as formata para leitura em um arquivo de log.

Fins de Estudo: Demonstra como a exfiltração de dados sensíveis pode ocorrer sem a percepção do usuário.

🛠️ Tecnologias Utilizadas
Linguagem: Python.

Interface: CustomTkinter (GUI).

Segurança: Cryptography (Fernet).

Monitoramento: Pynput.

📂 Estrutura de Arquivos
Conforme configurado no ambiente de desenvolvimento:

main_gui.py: Painel de controle principal.

ferramentas/: Módulos lógicos do Ransomware e Keylogger.

ambiente_teste/: Pasta segura para simulação de arquivos sequestrados.

logs_capturados/: Destino dos registros do Keylogger.

🛡️ Medidas de Defesa e Mitigação
Como parte da minha formação em ADS, este projeto reforça a importância das seguintes defesas:

Backups Offline: A única garantia total contra o sequestro de dados.

Princípio do Menor Privilégio: Limitar permissões de execução de scripts em diretórios sensíveis.

Endpoint Detection (EDR): Ferramentas que monitoram comportamentos anômalos, como a criptografia em massa de arquivos.

MFA (Autenticação Multifator): Previne que dados capturados por Keyloggers sejam usados para invasão de contas.

👨‍💻 Desenvolvedor
Daniel Gaio
Estudante de Análise e Desenvolvimento de Sistemas.
Focado em desenvolvimento Front-end e Cibersegurança.

<img width="1830" height="1018" alt="Malware_Simulado py" src="https://github.com/user-attachments/assets/a2dacf59-5f08-4165-b86e-c521d96c690e" />
