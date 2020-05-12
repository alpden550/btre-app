from fabric.api import sudo


def install_packages(parameter_list):
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


if __name__ == '__main__':
    deploy()
