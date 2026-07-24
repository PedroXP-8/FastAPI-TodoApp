from playwright.sync_api import sync_playwright
import time

### https://ph-todoapp.onrender.com/auth/login-page ###

with sync_playwright() as pw:

    navegador = pw.chromium.launch(headless=False)
    contexto = navegador.new_context()

    pagina = contexto.new_page()
    pagina.goto('https://ph-todoapp.onrender.com/auth/login-page')
    time.sleep(2)

    pagina.locator("input[name=\"username\"]").fill("coqui")
    pagina.locator("input[name=\"password\"]").fill("pedro000")
    time.sleep(2)

    botao1 = pagina.get_by_role("button", name="Login")
    botao1.click()

    pagina.wait_for_url('**/todo-page')
    time.sleep(2)

    botao2 = pagina.get_by_role("link", name="Add a new todo")
    botao2.click()

    pagina.wait_for_url('**/add-todo-page')
    time.sleep(2)

    pagina.locator("input[name=\"title\"]").fill("haircut")
    pagina.locator("textarea[name=\"description\"]").fill("o look lke a homeless")
    pagina.get_by_role("combobox").select_option("4")

    time.sleep(2)

    pagina.get_by_role("button", name="Add new todo").click()

    time.sleep(2)

    botao4 = pagina.get_by_role("link", name="Back")
    botao4.click()

    pagina.wait_for_url('**/todo-page')

    time.sleep(3)

    navegador.close()