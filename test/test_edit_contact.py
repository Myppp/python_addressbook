from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="EditedName", middlename="Edited", lastname="EditedLastname",
                                           mobilephone="+78888888545"))
    app.session.logout()
