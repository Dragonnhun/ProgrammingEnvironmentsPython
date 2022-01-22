from kivy.uix.label import Label
from kivy.uix.popup import Popup


def invalid_login():
    popup = Popup(
        title='Invalid credentials',
        content=Label(text='Invalid username or password!'),
        size_hint=(None, None),
        size=(400, 200))

    popup.open()


def invalid_register():
    popup = Popup(
        title='Invalid input',
        content=Label(text='Please fill in all the inputs with valid information!'),
        size_hint=(None, None),
        size=(400, 200))

    popup.open()


def email_already_exists():
    popup = Popup(
        title='Email already exists',
        content=Label(text='This email address already exists in the database!'),
        size_hint=(None, None),
        size=(400, 200))

    popup.open()


def username_already_exists():
    popup = Popup(
        title='Username already exists',
        content=Label(text='This username already exists in the database!'),
        size_hint=(None, None),
        size=(400, 200))

    popup.open()
