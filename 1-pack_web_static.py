#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from
the contents of the web_static folder
"""
from fabric.api import local, env
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['100.27.14.80', '54.236.24.31']


def do_pack():
    """targging project directory into a package as .tgz"""
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    local('sudo mkdir -p ./versions')
    path = './versions/web_static_{}'.format(now)
    local('sudo tar -czvf {}.tgz web_static'.format(path))
    name = '{}.tgz'.format(path)
    if name:
        return name
    else:
        return None
