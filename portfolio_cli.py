# portfolio_cli.py
# Portfólio de linha de comando (CLI) – Evellyn Gois

from textwrap import dedent

DADOS = {
    "nome": "Evellyn Gois dos Santos",
    "cidade": "São Paulo/SP – São Miguel Paulista",
    "sobre": (
        "Estudante de Análise e Desenvolvimento de Sistemas (UNICSUL). "
        "Em busca do primeiro estágio em TI. Foco atual em Lógica de Programação, "
        "Python, SQL e Git/GitHub, com interesse em Cibersegurança."
    ),
    "formacao": "Análise e Desenvolvimento de Sistemas – Universidade Cruzeiro do Sul (previsão 2027)",
    "aprendendo": [
        "Python (lógica, estruturas básicas)",
        "SQL (consultas e manipulação de dados)",
        "Git & GitHub (versionamento e colaboração)",
        "Markdown (anotações, documentação)"
    ],
    "tecnologias": {
        "Python": "básico",
        "SQL": "básico",
        "Git/GitHub": "iniciante",
        "Markdown": "iniciante"
    },
    "projetos": [
        {
            "nome": "Glossário de TI – Iniciantes",
            "repo": "https://github.com/evellyngois/glossario-ti-iniciantes",
            "descricao": "Mini glossário com termos básicos de TI, para quem está começando."
        },
        {
            "nome": "Otimizando LinkedIn",
            "repo": "https://github.com/evellyngois/otimizando-linkedin",
            "descricao": "Guia rápido com dicas simples para melhorar o perfil no LinkedIn."
        },
        {
            "nome": "Perfil (README)",
            "repo": "https://github.com/evellyngois/evellyngois",
            "descricao": "README do perfil com o que estou estudando e como uso o GitHub."
        }
    ],
    "contatos": {
        "Email": "evellyngois.ds@gmail.com",
        "LinkedIn": "https://www.linkedin.com/in/evellyngois/"
    }
}


def _titulo(t):
    print("\n" + "═" * 60)
    print(f" {t}")
    print("═" * 60)


def _pausa():
    input("\nPressione Enter para voltar ao menu...")


def _mostrar_sobre():
    _titulo("SOBRE MIM")
    print(f"Nome: {DADOS['nome']}")
    print(f"Cidade: {DADOS['cidade']}")
    print(f"Formação: {DADOS['formacao']}")
    print("\nResumo:")
    print("  " + DADOS["sobre"])
    _pausa()


def _mostrar_aprendendo():
    _titulo("O QUE ESTOU APRENDENDO")
    for i, item in enumerate(DADOS["aprendendo"], start=1):
        print(f" {i}. {item}")
    _pausa()


def _mostrar_tecnologias():
    _titulo("TECNOLOGIAS E NÍVEIS")
    for tech, nivel in DADOS["tecnologias"].items():
        print(f" • {tech}: {nivel}")
    _pausa()


def _mostrar_projetos():
    _titulo("PROJETOS")
    for i, p in enumerate(DADOS["projetos"], start=1):
        print(f" {i}. {p['nome']}")
        print(f"    Repo: {p['repo']}")
        print(f"    Sobre: {p['descricao']}\n")
    _pausa()


def _mostrar_contatos():
    _titulo("CONTATOS")
    for k, v in DADOS["contatos"].items():
        print(f" • {k}: {v}")
    _pausa()


def _gerar_markdown():
    """Gera um arquivo PORTFOLIO.md com um resumo do portfólio."""
    md = ["# Portfólio – Evellyn Gois\n"]
    md.append(f"**Sobre:** {DADOS['sobre']}\n")
    md.append(f"**Formação:** {DADOS['formacao']}\n")
    md.append("## O que estou aprendendo\n")
    md += [f"- {item}\n" for item in DADOS["aprendendo"]]
    md.append("\n## Tecnologias e níveis\n")
    md += [f"- **{t}**: {n}\n" for t, n in DADOS["tecnologias"].items()]
    md.append("\n## Projetos\n")
    for p in DADOS["projetos"]:
        md.append(f"- **{p['nome']}** – {p['descricao']}  \n  {p['repo']}\n")
    md.append("\n## Contatos\n")
    for k, v in DADOS["contatos"].items():
        md.append(f"- {k}: {v}\n")

    with open("PORTFOLIO.md", "w", encoding="utf-8") as f:
        f.write("".join(md))

    _titulo("Arquivo gerado!")
    print("Criei o arquivo PORTFOLIO.md na pasta do projeto.")
    _pausa()


def executar():
    while True:
        print(dedent("""
            ================================================
              Portfólio CLI – Evellyn Gois
            ================================================
            1) Sobre mim
            2) O que estou aprendendo
            3) Tecnologias e níveis
            4) Projetos
            5) Contatos
            6) Gerar PORTFOLIO.md
            7) Sair
        """))
        op = input("Escolha uma opção (1–7): ").strip()

        if op == "1":
            _mostrar_sobre()
        elif op == "2":
            _mostrar_aprendendo()
        elif op == "3":
            _mostrar_tecnologias()
        elif op == "4":
            _mostrar_projetos()
        elif op == "5":
            _mostrar_contatos()
        elif op == "6":
            _gerar_markdown()
        elif op == "7":
            print("\nAté mais! 👋")
            break
        else:
            print("Opção inválida. Tente novamente.\n")
def executar():
    print("=== Portfólio CLI - Evellyn Gois ===\n")
    print(f"Nome: {DADOS['nome']}")
    print(f"Cidade: {DADOS['cidade']}")
    print(f"Sobre: {DADOS['sobre']}\n")

    print("📚 Formação:")
    print(f"- {DADOS['formacao']}\n")

    print("📖 O que estou aprendendo:")
    for item in DADOS['aprendendo']:
        print(f"- {item}")
    print()

    print("🛠 Tecnologias:")
    for tech, nivel in DADOS['tecnologias'].items():
        print(f"- {tech}: {nivel}")
    print()

    print("📂 Projetos:")
    for projeto in DADOS['projetos']:
        print(f"- {projeto['nome']}")
        print(f"  Repositório: {projeto['repo']}")
        print(f"  Descrição: {projeto['descricao']}\n")

