"""
Configuration Strings
=======================

functions used to generate the configuration files for
pm2 and nginx for react and django applications

:Author: Nik Sumikawa
:Date: Sept 10, 2020

"""

import os

def react_ecosystem( name, port ):
    """ returns the pm2 ecosystem configuration string for react apps """
    return """
module.exports = {
  apps : [{
    name: '%s',
    script: 'npx',
    interpreter: 'none',
    args: 'serve build -s -l %s',
    instances: 1,
    autorestart: true,
    watch: false,
    max_memory_restart: '1G',
    env: {
      NODE_ENV: 'development'
    },
    env_production: {
      NODE_ENV: 'production'
    }
  }]
};
""" % (name, port)


def django_ecosystem( name, port ):
    """ returns the pm2 ecosystem configuration string for django apps """

    return """
module.exports = {
  apps : [{
    name: '%s',
    script: 'manage.py',
    interpreter: '%s/virenv/bin/python',
    exec_mode : 'fork',
    args: ['runserver','127.0.0.1:%s'],
    instances: 1,
    autorestart: true,
    watch: false,
    max_memory_restart: '1G',
    env: {
      NODE_ENV: 'development'
    },
    env_production: {
      NODE_ENV: 'production'
    }
  }]
};
""" % (name, os.getcwd(), port)


def nginx_conf( name, port ):
    """ returns the nginx configuration string """
    return """
location /%s {

proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header Host $http_host;
proxy_pass http://127.0.0.1:%s;
proxy_redirect off;

}


location /%s/static {
    autoindex on;
    alias %s/build/static;
}



    """ % (name, port, name, os.getcwd())
