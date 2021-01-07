from model.group import Group


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.open_edit_form_for_first()
    app.group.modify_group(Group(name="ModifyGroupName", header="ModifyGroupHeader", footer="ModifyGroupFooter"))
    app.session.logout()