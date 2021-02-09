from model.contact import Contact
from random import randrange
import allure


def test_edit_some_contact(app):
    with allure.step('Given a non-empty contact list'):
        if app.contact.count() == 0:
            app.contact.create(Contact(firstname="test"))
    with allure.step('Given a random contact from the list'):
        old_contacts = app.contact.get_contact_list()
        index = randrange(len(old_contacts))
        contact = Contact(firstname="testfirstname2", middlename="testmiddlename2", lastname="testlastname2",
                          address="2 test address 1", address2="2 test address 2",
                          email="2email@mail.ru", email2="2email2@mail.ru", email3="2email3@mail.ru",
                          homephone="72000000000", mobilephone="72000000001", workphone="72000000002",
                          secondaryphone="72000000003")
        contact.id = old_contacts[index].id
    with allure.step('When I edit the contact with <firstname>, <lastname> and <middlename>'):
        app.contact.edit_contact_by_index(index, contact)
    with allure.step('Then the new contact list is equal to the old list with the edited contact'):
        assert len(old_contacts) == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts[index] = contact
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
