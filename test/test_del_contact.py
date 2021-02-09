from model.contact import Contact
from random import randrange
import allure


def test_delete_some_contact(app):
    with allure.step('Given a non-empty contact list'):
        if app.contact.count() == 0:
            app.contact.create(Contact(firstname="test"))
    with allure.step('Given a random contact from the list'):
        old_contacts = app.contact.get_contact_list()
        index = randrange(len(old_contacts))
    with allure.step('When I delete the contact from the list'):
        app.contact.delete_contact_by_index(index)
    with allure.step('Then the new contact list is equal to the old list without the deleted contact'):
        assert len(old_contacts) - 1 == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts[index:index + 1] = []
        assert old_contacts == new_contacts
