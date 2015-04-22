from __future__ import unicode_literals
import copy
from .models import SubForum, Thread, Post, display_ancestors



def calc_menutree_forum(forum_id):
    # builds the subforum tree form the top
    subforums = SubForum.objects.filter(parentforum=None, forum_id=forum_id).order_by('display_nr')
    if not subforums.exists():
        return None
    else:
        list = []
        for item in subforums:
            list.append(calc_menutree_subforum(item))
        return list


def calc_menutree_subforum(subforum):
    # build the subforum tree for any real subforum
    subforums = SubForum.objects.filter(parentforum=subforum.id, forum_id=subforum.forum_id).order_by('display_nr')
    title = subforum.title
    if not subforums.exists():
        return {'title': title, 'is_leaf':True, 'id':subforum.id,  }
    else:
        list = []
        for item in subforums:
            list.append(calc_menutree_subforum(item))
        return {'title': title, 'is_leaf': False, 'list': list, 'id':subforum.id }


def calc_real_decendant_ids(subforum_id_list):
    # build the subforum list for any real subforum
    result_qslist = SubForum.objects.filter(parentforum_id__in=subforum_id_list).values_list('id', flat=True)
    result_list = list(result_qslist)
    if result_list == []:
        return result_list
    else:
        addon_list = calc_real_decendant_ids(result_list)
        return result_list + addon_list


def calc_subforum_thread_count(subforum_id):
    count = Thread.objects.filter(subforum_id=subforum_id).count()
    return count


def calc_ancestor_lists(forumtree):
    ancestor_lists = []
    for item in forumtree:
        item_ancestor_lists = add_decendants_to_ancestor_list([],item)
        ancestor_lists += item_ancestor_lists
    return ancestor_lists


def add_decendants_to_ancestor_list(ancestor_list,item):
    new_list = copy.copy(ancestor_list)
    new_list.append(item['id'])
    if item['is_leaf'] == True:
        return [new_list]
    else:
        ancestor_lists = []
        for listitem in item['list']:
            item_ancestor_lists = add_decendants_to_ancestor_list(new_list,listitem)
            ancestor_lists += item_ancestor_lists

        return ancestor_lists


def calc_ancestor_lists(forumtree):
    ancestor_lists = []
    for item in forumtree:
        item_ancestor_lists = add_decendants_to_ancestor_list([],item)
        ancestor_lists += item_ancestor_lists
    return ancestor_lists


def add_decendants_to_ancestor_list(ancestor_list,item):
    ancestor_list.append(item['id'])
    if item['is_leaf'] == True:
        return [ancestor_list]
    else:
        ancestor_lists = []
        for listitem in item['list']:
            item_ancestor_lists = add_decendants_to_ancestor_list(ancestor_list,listitem)
            ancestor_lists += item_ancestor_lists

        return ancestor_lists