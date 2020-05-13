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
        with cd('/home/ubuntu/btre-app/'):
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


def configure_celery():
    sudo('useradd celery -d /home/celery -b /bin/bash')

    if not files.exists('/var/log/celery'):
        sudo('mkdir /var/log/celery')
    if not files.exists('/var/run/celery'):
        sudo('mkdir /var/run/celery')
    sudo('chown -R celery:celery /var/log/celery')
    sudo('chmod -R 755 /var/log/celery')
    sudo('chown -R celery:celery /var/run/celery')
    sudo('chmod -R 755 /var/run/celery')

    if not files.exists('/etc/conf.d/celery'):
        files.upload_template('fabric_templates/celery', '/etc/default/celery', use_sudo=True)
    if not files.exists('/etc/systemd/system/celery.service'):
        files.upload_template('fabric_templates/celery.service', '/etc/systemd/system/celery.service', use_sudo=True)


def restart_services():
    sudo('systemctl daemon-reload')
    sudo('sudo systemctl enable celery')
    sudo('sudo systemctl start celery')


def deploy():
    install_packages()
    install_project_code()
    install_docker()
    run_docker_container()
    create_env()
    install_pip_requirements()
    configure_celery()
    restart_services()
