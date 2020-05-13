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


def install_docker():
    packages = [
        'docker.io',
        'docker-compose',
    ]
    sudo('apt-get install -y {}'.format(' '.join(packages)))
    sudo('systemctl start docker')
    sudo('systemctl enable docker')


def run_docker_container():
    if files.exists('/home/ubuntu/btre-app/docker-compose.yml'):
        sudo('docker-compose up -d')


def create_env():
    if not files.exists('/home/ubuntu/btre-app/env'):
        run('python3 -m venv env')
    else:
        with cd('/home/ubuntu/btre-app/'):
            run('git pull')


def install_project_code():
    if not files.exists('/home/ubuntu/btre-app'):
        run('git clone https://github.com/alpden550/btre-app.git')


def install_pip_requirements():
    with cd('/home/ubuntu/btre-app/'):
        run('/home/ubuntu/btre-app/env/bin/pip install -r requirements.txt --upgrade')


def deploy():
    install_packages()
    install_project_code()
    install_docker()
    run_docker_container()
    create_env()
    install_pip_requirements()
