# Findora: Sistema de Busca de Pessoas

O **Findora** é uma aplicação desenvolvida para auxiliar na gestão e organização de processos de busca de pessoas desaparecidas. O sistema permite registar pessoas, técnicos responsáveis e gerir tickets de acompanhamento, garantindo a integridade e segurança dos dados.

## 🚀 Funcionalidades Principais
*   **Gestão de Pessoas:** Registo, listagem e atualização de status (ex: "Encontrado").
*   **Gestão de Técnicos:** Registo de profissionais responsáveis pela busca.
*   **Gestão de Tickets:** Abertura e acompanhamento de tickets de busca associando pessoas a técnicos.
*   **Controlo de Acesso:** Implementação de perfis de utilizador (Admin/Técnico) para restringir ações sensíveis.
*   **Auditoria:** Registo automático de todas as ações críticas em ficheiro de logs (`sistema.log`).

## 🛠 Tecnologias Utilizadas
*   **Linguagem:** Python
*   **Base de Dados:** MySQL
*   **ORM:** SQLAlchemy
*   **Testes:** unittest

## 📋 Como Instalar e Executar

1. **Pré-requisitos:**
   - Ter o MySQL Workbench a correr.
   - Ter o Python instalado.

2. **Preparação:**
   - Cria uma base de dados chamada `findora_db` no MySQL Workbench.
   - Instala as dependências necessárias:
     ```bash
     pip install sqlalchemy mysql-connector-python
     ```

3. **Execução:**
   - Abre o terminal na pasta do projeto e executa:
     ```bash
     python main.py
     ```

## 🔐 Segurança
O Findora prioriza a integridade dos dados através de:
- **RBAC (Role-Based Access Control):** Ações administrativas restritas a perfis de administrador.
- **Tratamento de Exceções:** Prevenção de falhas críticas durante a execução.
- **Auditoria:** Histórico detalhado de atividades para fins de rastreabilidade.

## ✒️ Autor
Desenvolvido por **Robson Cabral**.

---
*Projeto académico focado em boas práticas de programação e segurança de sistemas.*