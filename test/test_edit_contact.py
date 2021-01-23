from model.contact import Contact
from random import randrange


def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="EditedName", middlename="EditedMiddleName", lastname="EditedLastname",
                      address="Россия, г.Москва", address2="Узбекистан, г.Ташкент",
                      email="email@mail.ru", email2="email2@mail.ru", email3="email3@mail.ru",
                      homephone="+7989891234", mobilephone="+7779991234", workphone="+9999991234",
                      secondaryphone="+7989991234")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)