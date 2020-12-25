# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add(Contact(firstname="Dmitriy", lastname="Belkin", address="Moscow", mobile="+79999999999", email="demetrius.belkin@gmail.com"))
    app.contact.return_to_home_page()
    app.session.logout()


def test_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add(Contact(firstname="", lastname="", address="", mobile="", email=""))
    app.contact.return_to_home_page()
    app.session.logout()

