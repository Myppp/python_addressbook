from model.group import Group
from random import randrange
import allure


def test_edit_some_group(app):
    with allure.step('Given a non-empty group list'):
        if app.group.count() == 0:
            app.group.create(Group(name="test"))
        old_groups = app.group.get_group_list()
    with allure.step('Given a random group from the list'):
        index = randrange(len(old_groups))
    with allure.step('When I edit the group from the list'):
        group = Group(name="testname2", header="testheader2", footer="testfooter2")
        group.id = old_groups[index].id
        app.group.edit_group_by_index(index, group)
    with allure.step('Then the new group list is equal to the old list without the edit group'):
        assert len(old_groups) == app.group.count()
        new_groups = app.group.get_group_list()
        old_groups[index] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)