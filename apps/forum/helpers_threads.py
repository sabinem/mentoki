from __future__ import unicode_literals
import logging
from .models import Thread, Post
from .helpers_subforums import subforum_ancestors, calc_subforum_enriched_list


logger = logging.getLogger(__name__)


def enrich_subforum_dict(forum_id, subforum_dict):
    threads = Thread.objects.filter(forum_id=forum_id)

    if subforum_dict:
        for thread in threads:

            try:
                subforum_dict[thread.subforum_id]['threadcount']+=1
            except:
                subforum_dict[thread.subforum_id]['threadcount']=1
        return subforum_dict
    else:
        return None


def calc_enrich_forumtree(tree, enriched_subforum_dict):
    # tree as it comes from calc_menutree_forum or calc_menutree_subforum
    result_list = []
    try:
        for item in tree:
            result_list.append(calc_enrich_subforumtree_dict(item,enriched_subforum_dict))
        return result_list
    except:
        return None

def calc_enrich_subforumtree_dict(tree_dict, enriched_subforum_dict):
    # tree as it comes from calc_menutree_forum or calc_menutree_subforum
    # {'title': title, 'is_leaf':True, 'id':subforum.id,  }
    # {'title': title, 'is_leaf': False, 'list': list, 'id':subforum.id }
    try:
        thread_count = enriched_subforum_dict[tree_dict['id']]['threadcount']
    except:
        thread_count = 0
    tree_dict['count'] = " ( " + str(thread_count) + " ) "
    if tree_dict['is_leaf']:
        if thread_count > 0:
           tree_dict['status'] = "active"
    else:
        #has list:
        for dict in tree_dict['list']:
            calc_enrich_subforumtree_dict(dict,enriched_subforum_dict)
    return tree_dict


