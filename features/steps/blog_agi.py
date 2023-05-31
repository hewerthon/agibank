from behave import given, when, then
from selenium.webdriver.common.by import By

url = 'https://blogdoagi.com.br/'
url_tag = 'https://blogdoagi.com.br/tag/agi'
url_autor = 'https://blogdoagi.com.br/author/conteudoagi/'
search_btn = 'search-open'
search_field = 'search-field'
search_submit = 'search-submit'
archive_title = 'archive-title'
product = 'menu-item-584'


@given(u'O usuário acessa o site https://blogdoagi.com.br/')
def go_to_page(context):
    context.browser.get(url)


@when(u'Usuário digita uma palavra-chave na barra de busca e clica no botão de pesquisar')
def step_impl(context):
    context.browser.find_element(By.ID, search_btn).click()
    context.browser.find_element(By.CLASS_NAME, search_field).send_keys('Agibank')
    context.browser.find_element(By.CLASS_NAME, search_submit).click()


@then(u'O sistema retorna uma lista de artigos que contêm a palavra-chave pesquisada')
def check_result(context):
    assert 'Resultados da busca por: Agibank' in context.browser.find_element(By.CLASS_NAME, archive_title).text


@when(u'Usuário clica em uma categoria específica (ex: Produtos, Serviços, Suas finanças)')
def step_impl(context):
    context.browser.find_element(By.ID, product).click()


@then(u'O sistema retorna uma lista de artigos relacionados à categoria selecionada')
def check_result(context):
    assert 'Categoria: Produtos' in context.browser.find_element(By.CLASS_NAME, archive_title).text


@when(u'Usuário clica uma tags (ex: agi, inclusao, desenvolvimento-de-talentos)')
def step_impl(context):
    context.browser.get(url_tag)


@then(u'O sistema retorna uma lista de artigos que contêm a tag')
def check_result(context):
    assert 'Tag: agi' in context.browser.find_element(By.CLASS_NAME, archive_title).text


@when(u'Usuário clica em um autor (ex: CONTEUDOAGI, REDACAOAGI)')
def step_impl(context):
    context.browser.get(url_autor)


@then(u'O sistema retorna uma lista de artigos escritos pelo autor')
def check_result(context):
    assert 'Autor: conteudoagi' in context.browser.find_element(By.CLASS_NAME, archive_title).text
