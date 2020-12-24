# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_contact(app):
    app.login(username="admin", password="secret")
    app.add_contact(Contact(firstname="Dmitriy", lastname="Belkin", address="Moscow", mobile="+79999999999", email="demetrius.belkin@gmail.com"))
    app.return_to_home_page()
    app.logout()


def test_empty_contact(app):
    app.login(username="admin", password="secret")
    app.add_contact(Contact(firstname="", lastname="", address="", mobile="", email=""))
    app.return_to_home_page()
    app.logout()

