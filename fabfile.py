from __future__ import with_statement
from fabric.api import *
from fabric.network import ssh
from fabric.contrib.console import confirm
ssh.util.log_to_file("paramiko.log", 10)

env.hosts = ['ssh.pyrox.eu']
env.user = 'web0263'

def gitclean():
    """
    stops files in gitignore from being tracked without deleting them
    """
    local('git rm --cached `git ls-files -i -X .gitignore`')

def gitlist():
    """
    shows files that are in gitignore, but tracked or commited
    """
    local('git ls-files -i --exclude-standard')


def gitlist2():
    """
    shows files that are in gitignore, but tracked or commited
    """
    local('git ls-files -i -X .gitignore')

def stage():
    """
    employs mentoki repo to mentoki_test
    """
    code_dir = '/srv/http/web0263/mentoki_test/mentoki'
    with cd(code_dir):
        run("git pull")
        run("touch app.wsgi")


def deploy():
    """
    employs mentoki repo to mentoki_live
    """
    code_dir = '/srv/http/web0263/mentoki_live/mentoki'
    with cd(code_dir):
        run("git pull")
        run("touch app.wsgi")


def livedata():
    """
    gets data from the live website
    """
    get(remote_path="/srv/http/web0263/tools/live.sql", local_path="../mentoki_tools/./live.sql")











