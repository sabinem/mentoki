import logging
from django.core.cache import cache
from .cacheconfig import *


logger = logging.getLogger(__name__)


def get_cachedata(data, data_id, flagcode, datacode, function):
    logger.debug("---------- in get_cachedata for id = %s function= %s" % (data_id, function))

    # necessary to recalculate? (smt = subforum menu tree)
    flagkey = get_cache_key(code=flagcode, data_id=data_id)
    datakey = get_cache_key(code=datacode, data_id=data_id)
    status = cache.get(flagkey)
    logger.debug("       status is %s" % status)
    # compute from scratch


    if status == CACHE_GOOD_DATA:
        logger.debug("---------- use cache")
        result = cache.get(datakey)
    else:
        logger.debug("---------- recalculate cache")
        # compute from scratch
        result = function(data)
        cache.set(datakey, result)
        cache.set(flagkey, CACHE_GOOD_DATA)
        logger.debug("---------- new result from cache")
    return result


def set_flag_recalc_cache(data_id, flagcode, datacode, function):
    logger.debug("---------- in set_recalcflag %s %s function= %s" % (flagcode, datacode, function))
    flagkey = get_cache_key(code=flagcode, data_id=data_id)
    cache.set(flagkey, CACHE_BAD_DATA)
    return None


def get_cache_key(code, data_id):
    return code + "+" + str(data_id)