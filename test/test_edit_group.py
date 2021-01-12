from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="UnknownGroupName"))
    app.group.edit_first_group(Group(name="EditedGroupName", header="EditedGroupHeader", footer="EditedGroupFooter"))


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="UnknownGroupName1"))
    app.group.edit_first_group(Group(name="EditedGroupName"))


def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="UnknownGroupName2"))
    app.group.edit_first_group(Group(header="EditedGroupHeader"))