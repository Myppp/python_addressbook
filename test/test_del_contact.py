def test_del_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.contact.return_to_home_page()
    app.session.logout()
