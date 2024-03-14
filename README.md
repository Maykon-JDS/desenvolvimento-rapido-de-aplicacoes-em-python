![https://img.shields.io/badge/linting-pylint-yellowgreen](https://img.shields.io/badge/linting-pylint-yellowgreen)

# Levantamento de Requisitos - Sistema de Controle Financeiro Pessoal

## 1. Descrição do Sistema
O Sistema de Controle Financeiro Pessoal tem como objetivo ajudar os usuários a gerenciar suas finanças pessoais de forma eficiente. O sistema permite o registro de receitas e despesas, categorização de transações, geração de relatórios e monitoramento do orçamento mensal.

## 2. Funcionalidades Principais

### 2.1. Cadastro de Usuários
- **RF01**: O sistema deve permitir o cadastro de novos usuários com nome, e-mail e senha.
- **RF02**: O sistema deve permitir que os usuários façam login utilizando e-mail e senha cadastrados.
- **RF03**: O sistema deve fornecer uma opção de recuperação de senha via e-mail.

### 2.2. Controle de Receitas e Despesas
- **RF04**: O sistema deve permitir o cadastro de receitas com os seguintes campos:
  - Valor da receita
  - Categoria da receita (Ex: Salário, Investimentos, etc.)
  - Data da receita
  - Descrição (opcional)
- **RF05**: O sistema deve permitir o cadastro de despesas com os seguintes campos:
  - Valor da despesa
  - Categoria da despesa (Ex: Alimentação, Transporte, Moradia, etc.)
  - Data da despesa
  - Descrição (opcional)
- **RF06**: O sistema deve permitir a edição e exclusão de receitas e despesas cadastradas.

### 2.3. Categorização de Transações
- **RF07**: O sistema deve permitir que o usuário crie, edite e exclua categorias personalizadas para receitas e despesas.
- **RF08**: O sistema deve exibir uma lista de categorias pré-definidas para facilitar o processo de categorização.

### 2.4. Monitoramento de Orçamento
- **RF09**: O sistema deve permitir que o usuário defina um orçamento mensal para cada categoria de despesa.
- **RF10**: O sistema deve alertar o usuário quando o limite do orçamento de uma categoria for atingido ou excedido.

### 2.5. Relatórios e Visualização de Dados
- **RF11**: O sistema deve gerar relatórios financeiros que permitam ao usuário visualizar:
  - Total de receitas e despesas por período.
  - Comparação entre receitas e despesas mensais.
  - Distribuição de despesas por categoria.
- **RF12**: O sistema deve permitir a exportação de relatórios em formato PDF ou CSV.

### 2.6. Gráficos e Painéis de Controle
- **RF13**: O sistema deve fornecer gráficos de:
  - Receita vs. Despesa (por mês)
  - Distribuição percentual das despesas por categoria
  - Evolução das receitas e despesas ao longo do tempo
- **RF14**: O sistema deve exibir um painel de controle (dashboard) com resumo financeiro do mês atual, incluindo saldo disponível, total de receitas, total de despesas e status do orçamento.

### 2.7. Lembretes e Notificações
- **RF15**: O sistema deve permitir que o usuário configure lembretes para datas de vencimento de contas e outras despesas recorrentes.
- **RF16**: O sistema deve notificar o usuário sobre eventos importantes, como vencimento de contas e ultrapassagem de orçamento.

## 3. Requisitos Não Funcionais

### 3.1. Segurança
- **RNF01**: O sistema deve utilizar criptografia para armazenamento de senhas.
- **RNF02**: O sistema deve garantir a proteção dos dados financeiros dos usuários.

### 3.2. Performance
- **RNF03**: O sistema deve carregar páginas e exibir dados com tempo de resposta inferior a 2 segundos para a maioria das operações.

### 3.3. Usabilidade
- **RNF04**: O sistema deve ser intuitivo e fácil de usar, com uma interface amigável e acessível a usuários não técnicos.

### 3.4. Disponibilidade
- **RNF05**: O sistema deve estar disponível 99% do tempo durante o mês, exceto em casos de manutenção planejada.

### 3.5. Portabilidade
- **RNF06**: O sistema deve ser acessível tanto via web quanto em dispositivos móveis (responsividade).

## 4. Regras de Negócio

- **RN01**: O usuário não pode cadastrar uma despesa com valor superior ao saldo disponível no sistema.
- **RN02**: O usuário pode criar categorias ilimitadas, mas só pode definir um orçamento mensal para cada uma delas.
- **RN03**: O sistema deve impedir a exclusão de categorias que contenham transações associadas, a menos que essas transações sejam movidas para outra categoria ou excluídas.

## 5. Considerações Finais
Este sistema deve ser projetado para facilitar o controle financeiro pessoal de forma simples e intuitiva, com ênfase na usabilidade e segurança dos dados dos usuários. Futuras expansões podem incluir funcionalidades como sincronização com contas bancárias, sugestões de investimentos e consultoria financeira automatizada.
