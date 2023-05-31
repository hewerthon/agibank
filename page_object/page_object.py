from selenium.webdriver.common.by import By


class BlogdoAGIPage:
    def __init__(self, browser):
        self.browser = browser

    def go_to_page(self):
        self.browser.get('https://blogdoagi.com.br/')

    def search_keyword(self, keyword):
        search_btn = self.browser.find_element(By.ID, 'search-open')
        search_btn.click()
        search_field = self.browser.find_element(By.CLASS_NAME, 'search-field')
        search_field.send_keys(keyword)
        search_submit = self.browser.find_element(By.CLASS_NAME, 'search-submit')
        search_submit.click()

    def click_category(self, category):
        category_link = self.browser.find_element(By.ID, f'menu-item-{category}')
        category_link.click()

    def click_tag(self, tag):
        self.browser.get(f'https://blogdoagi.com.br/tag/{tag}')

    def click_author(self, author):
        self.browser.get(f'https://blogdoagi.com.br/author/{author}')

    def get_search_results_title(self):
        archive_title = self.browser.find_element(By.CLASS_NAME, 'archive-title').text
        return archive_title

    def get_article_count(self):
        tag_articles = self.browser.find_elements(By.XPATH, '//article')
        return len(tag_articles)

    def check_category_in_articles(self, category):
        tag_categories = self.browser.find_elements(By.CLASS_NAME, 'entry-cats')
        for category_element in tag_categories:
            if category not in category_element.text:
                return False
        return True

    def get_tag_results_title(self):
        archive_title = self.browser.find_element(By.CLASS_NAME, 'archive-title').text
        return archive_title

    def check_author_in_articles(self):
        archive_title = self.browser.find_element(By.CLASS_NAME, 'archive-title').text
        return archive_title
