import os
import subprocess
import sys

def github_upload(repo_url, commit_message=None):
    """
    Script completo para enviar o projeto para o GitHub.
    Gerencia todo o processo: inicialização, configuração, commit e push.
    
    Args:
        repo_url (str): URL do repositório GitHub
        commit_message (str, optional): Mensagem de commit personalizada
    """
    print("🚀 Iniciando upload para GitHub...")
    current_dir = os.getcwd()
    print(f"📂 Diretório atual: {current_dir}")
    
    try:
        # Verifica se é um repositório git
        is_git_repo = os.path.isdir(os.path.join(current_dir, '.git'))
        
        if not is_git_repo:
            print("🔧 Inicializando repositório Git...")
            subprocess.run(["git", "init"], check=True)
            print("✅ Repositório Git inicializado")
        else:
            print("✅ Já é um repositório Git")
        
        # Verifica e limpa configuração origin anterior
        remote_check = subprocess.run(["git", "remote", "-v"], capture_output=True, text=True)
        if "origin" in remote_check.stdout:
            print("🔄 Removendo configuração origin anterior...")
            subprocess.run(["git", "remote", "remove", "origin"], check=True)
        
        # Adiciona o novo repositório remoto
        print(f"🔗 Configurando repositório remoto: {repo_url}")
        subprocess.run(["git", "remote", "add", "origin", repo_url], check=True)
        
        # Verifica status para mostrar arquivos modificados
        status_result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if not status_result.stdout.strip():
            print("⚠️ Nenhuma alteração detectada. Nada para commit.")
            return False
        
        print("\n📄 Arquivos a serem enviados:")
        subprocess.run(["git", "status", "-s"])
        print()  # Linha em branco para melhor legibilidade
        
        # Adiciona todos os arquivos ao stage
        print("➕ Adicionando arquivos ao stage...")
        subprocess.run(["git", "add", "."], check=True)
        
        # Realiza o commit
        if commit_message is None:
            commit_message = "Versão inicial do projeto"
        
        print(f"💾 Realizando commit: '{commit_message}'")
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        # Determina qual branch está sendo usada (main ou master)
        branch_result = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True)
        current_branch = branch_result.stdout.strip()
        if not current_branch:
            # Verifica qual é a branch padrão
            current_branch = "main"
            # Verifica se precisamos renomear a branch
            branch_list = subprocess.run(["git", "branch"], capture_output=True, text=True).stdout
            if "master" in branch_list and "main" not in branch_list:
                current_branch = "master"
        
        print(f"🔄 Enviando para branch '{current_branch}'...")
        push_result = subprocess.run(["git", "push", "-u", "origin", current_branch], capture_output=True, text=True)
        
        if push_result.returncode != 0:
            print("\n⚠️ Erro ao fazer push. Possível problema de autenticação.")
            print(push_result.stderr)
            
            # Verifica se é problema de autenticação e tenta ajudar
            if "Authentication failed" in push_result.stderr or "could not read Username" in push_result.stderr:
                print("\n🔑 Problema de autenticação. Tentando configurar...")
                
                # Configura URL com token pessoal se fornecido
                token = input("Digite seu token de acesso pessoal do GitHub (ou deixe em branco para usar login interativo): ").strip()
                if token:
                    # Extrai informações da URL
                    if "https://" in repo_url:
                        new_url = repo_url.replace("https://", f"https://{token}@")
                        subprocess.run(["git", "remote", "set-url", "origin", new_url], check=True)
                        print("🔐 URL do remote atualizada com token")
                        
                        # Tenta push novamente
                        print(f"🔄 Tentando push novamente para '{current_branch}'...")
                        push_result = subprocess.run(["git", "push", "-u", "origin", current_branch], capture_output=True, text=True)
                        
                        if push_result.returncode != 0:
                            print("❌ Falha ao fazer push mesmo com token.")
                            print(push_result.stderr)
                            return False
                        else:
                            print("✅ Push realizado com sucesso usando token!")
                    else:
                        print("⚠️ URL não é HTTPS. Não foi possível incorporar o token.")
                else:
                    print("🔄 Tentando push com credenciais interativas...")
                    # Tenta push novamente, deixando Git solicitar credenciais
                    interactive_push = subprocess.run(["git", "push", "-u", "origin", current_branch])
                    if interactive_push.returncode != 0:
                        print("❌ Falha ao fazer push interativo.")
                        return False
                    else:
                        print("✅ Push interativo realizado com sucesso!")
            else:
                return False
        else:
            print("✅ Push realizado com sucesso!")
        
        # Exibe link do repositório
        clean_url = repo_url.replace(".git", "")
        if clean_url.startswith("git@"):
            clean_url = clean_url.replace("git@github.com:", "https://github.com/")
        
        print(f"\n🌐 Seu projeto foi enviado! Acesse: {clean_url}")
        print("📝 README.md foi enviado (se existir) e deve estar formatado corretamente.")
        print("🎉 Processo concluído com sucesso!")
        
        return True
    
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar comando Git: {e}")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False

if __name__ == "__main__":
    # Usar URL fornecida como argumento ou pedir ao usuário
    if len(sys.argv) > 1:
        repository_url = sys.argv[1]
    else:
        repository_url = input("URL do repositório GitHub: ").strip()
        
        # Validação básica da URL
        while not repository_url or not ("github.com" in repository_url):
            print("⚠️ URL inválida. Deve ser uma URL do GitHub.")
            repository_url = input("URL do repositório GitHub: ").strip()
    
    # Verificar se o usuário quer fornecer uma mensagem de commit personalizada
    if len(sys.argv) > 2:
        custom_message = sys.argv[2]
    else:
        custom_message = input("Mensagem de commit (deixe em branco para mensagem padrão): ").strip()
        if not custom_message:
            custom_message = None
    
    # Executa o upload
    success = github_upload(repository_url, custom_message)
    
    if success:
        print("\n✨ Tudo pronto! Seu código está no GitHub.")
    else:
        print("\n⚠️ Houve problemas durante o upload. Revise os erros acima.")
        
    # Pausa antes de fechar
    print("\nPressione Enter para sair...")
    input()