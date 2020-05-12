from fabric.api import cd, env, run, sudo
from fabric.contrib import files

env.hosts = ['ubuntu@3.121.63.217']

def install_packages():
    packages = [
        'python3-pip',
        'python3-dev',
        'python3-venv',
        'nginx',
        'git-core',
    ]
    sudo('apt-get install -y {}'.format(' '.join(packages)))


def install_docker_compose():
    sudo('curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
    sudo('chmod +x /usr/local/bin/docker-compose')
    sudo('ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose')


def create_env():
    if not files.exists('/home/ubuntu/btre-app/env'):
        run('python3 -m venv env')
    else:
        with cd('/home/ubuntu/btre-app/'):
            run('git pull')


def install_project_code():
    if not files.exists('/home/ubuntu/btre-app'):
        run('git clone https://github.com/alpden550/btre-app.git')


def deploy():
    install_packages()
    install_docker_compose()
    install_project_code()
    create_env()
