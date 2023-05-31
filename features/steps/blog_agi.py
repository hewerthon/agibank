from behave import given, when, then
from page_object.page_object import BlogdoAGIPage


@given(u'O usuário acessa o site https://blogdoagi.com.br/')
def go_to_page(context):
    context.blog_page = BlogdoAGIPage(context.browser)
    context.blog_page.go_to_page()


@when(u'Usuário digita uma palavra-chave na barra de busca e clica no botão de pesquisar')
def step_impl(context):
    context.blog_page.search_keyword('Agibank')


@then(u'O sistema retorna uma lista de artigos que contêm a palavra-chave pesquisada')
def check_result(context):
    assert 'Resultados da busca por: Agibank' in context.blog_page.get_search_results_title()
    assert 10 == context.blog_page.get_article_count()
    assert context.blog_page.check_category_in_articles('NOSSO AGI')


@when(u'Usuário clica em uma categoria específica (ex: Produtos, Serviços, Suas finanças)')
def step_impl(context):
    context.blog_page.click_category('584')


@then(u'O sistema retorna uma lista de artigos relacionados à categoria selecionada')
def check_result(context):
    assert 'Categoria: Produtos' in context.blog_page.get_search_results_title()
    assert 10 == context.blog_page.get_article_count()
    assert context.blog_page.check_category_in_articles('PRODUTOS')


@when(u'Usuário clica uma tags (ex: agi, inclusao, desenvolvimento-de-talentos)')
def step_impl(context):
    context.blog_page.click_tag('agi')


@then(u'O sistema retorna uma lista de artigos que contêm a tag')
def check_result(context):
    assert 'Tag: agi' in context.blog_page.get_tag_results_title()
    assert 10 == context.blog_page.get_article_count()
    '''
    Não é possivel verificar lista de categoras pelas tags porque a publicação https://blogdoagi.com.br/2023/04/26/dia-combate-hipertensao/
    Não está dentro da Tag AGI
    assert context.blog_page.check_category_in_articles('AGI')
    '''


@when(u'Usuário clica em um autor (ex: CONTEUDOAGI, REDACAOAGI)')
def step_impl(context):
    context.blog_page.click_author('conteudoagi')


@then(u'O sistema retorna uma lista de artigos escritos pelo autor')
def check_result(context):
    assert 'Autor: conteudoagi' in context.blog_page.get_search_results_title()
    assert 10 == context.blog_page.get_article_count()
