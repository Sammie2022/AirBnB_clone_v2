#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from 
the contents of the web_static folder
"""
from fabric.api import local, env, put, run
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


def do_deploy(archive_path):
    """distributes an archive to the webservers"""
    try:
        archive = archive_path.split('/')[-1]
        path = '/data/web_static/releases/' + archive.strip('.tgz')
        current = '/data/web_static/current'
        put(archive_path, '/tmp')
        run('mkdir -p {}/'.format(path))
        run('tar -xzf /tmp/{} -C {}'.format(archive, path))
        run('rm /tmp/{}'.format(archive))
        run('mv {}/web_static/* {}'.format(path, path))
        run('rm -rf {}/web_static'.format(path))
        run('rm -rf {}'.format(current))
        run('ln -s {} {}'.format(path, current))
        print('New version deployed!')
        return True
    except:
        return False


def deploy():
    """Function that calls do_pack and do_deploy"""
    archive_path = do_pack()
    resp = do_deploy(archive_path)
    return resp
