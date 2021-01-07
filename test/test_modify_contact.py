# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_contact(Contact(firstname="NoDmitriy", lastname="BelkinMod", address="Russia, Moscow", mobile="+78988555874", email="testmodify@mail.ru"))
    app.session.logout()


def test_modify_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_contact(Contact(firstname="", lastname="", address="", mobile="", email=""))
    app.session.logout()