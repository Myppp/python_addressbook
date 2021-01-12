# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_add_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.create(Contact(firstname="Дмитрий", middlename="Александрович", lastname="Белкин",
                                   mobilephone="+79999995445"))
        app.session.logout()


def test_add_empty_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.create(Contact(firstname="", middlename="", lastname="", mobilephone=""))
        app.session.logout()
