#!/usr/bin/python
#
# This script aims to make git UI more user friendly. 
# Python 2.4+ is required to run it.
#
# Any suggestions and comments are strongly welcomed. E-mail: jonas.fiala@gmail.com
import sys
from os import system
from time import sleep
from optparse import  OptionParser

SCRIPT_USAGE = 'Usage: %prog [options]'
EXIT_OK = 0
EXIT_OPTIONS_ERROR = 1

"""
TODO:

0. Use subprocess module function(s) instead of os.system() call.
1. proxy command fgit <command> params, in case of when no custom command is not present.
2. fgit his[tory] [filename] [origos paranetry gitu]  >> git log -p filename 
3. --show or something like that.. dry run which shows which git equivalent to fgit call.
4. git log --stat  (Shows change statistics)
5. create new branch (local) and equivalent remote branch via one command.
    git branch mynewbranch
    git push origin mynewbranch
    git branch --track mynewbranch origin/mynewbranch

    >> git newbr[anch] [remote-name/]branch-name
6. Deleting branch (local or remote accordingly to / is present or not)
    >> git delbr[anch] [remote-name/]branch-name
"""

def create_new_branch_synced_with_remote_branch(option, option_string, value, parser):
    " http://book.git-scm.com/4_tracking_branches.html "
    # git branch --track experimental origin/experimental
    branch_name = None
    if len(parser.rargs) >= 1:
        branch_name = parser.rargs[0]
    if type(branch_name) in (str, unicode):
        system('git branch --track %(name)s origin/%(name)s' % {'name': branch_name})
    else:
        raise ValueError('You must specify branch name to create and synchronize.')

def print_status(option, option_string, value, parser):
    params = None
    if len(parser.rargs) >= 1:
        params = parser.rargs[0]
    if type(params) in (str, unicode):
        system('git status %s' % params)
    else:
        system('git status -a')

def print_branches(option, option_string, value, parser):
    system('git branch -a')

def push(*args):
    system('git push')

def pull(*args):
    system('git pull')

def switch_branch(option, option_string, value, parser):
    branch_name = None
    if len(parser.rargs) >= 1:
        branch_name = parser.rargs[0]
    if type(branch_name) in (str, unicode):
        system('git checkout %s' % branch_name)
    else:
        raise ValueError('You must specify a branch name to switch.')


if __name__ == '__main__':
    p = OptionParser(usage=SCRIPT_USAGE, version='%prog 0.1')
    # TODO group options via OPtionGroup object.
    p.add_option(
        '--new-branch', 
        help='Creates new local branch synced with remote branch (origin/branch_name). Expects branch name.',
        action='callback', 
        callback=create_new_branch_synced_with_remote_branch,
    )
    p.add_option(
        '--branches',
        help='Prints all branches.',
        action='callback',
        callback=print_branches
    )
    p.add_option(
        '--switch',
        help='Switch local branch.',
        action='callback',
        callback=switch_branch
    )
    p.add_option(
        '--status',
        help='Prints status.',
        action='callback',
        callback=print_status
    )
    p.add_option(
        '--pull',
        help='Git pull',
        action='callback',
        callback=pull
    )
    p.add_option(
        '--push',
        help='Git push',
        action='callback',
        callback=push
    )
    options, arguments = p.parse_args()
    sys.exit(0)
