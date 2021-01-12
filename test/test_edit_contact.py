from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Unknown"))
    app.contact.edit_first_contact(Contact(firstname="EditedName", middlename="EditedMiddleName",
                                           lastname="EditedLastname", mobilephone="+7779991234"))


def test_edit_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Unknown"))
    app.contact.edit_first_contact(Contact(firstname="EditedFirstName2"))


def test_edit_first_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Unknown"))
    app.contact.edit_first_contact(Contact(middlename="EditedFirstMiddleName2"))
