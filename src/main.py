from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen

from database import database
from src.error import invalid_login, invalid_register, email_already_exists, username_already_exists


# MAIN WINDOW

class MainWindow(Screen):
    identifier = ObjectProperty(None)
    username = ObjectProperty(None)
    email = ObjectProperty(None)

    def logout_button(self):
        self.reset()
        screen_manager.current = "login_window"

    def reset(self):
        self.identifier.text = ""
        self.username.text = ""
        self.email.text = ""


# LOGIN WINDOW

class LoginWindow(Screen):
    username_or_email = ObjectProperty(None)
    password = ObjectProperty(None)

    def login_button(self):
        if database.validate_user(self.username_or_email.text, self.password.text):
            user = database.get_user(self.username_or_email.text, self.password.text)

            App.get_running_app().root.screens[2].identifier.text = "ID: " + str(user[0][0])
            App.get_running_app().root.screens[2].username.text = "Username: " + user[0][1]
            App.get_running_app().root.screens[2].email.text = "Email: " + user[0][2]

            self.reset()
            screen_manager.current = "main_window"
        else:
            invalid_login()

    def register_button(self):
        self.reset()
        screen_manager.current = "register_window"

    def reset(self):
        self.username_or_email.text = ""
        self.password.text = ""


# REGISTER WINDOW

class RegisterWindow(Screen):
    username = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit_button(self):
        if self.username.text != "" and \
                self.email.text != "" and \
                self.email.text.count("@") == 1 and \
                self.email.text.count(".") > 0 and \
                self.password != "":
            if database.check_email_address(self.email.text):
                email_already_exists()
            elif database.check_username(self.username.text):
                username_already_exists()
            else:
                database.add_user(self.username.text, self.email.text, self.password.text)

                self.reset()

                screen_manager.current = "login_window"
        else:
            invalid_register()

    def login_button(self):
        self.reset()
        screen_manager.current = "login_window"

    def reset(self):
        self.username.text = ""
        self.email.text = ""
        self.password.text = ""


# MAIN

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("../kv/properties.kv")

screen_manager = WindowManager()

screens = [LoginWindow(name="login_window"), RegisterWindow(name="register_window"), MainWindow(name="main_window")]

for screen in screens:
    screen_manager.add_widget(screen)

screen_manager.current = "login_window"


class MainApp(App):
    def build(self):
        return screen_manager


if __name__ == "__main__":
    MainApp().run()
