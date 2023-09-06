# Pokemon Scraper

Este é um projeto Python que realiza a raspagem de dados sobre Pokémon a partir do site [Serebii](https://www.serebii.net/pokemon/nationalpokedex.shtml) e salva esses dados em formato JSON e texto. O projeto utiliza bibliotecas como `requests`, `BeautifulSoup`, `dataclasses`, e `json` para realizar a tarefa de raspagem e persistência dos dados.

## Funcionalidades

### Classe `Pokemon`

A classe `Pokemon` é uma classe de dados que representa informações sobre um Pokémon. Ela possui os seguintes campos:

- `id`: O ID do Pokémon.
- `name`: O nome do Pokémon.
- `type`: Uma lista de tipos do Pokémon.
- `abilities`: Uma lista de habilidades do Pokémon.
- `bs_hp`, `bs_att`, `bs_def`, `bs_s_att`, `bs_s_def`, `bs_spd`: Os valores de estatísticas base do Pokémon.

Além disso, a classe possui um método `json` que converte uma instância de `Pokemon` em uma representação JSON.

### Função `get_html(url)`

Esta função recebe uma URL como entrada e faz uma solicitação HTTP para obter o HTML da página correspondente. Ela retorna o conteúdo HTML da página como uma string.

### Função `parse_html(html)`

Esta função recebe o HTML da página como entrada e utiliza a biblioteca BeautifulSoup para analisar o HTML. Ela retorna um objeto BeautifulSoup que pode ser usado para buscar informações específicas na página.

### Função `parse_pokemon_type(pokemon_data)`

Esta função recebe dados de Pokémon como entrada e analisa os tipos do Pokémon. Ela extrai os tipos dos links encontrados nos dados do Pokémon e retorna uma lista de tipos em formato de texto.

### Função `parse_pokemon_info(pokemon_data)`

Esta função recebe dados de Pokémon como entrada e cria uma instância da classe `Pokemon` com as informações extraídas dos dados. Ela utiliza outras funções auxiliares para extrair informações como tipos e habilidades.

### Função `save_on_json(pokemons)`

Esta função recebe uma lista de objetos `Pokemon` e os salva em um arquivo JSON chamado "pokemons.json". Cada objeto `Pokemon` é serializado em formato JSON e o arquivo resultante contém uma lista de todos os Pokémon.

### Função `save_on_text(pokemons)`

Esta função recebe uma lista de objetos `Pokemon` e os salva em arquivos de texto individuais dentro do diretório "./pokemons". Cada arquivo de texto contém informações detalhadas sobre um Pokémon, incluindo ID, nome, tipos e estatísticas de base.

### Função `main()`

A função `main()` é a função principal do projeto. Ela realiza as seguintes etapas:

1. Obtém o HTML da página da National Pokédex do site Serebii.
2. Analisa o HTML para extrair informações sobre os Pokémon.
3. Cria objetos `Pokemon` com as informações extraídas.
4. Salva os Pokémon em um arquivo JSON e em arquivos de texto individuais.

### Executando o Projeto

Para executar o projeto, siga os passos abaixo:

1. Clone este repositório em sua máquina local:

    ```bash
    git clone https://github.com/Diegiwg/serebii-pokemon.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd serebii-pokemon
    ```

3. Instale as dependências a partir do arquivo `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

4. Execute o script Python:

    ```bash
    python serebii-pokemon.py
    ```

Após a execução bem-sucedida, você terá um arquivo "pokemons.json" contendo os dados em formato JSON e arquivos de texto individuais dentro do diretório "./pokemons" com informações detalhadas sobre cada Pokémon.

Este é um projeto de raspagem de dados básico que pode ser estendido para obter mais informações sobre Pokémon ou adaptado para outros sites. Certifique-se de cumprir os termos de uso do site ao realizar raspagem de dados da web.
