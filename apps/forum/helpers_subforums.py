from __future__ import unicode_literals
import logging
import copy
from .models import SubForum, Thread, Post, display_ancestors


logger = logging.getLogger(__name__)


def calc_menutree_forum(forum_id):
    # main function
    subforums = SubForum.objects.filter(parentforum=None, forum_id=forum_id).order_by('display_nr')
    if not subforums.exists():
        return None
    else:
        list = []
        for item in subforums:
            list.append(calc_menutree_subforum(item))
        return list


def calc_menutree_subforum(subforum):
    # helper function
    subforums = SubForum.objects.filter(parentforum=subforum.id, forum_id=subforum.forum_id).order_by('display_nr')
    title = subforum.title
    if not subforums.exists():
        return {'title': title, 'is_leaf':True, 'id':subforum.id, 'display_nr':subforum.display_nr }
    else:
        list = []
        for item in subforums:
            list.append(calc_menutree_subforum(item))
        return {'title': title, 'is_leaf': False, 'list': list, 'id':subforum.id, 'display_nr':subforum.display_nr }


def calc_subforum_dict(forumtree, path_lists):
    subforum_dict = {}
    try:
        for item in forumtree:
            subforum_dict = add_item_to_dict(path_lists, subforum_dict, item)
        return subforum_dict
    except:
        return None


def add_item_to_dict(path_lists, subforum_dict, item):
    ancestors = subforum_ancestors(path_lists, item['id'])
    subforum_dict[item['id']] = {
        'title': item['title'],
        'is_leaf': item['is_leaf'],
        'id':item['id'],
        'display_nr': item['display_nr'],
        'ancestors':ancestors,
        'depth_below':calc_depth_below(path_lists,item['id']),
        'depth_above':len(ancestors),
        'decendants':descendants(path_lists, item['id']),
    }
    if item['is_leaf'] == True:
        return subforum_dict
    else:
        for listitem in item['list']:
            subforum_dict = add_item_to_dict(path_lists, subforum_dict, listitem)
        return subforum_dict

#main function: output: path_lists
def calc_ancestor_lists(forumtree):
    ancestor_lists = []
    try:
        for item in forumtree:
            item_ancestor_lists = add_decendants_to_ancestor_list([],item)
            ancestor_lists += item_ancestor_lists
        return ancestor_lists
    except:
        return None


# helper function
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

def calc_depth_below(path_lists,id):
    depth_list = []
    for list in path_lists:
        try:
            depth = len(list) - list.index(id) - 1
            depth_list.append(depth)
        except:
            pass
    max_depth = max(depth_list)
    return max_depth





#main function
def descendants(path_list,id):
    result = set()
    for path in path_list:
        result = result | descendants_in_path(path, id)
    return list(result)


# helper function
def descendants_in_path(path,id):
    for i in range(len(path)):
        if path[i]==id:
            return set(path[i:])
    return set()




# helper_function
# returns None if id does not appear in any path
def ancestors_in_path(path, id):
    for i in range(len(path)):
        if path[i]==id:
            return path[:i]
    return None

# main_function
def subforum_ancestors(path_list,id):
    for path in path_list:
        result = ancestors_in_path(path,id)
        if result != None:
            return result
    return None


# returns None if id not found
def calc_subtree(forumtree, id):
    for node in forumtree:
        if node['id']==id:
            return node
    for node in forumtree:
        if not node['is_leaf']:
            result = calc_subtree(node['list'],id)
            if result != None:
                return result
    return None



def calc_subforum_enriched_list(id_list, subforum_dict):
        enriched_list = []
        for id in id_list:
            enriched_list.append(
                {
                    'id':id,
                    'title':subforum_dict[id]['title'],
                }
            )
        return enriched_list