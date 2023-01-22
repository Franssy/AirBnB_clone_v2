#!/usr/bin/python3
'''Fabric script to generate .tgz archive'''

from fabric.api import local
from datetime import datetime

from fabric.decorators import runs_once


@runs_once
def do_pack():
<<<<<<< HEAD
    '''generates .tgz archive from the contents of the web_static folder'''
    local("mkdir -p versions")
    path = ("versions/web_static_{}.tgz"
            .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    result = local("tar -cvzf {} web_static"
                   .format(path))

    if result.failed:
=======
    """distributes an archive to your web servers
    """
    target = local("mkdir -p versions")
    name = str(datetime.now()).replace(" ", '')
    opt = re.sub(r'[^\w\s]', '', name)
    tar = local('tar -cvzf versions/web_static_{}.tgz web_static'.format(opt))
    if os.path.exists("./versions/web_static_{}.tgz".format(opt)):
        return os.path.normpath("/versions/web_static_{}.tgz".format(opt))
    else:
        
>>>>>>> 343c5298732c1f37b8dd5137c4a81f21053bcdf4
        return None
    return path
