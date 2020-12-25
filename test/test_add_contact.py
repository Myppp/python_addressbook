# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


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

