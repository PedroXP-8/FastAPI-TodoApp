from playwright.sync_api import sync_playwright, expect
import pytest
from .models_pw import LoginPage, TodoPage

### https://ph-todoapp.onrender.com/auth/login-page ###

@pytest.fixture
def page():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        yield page

        browser.close()

def test_add_todo(page):

    login = LoginPage(page)
    login.login('coqui', 'pedro000')

    loggeed_page = TodoPage(page)
    loggeed_page.add_todo('study', 'new work', '5')


def test_delete_todo(page):

    login = LoginPage(page)
    login.login('coqui', 'pedro000')

    logged_page = TodoPage(page)
    logged_page.delete_todo('study')

def test_update_todo(page):

    login = LoginPage(page)
    login.login('coqui', 'pedro000')

    logged_page = TodoPage(page)
    logged_page.add_todo('study', 'new work', '5')

    logged_page.edit_todo('study', 'new_work on itau', '4', True)