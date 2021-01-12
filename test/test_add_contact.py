# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_add_contact(app):
        app.contact.create(Contact(firstname="Дмитрий", middlename="Александрович", lastname="Белкин",
                                   mobilephone="+79998881234"))


def test_add_empty_contact(app):
        app.contact.create(Contact(firstname="", middlename="", lastname="", mobilephone=""))