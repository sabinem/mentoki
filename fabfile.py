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
    :return: git-tracked-file.txt
    """
    local('git rm --cached `git ls-files -i -X .gitignore`')

def git_tryclean():
    """
    stops files in gitignore from being tracked without deleting them
    :return: writes on console all files in gitignore that are still tracked
    """
    local('git ls-files -i -X .gitignore')


def stage():
    code_dir = '/srv/http/web0263/netteachers_test/netteachers'
    with cd(code_dir):
        run("git pull")
        run("touch app.wsgi")


def deploy():
    local('cp metoki/settings_production.py mentoki/settings.py')
    local('git push origin master')
    local('cp metoki/settings_test.py mentoki/settings.py')
    code_dir = '/srv/http/web0263/mentoki_live/mentoki'
    with cd(code_dir):
        run("git pull")
        run("touch app.wsgi")


def test_deploy():
    local('cp metoki/settings_production.py mentoki/settings.py')
    local('git push origin master')
    local('cp metoki/settings_test.py mentoki/settings.py')


def hello(name="world"):
    print("Hello %s!" % name)





