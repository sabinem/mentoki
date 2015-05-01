from __future__ import with_statement
from fabric.api import *
from fabric.network import ssh
from fabric.contrib.console import confirm
ssh.util.log_to_file("paramiko.log", 10)

env.hosts = ['ssh.pyrox.eu']
env.user = 'web0263'

def gitlist():
    """
    makes a list of the tracked files in the current git branch
    :return: git-tracked-file.txt
    """
    local('git ls-tree --full-tree -r HEAD > projectdocs/git-tracked-files.txt')

def gitclean():
    """
    stops files in gitignore from being tracked without deleting them
    """
    local('git rm --cached `git ls-files -i -X .gitignore`')

def git_listclean():
    """
    determines whether there are files in gitignore that are still being tracked
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


def prepare_commit():
    """
    copies production settings onto settings
    """
    local('cp mentoki/settings_production.py mentoki/settings.py')

def prepare_dev():
    """
    copies dev settings onto settings
    """
    local('cp mentoki/settings_test.py mentoki/settings.py')







