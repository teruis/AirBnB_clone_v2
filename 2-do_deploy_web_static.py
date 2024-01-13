#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists
from fabric.exceptions import NetworkError

env.hosts = ['142.44.167.228', '144.217.246.195']

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return "Error: Archive not found at {}".format(archive_path)

    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"

        # Upload archive to /tmp/
        put(archive_path, '/tmp/')

        # Create directory for new release
        run('mkdir -p {}{}/'.format(path, no_ext))

        # Extract contents
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, no_ext))

        # Remove the archive
        run('rm /tmp/{}'.format(file_name))

        # Move contents to the proper location
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))

        # Remove the old symbolic link
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))

        return "Deployment successful!"

    except NetworkError as e:
        return "NetworkError: {}".format(str(e))

    except Exception as e:
        return "An error occurred: {}".format(str(e))

