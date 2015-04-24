from __future__ import unicode_literals
import logging
from apps.core.cacheconfig import *
from apps.core.cache import get_cachedata, set_flag_recalc_cache
from .helpers_subforums import *


def get_forum_structure(forum_id):
    logger.debug("---------- in get_form_structure %s" % forum_id)
    return get_cachedata(
        data = forum_id,
        data_id = forum_id,
        flagcode = CACHE_FLAG_FORUM,
        datacode = CACHE_DATA_FORUM,
        function = calc_forum_structure
    )


def calc_forum_structure(forum_id):
    logger.debug("---------- in calc_forum_structure %s" % forum_id)
    forumtree = calc_menutree_forum(forum_id)
    path_lists = calc_ancestor_lists(forumtree)
    subforum_dict = calc_subforum_dict(forumtree, path_lists)
    return {
        'forumtree': forumtree,
        'path_lists': path_lists,
        'subforum_dict':subforum_dict,
    }


def recalc_forum_structure(forum_id):
    logger.debug("---------- in recalc_forum_structure %s" % forum_id)
    return set_flag_recalc_cache(
        data_id = forum_id,
        flagcode = CACHE_FLAG_FORUM,
        datacode = CACHE_DATA_FORUM,
        function = calc_forum_structure
    )


def get_thread_data(forum_id):
    logger.debug("---------- in get_thread_data %s" % forum_id)
    return get_cachedata(
        data = forum_id,
        data_id = forum_id,
        flagcode = CACHE_FLAG_THREADDATA,
        datacode = CACHE_DATA_THREADDATA,
        function = calc_thread_data
    )


def calc_thread_data(forum_id):
    logger.debug("---------- in calc_thread_data %s" % forum_id)

    thread_dict = {}
    threads = Thread.objects.filter(forum_id=forum_id).select_related('author')
    for thread in threads:
        thread_dict[thread.id] = {
            'subforum_id': thread.subforum_id,
            'last_changed': thread.created,
            'last_author': thread.author.username,
            'last_author_id': thread.author.id,
            'post_count': 0
        }
    posts = Post.objects.filter(forum_id=forum_id).select_related('author')
    for post in posts:
        if post.created > thread_dict[post.thread_id]['last_changed']:
            thread_dict[post.thread_id]['last_changed'] = post.modified
            thread_dict[post.thread_id]['last_author'] = post.author.username
            thread_dict[post.thread_id]['last_author_id'] = post.author.id
        thread_dict[post.thread_id]['post_count'] += 1
    return thread_dict



def recalc_thread_data(forum_id):
    logger.debug("---------- in recalc_thread_data %s" % forum_id)
    return set_flag_recalc_cache(
        data_id = forum_id,
        flagcode = CACHE_FLAG_THREADDATA,
        datacode = CACHE_DATA_THREADDATA,
        function = calc_thread_data
    )


def get_subforum_change(forum_id):
    logger.debug("---------- in get_subforum_change %s" % forum_id)
    return get_cachedata(
        data = forum_id,
        data_id = forum_id,
        flagcode = CACHE_FLAG_SUBFORUMCHANGE,
        datacode = CACHE_DATA_SUBFORUMCHANGE,
        function = calc_subforum_change
    )


def calc_subforum_change(forum_id):
    logger.debug("---------- in calc_subforum_change %s" % forum_id)

    subforumchange_dict = {}
    subforums = SubForum.objects.filter(forum_id=forum_id)

    for subforum in subforums:
        subforumchange_dict[subforum.id] = {
            'last_changed': None,
            'last_author': None,
            'last_author_id': None,
            'thread_count': 0
        }

    thread_dict = get_thread_data(forum_id)
    for key in thread_dict:
        thread_subforum_id = thread_dict[key]['subforum_id']
        switch = False
        try:
            if thread_dict[key]['last_changed'] > subforumchange_dict[thread_subforum_id]['last_changed']:
               switch = True
        except:
            switch = True
        if switch:
            subforumchange_dict[thread_subforum_id]['last_changed'] = thread_dict[key]['last_changed']
            subforumchange_dict[thread_subforum_id]['last_author'] = thread_dict[key]['last_author']
            subforumchange_dict[thread_subforum_id]['last_author_id'] = thread_dict[key]['last_author_id']
        subforumchange_dict[thread_subforum_id]['thread_count'] += 1
    return subforumchange_dict



def recalc_subforum_change(forum_id):
    logger.debug("---------- in recalc_subforum_change %s" % forum_id)
    return set_flag_recalc_cache(
        data_id = forum_id,
        flagcode = CACHE_FLAG_SUBFORUMCHANGE,
        datacode = CACHE_DATA_SUBFORUMCHANGE,
        function = calc_subforum_change
    )