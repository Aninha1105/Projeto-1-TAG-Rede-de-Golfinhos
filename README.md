# Projeto 1 de Teoria e Aplicação de Grafos - Rede de Golfinhos

## Introdução

Este projeto analisa uma rede social de associações duradouras em uma comunidade de 62 golfinhos, representada como um grafo não direcionado. Utilizando dados de um arquivo (`soc-dolphins.mtx`), o programa constrói o grafo e realiza análises, como:

1. Grau de cada vértice (representando o número de conexões de cada golfinho).
2. Identificação e exibição de todos os cliques maximais.
3. Cálculo do Coeficiente de Aglomeração de cada vértice.
4. Cálculo do Coeficiente médio de Aglomeração do grafo.
5. Geração de uma visualização do grafo, com cores distintas para cada clique maximal.

## Requisitos

Este projeto foi desenvolvido em Python 3.9.6 e utiliza as seguintes bibliotecas:

- `networkx` para manipulação do grafo.
- `matplotlib.pyplot` para visualização do grafo.
- `numpy` para operações numéricas.
- `imageio.v2` para criação de um GIF que destaca visualmente os cliques maximais.
- `os` para manipulação de diretórios e arquivos.
- `scipy`: para operações matemáticas e científicas avançadas.

## Como Executar o Projeto

### 1. **Abrir o Projeto**

- Abra o terminal.
- Navegue até a pasta onde o projeto está localizado:
    
    ```
    cd /caminho/para/o/projeto
    ```
    

### 2. Configurar e **Ativar o Ambiente Virtual**

O projeto utiliza um ambiente virtual para garantir que as dependências e pacotes necessários estejam isolados e não interfiram em outros projetos.

### Criar o Ambiente Virtual:

- Para criar o ambiente virtual, execute o seguinte comando no terminal:
    
    ```
    python3 -m venv venv
    ```
    
Esse comando cria uma pasta chamada `venv` com todos os arquivos necessários para o ambiente virtual.
    

### No macOS ou Linux:

- Ative o ambiente virtual com o seguinte comando:
    
    ```
    source venv/bin/activate
    ```
    

### No Windows:

- Ative o ambiente virtual com o comando:
    
    ```
    venv\Scripts\activate
    ```
    

Após executar o comando de ativação, o nome do seu ambiente virtual (normalmente `venv`) aparecerá entre parênteses no terminal, indicando que o ambiente virtual está ativo.

### 3. **Instalar as Dependências**

Se você nunca instalou as dependências do projeto, ou se está começando a configurar o ambiente, basta rodar o seguinte comando:

    ```
    pip install -r requirements.txt
    ```

Isso irá instalar todas as bibliotecas e pacotes necessários para o seu projeto.

### 4. **Executar o Projeto**

Com o ambiente virtual ativado e as dependências instaladas, execute o seu código Python com:

    ```
    python projeto1.py
    ```

Isso irá rodar o programa conforme o que está no arquivo `projeto1.py`.

### 5. **Fechar o Ambiente Virtual**

Após terminar de trabalhar com o projeto, você pode desativar o ambiente virtual com o comando:

    ```
    deactivate
    ```

Isso irá sair do ambiente virtual e retornar ao terminal normal.
