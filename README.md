# GitHub Upload Script

<div align="center">
  <img src="public/logo_ami.png" alt="Am I Artificial Intelligence Logo" width="250" height="250">
  <h1>github_upload.py</h1>
  <p>Uma ferramenta Python simples e eficaz para enviar qualquer projeto para o GitHub em um único comando</p>
</div>

## 🌟 Visão Geral

O **github_upload.py** é um script Python autônomo que simplifica todo o processo de envio de projetos para o GitHub. Não importa se você é iniciante ou se apenas quer evitar digitar múltiplos comandos Git, este script automatiza tudo: desde a inicialização do repositório até o push final.

## ✨ Características

- 🚀 **Tudo-em-Um**: Gerencia o processo completo em uma única execução
- 🔄 **Auto-Correção**: Detecta e corrige configurações incorretas
- 🔐 **Autenticação Flexível**: Suporta tokens ou login interativo
- 📊 **Feedback Visual**: Mostra claramente o que está acontecendo em cada etapa
- 🌐 **URL Inteligente**: Formata corretamente a URL do GitHub em vários formatos
- 🔧 **Sem Dependências**: Utiliza apenas bibliotecas padrão do Python
- 📝 **Mensagens Personalizadas**: Permite personalizar a mensagem de commit

## 📋 Requisitos

- Python 3.6 ou superior
- Git instalado e disponível na linha de comando
- Conexão com internet
- Acesso a uma conta do GitHub

## 🚀 Como Usar

### Método Rápido:

1. Baixe o arquivo `github_upload.py` para a pasta raiz do seu projeto
2. Execute o script incluindo a URL do repositório como argumento:

```bash
python github_upload.py https://github.com/seu-usuario/seu-repositorio.git
```

### Método com Mensagem Personalizada:

```bash
python github_upload.py https://github.com/seu-usuario/seu-repositorio.git "Sua mensagem de commit personalizada"
```

### Método Interativo:

1. Baixe o arquivo `github_upload.py` para a pasta raiz do seu projeto
2. Execute o script sem argumentos:

```bash
python github_upload.py
```

3. Quando solicitado, insira a URL do seu repositório no GitHub
4. Opcionalmente, forneça uma mensagem de commit personalizada

## 🔍 O que o script faz

1. **Inicializa** um repositório Git (se ainda não existir)
2. **Remove** qualquer configuração anterior de "origin" (para evitar conflitos)
3. **Configura** o remote "origin" com a URL correta do seu repositório
4. **Mostra** todos os arquivos que serão enviados
5. **Adiciona** todos os arquivos ao stage
6. **Realiza** um commit com a mensagem personalizada ou padrão
7. **Detecta** automaticamente a branch padrão (main ou master)
8. **Envia** (push) para o GitHub
9. **Trata** problemas de autenticação oferecendo opções para usar token ou login interativo

## 🔒 Autenticação

Se encontrar problemas de autenticação, o script oferece duas opções:

### Opção 1: Token de Acesso Pessoal (Recomendado)
1. Crie um token em: GitHub → Settings → Developer Settings → Personal Access Tokens → Tokens (classic)
2. Certifique-se de que o token tenha permissão para o escopo "repo"
3. Quando solicitado pelo script, insira o token gerado

### Opção 2: Login Interativo
1. Deixe o campo de token em branco quando solicitado
2. O Git solicitará seu nome de usuário e senha ou token

## 📝 Exemplos

### Exemplo 1: Enviar um novo projeto

```bash
# Na pasta do seu projeto
$ python github_upload.py https://github.com/seu-usuario/novo-projeto.git "Primeira versão"

🚀 Iniciando upload para GitHub...
📂 Diretório atual: /caminho/para/seu/projeto
🔧 Inicializando repositório Git...
✅ Repositório Git inicializado
🔗 Configurando repositório remoto: https://github.com/seu-usuario/novo-projeto.git
📄 Arquivos a serem enviados:
 A  index.html
 A  style.css
 A  script.js
➕ Adicionando arquivos ao stage...
💾 Realizando commit: 'Primeira versão'
🔄 Enviando para branch 'main'...
✅ Push realizado com sucesso!
```

### Exemplo 2: Atualizar um repositório existente

```bash
# Na pasta de um projeto já enviado anteriormente
$ python github_upload.py

URL do repositório GitHub: https://github.com/seu-usuario/projeto-existente.git
Mensagem de commit (deixe em branco para mensagem padrão): Atualização da documentação
🚀 Iniciando upload para GitHub...
📂 Diretório atual: /caminho/para/seu/projeto
✅ Já é um repositório Git
🔗 Configurando repositório remoto: https://github.com/seu-usuario/projeto-existente.git
📄 Arquivos a serem enviados:
 M  README.md
 A  docs/guia.md
➕ Adicionando arquivos ao stage...
💾 Realizando commit: 'Atualização da documentação'
🔄 Enviando para branch 'main'...
✅ Push realizado com sucesso!
```

## 🚨 Limitações

- Envia todos os arquivos na pasta que não estão no `.gitignore`
- Não gerencia branches diferentes da principal (main/master)
- Não resolve conflitos de merge automaticamente

## 🔮 Futuras Melhorias

- [ ] Suporte para seleção de arquivos específicos
- [ ] Gerenciamento de múltiplas branches
- [ ] Resolução de conflitos básicos
- [ ] Interface gráfica simples
- [ ] Opção para preservar configuração de remote existente

## 📜 Licença

Este script é disponibilizado sob a licença MIT. Fique à vontade para usar, modificar e distribuir conforme necessário.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir melhorias
- Enviar pull requests

---

<div align="center">
  <p>Desenvolvido por <a href="https://ami.digital">Am I Artificial Intelligence</a></p>
  <a href="https://ami.digital"><img src="public/logo_ami.png" alt="Am I Artificial Intelligence Logo" width="50" height="50"></a>
</div>
