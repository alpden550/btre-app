from fabric.api import sudo


def install_packages():
    packages = [
        'python3-pip',
        'python3-dev',
        'python3-venv',
        'nginx',
        'git-core',
        'py-pip',
    ]
    sudo('apt-get install -y {}'.format(' '.join(packages)))


def deploy():
    install_packages()
