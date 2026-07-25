import re

class LoginPage:

    def __init__(self, page):
        self.page = page

    def login(self, user, password):

        self.page.goto('https://ph-todoapp.onrender.com/auth/login-page')

        self.page.locator("input[name=\"username\"]").fill(user)

        self.page.locator("input[name=\"password\"]").fill(password)

        botao1 = self.page.get_by_role("button", name="Login")

        botao1.click()

class TodoPage:

    def __init__(self,page):
        self.page = page

    def add_todo(self, title : str, description : str, priority:int):

        self.page.wait_for_url('**/todo-page')
        botao2 = self.page.get_by_role("link", name="Add a new todo")
        botao2.click()
    
        self.page.wait_for_url('**/add-todo-page')
        self.page.locator("input[name=\"title\"]").fill(title)
        self.page.locator("textarea[name=\"description\"]").fill(description)
        self.page.get_by_role("combobox").select_option(priority)
        self.page.get_by_role("button", name="Add new todo").click()
    
        botao4 = self.page.get_by_role("link", name="Back")
    
        botao4.click()

        self.page.wait_for_url('**/todo-page')

    def delete_todo(self, title : str):

        self.page.wait_for_url('**/todo-page')

        line = self.page.get_by_role("row", name=re.compile(title))
        line.get_by_role("button", name="Edit").click()
        self.page.wait_for_url('**/edit-todo-page/*')

        self.page.get_by_role("button", name="Delete").click()
        self.page.wait_for_url('**/todo-page')

    def edit_todo(self, title, description=None, priority=None, complete=None):

        self.page.wait_for_url('**/todo-page')

        line = self.page.get_by_role("row", name=re.compile(title))
        line.get_by_role("button", name="Edit").click()

        self.page.wait_for_url('**/edit-todo-page/*')

        if title is not None:
            campo = self.page.locator("input[name='title']")
            campo.clear()
            campo.fill(title)

        if description is not None:
            campo = self.page.locator("textarea[name='description']")
            campo.clear()
            campo.fill(description)

        if priority is not None:
            self.page.get_by_role("combobox").select_option(str(priority))

        if complete is not None:
            campo = self.page.get_by_role("checkbox")
            if complete == True:
                campo.check()
            elif complete == False:
                campo.uncheck()
    
        self.page.get_by_role("button", name="Edit your todo").click()

        self.page.wait_for_url('**/todo-page')


    