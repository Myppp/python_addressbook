from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="UnknownGroupName"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="EditedGroupName", header="EditedGroupHeader", footer="EditedGroupFooter"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="UnknownGroupName1"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="EditedGroupName"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="UnknownGroupName2"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(header="EditedGroupHeader"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)