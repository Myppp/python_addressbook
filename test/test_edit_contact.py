from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="EditedName", middlename="EditedMiddlename",
                                           lastname="EditedLastname", mobilephone="+7779991234"))
    app.session.logout()


def test_edit_first_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="EditedFirstName"))
    app.session.logout()


def test_edit_first_contact_middlename(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(middlename="EditedFirstMiddlename"))
    app.session.logout()
