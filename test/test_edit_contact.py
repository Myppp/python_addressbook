from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Unknown"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(firstname="EditedName", middlename="EditedMiddleName",
                                           lastname="EditedLastname", mobilephone="+7779991234"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Unknown"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(firstname="EditedFirstName2"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_first_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Unknown"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(middlename="EditedFirstMiddleName2"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
