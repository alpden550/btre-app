from fabric.api import env, sudo

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


def deploy():
    install_packages()
    install_docker_compose()
