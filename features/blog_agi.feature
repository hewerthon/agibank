Feature: Test Blog do Agi

    Scenario: Busca por palavra-chave
        Given O usuário acessa o site https://blogdoagi.com.br/
        When Usuário digita uma palavra-chave na barra de busca e clica no botão de pesquisar
        Then  O sistema retorna uma lista de artigos que contêm a palavra-chave pesquisada

    Scenario: Busca por categoria
        Given O usuário acessa o site https://blogdoagi.com.br/
        When Usuário clica em uma categoria específica (ex: Produtos, Serviços, Suas finanças)
        Then  O sistema retorna uma lista de artigos relacionados à categoria selecionada

    Scenario: Busca por tags
        Given O usuário acessa o site https://blogdoagi.com.br/
        When Usuário clica uma tags (ex: agi, inclusao, desenvolvimento-de-talentos)
        Then  O sistema retorna uma lista de artigos que contêm a tag

    Scenario: Busca por autor
        Given O usuário acessa o site https://blogdoagi.com.br/
        When Usuário clica em um autor (ex: CONTEUDOAGI, REDACAOAGI)
        Then O sistema retorna uma lista de artigos escritos pelo autor