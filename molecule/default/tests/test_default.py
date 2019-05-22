import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_redis_installed(host):
    service = host.service("redis")

    assert service.is_running
    assert service.is_enabled


def test_port_listening(host):
    socket = host.socket("tcp://0.0.0.0:6379")

    assert socket.is_listening


def test_redis_conf_file(host):
    file = host.file("/etc/redis/6379.conf")

    assert file.exists
    assert file.is_file
    assert file.user == "redis"
    assert "port 6379" in file.content_string


def test_redis_server_pid_file(host):
    file = host.file("/var/run/redis/redis-server.pid")

    assert file.exists
    assert file.user == "redis"
    assert file.size > 0


def test_redis_server_file(host):
    file = host.file("/usr/bin/redis-server")

    assert file.is_symlink


def test_redis_cli_file(host):
    file = host.file("/usr/bin/redis-cli")

    assert file.is_symlink
