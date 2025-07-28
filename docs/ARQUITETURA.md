# Documentação de Arquitetura e Tecnologias - big_project

Este documento descreve as tecnologias utilizadas e os requisitos não funcionais implementados na aplicação.

## 1. Tecnologias Utilizadas

O projeto é uma aplicação web full-stack com uma clara separação entre o cliente (front-end) e o servidor (back-end).

### 1.1. Back-end

*   **Linguagem**: Python
*   **Framework Web**: A estrutura com `app.py` e uma pasta `routes` sugere o uso de um micro-framework como **Flask** ou **FastAPI**.
*   **Gerenciamento de Dependências**: As dependências são gerenciadas através do arquivo `requirements.txt` e instaladas em um ambiente virtual Python (`.venv`), garantindo o isolamento do ambiente.
*   **Arquitetura**:
    *   **Servidor de API REST**: O back-end expõe uma API REST para o front-end consumir.
    *   **Padrão de Camadas**: O código é organizado em camadas de responsabilidade:
        *   `models`: Para a definição da estrutura de dados (ORM).
        *   `routes`: Para o roteamento das requisições HTTP.
        *   `services`: Para a lógica de negócios.
        *   `utils`: Para funções e utilitários compartilhados.

### 1.2. Front-end

*   **Linguagem**: JavaScript (com sintaxe JSX)
*   **Biblioteca Principal**: **React.js**, utilizado para construir a interface de usuário como uma Single Page Application (SPA).
*   **Gerenciamento de Pacotes**: **npm** (Node Package Manager), com os arquivos `package.json` e `package-lock.json` para gerenciar as bibliotecas e scripts do projeto.
*   **Estrutura**: O projeto foi inicializado com `create-react-app`.
*   **Arquitetura**:
    *   **Componentização**: A interface é dividida em componentes reutilizáveis.
    *   **Organização por Funcionalidade (Feature)**: O código-fonte (`src`) é estruturado em pastas por funcionalidade (`auth`, `dashboard`, `perfil`, etc.), o que facilita a escalabilidade e manutenção.
    *   **Estilização**: CSS modular, com arquivos de estilo (`.css`) específicos para cada componente.

### 1.3. Ferramentas e Ambiente

*   **Controle de Versão**: **Git**, indicado pela presença da pasta `.git`.
*   **Editor/IDE**: A pasta `.vscode` sugere o uso do Visual Studio Code como ambiente de desenvolvimento.

## 2. Requisitos Não Funcionais Implementados

*   **Modularidade e Organização**: O código é altamente modular, tanto no back-end (camadas de serviço, rotas e modelos) quanto no front-end (organização por features e componentes). Isso promove a reutilização de código e facilita a manutenção.
*   **Configurabilidade**: O back-end utiliza um arquivo `.env` e um `config.py` para externalizar configurações sensíveis (como credenciais de banco de dados) e de ambiente, evitando que sejam codificadas diretamente no código-fonte.
*   **Escalabilidade**: A arquitetura em camadas do back-end e a organização por features do front-end permitem que a aplicação cresça de forma ordenada, facilitando a adição de novas funcionalidades sem impactar as existentes.
*   **Manutenibilidade**: A separação clara de responsabilidades e a estrutura organizada tornam o código mais fácil de entender, depurar e modificar.
*   **Usabilidade (Planejamento)**: A existência da pasta `docs/prototipacao` com mockups detalhados das telas indica uma preocupação inicial com a experiência do usuário (UX) e a usabilidade do sistema, guiando o desenvolvimento da interface.
