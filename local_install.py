#!/usr/bin/python3
#
# print('waiting for input')
# print(input())
import os
import subprocess

from config_strings import *


def ecosystem(name, port, product):
    """ create an ecosystem file """
    import os

    print( 'creating file: %s/ecosystem.config.js' % (os.getcwd()) )
    file = open('ecosystem.config.js', 'w')

    if product.lower() == 'react':
        file.write( react_ecosystem(name, port) )
    else:
        file.write( django_ecosystem(name, port) )

    file.close()

def nginx_config(name, port, nginx_path):
    print( 'creating file: %s' % (nginx_path + '%s.conf' % name) )
    file = open(nginx_path + '%s.conf' % name, 'w')
    file.write( nginx_conf(name, port) )
    file.close()


def create_virenv():
    # create a virtual environment directory when one does not exist
    if not os.path.exists( 'virenv' ):
        # raise error when a requirements.txt doesn't exist
        if not os.path.exists( 'requirements.txt' ):
            print( """cannot install the django applications without a requirements.txt file
                python -m pip freeze > requirements.txt
            """)
            return

        print( 'installing virtual environment and all dependencies from requirements.txt' )
        subprocess.call(['python3 -m venv virenv'], shell=True)
        subprocess.call(['virenv/bin/python3 -m pip install -r requirements.txt'], shell=True)




def install(product, path, name, port):
    """ installs the configuration files based on the specifications """

    os.chdir(path)
    
    import platform
    linux_dist = platform.linux_distribution()[0]

    if linux_dist == 'Red Hat Enterprise Linux Server':
        nginx_path = '/etc/nginx/default.d/'
    else:
        nginx_path = '/etc/nginx/sites-enabled/'

    nginx_config(name, port, nginx_path)

    # change the directory to where the code exists
    ecosystem(name, port, product)

    if product == 'django':
        create_virenv()

    elif product == 'react':
        subprocess.call(['chmod 775 -R build'], shell=True)

    cwd = os.getcwd()
    subprocess.call(['chmod 775 -R %s' % cwd], shell=True)

    subprocess.call(['pm2 start ecosystem.config.js'], shell=True)
    subprocess.call(['service nginx restart'], shell=True)







