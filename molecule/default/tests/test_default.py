import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

def test_apache_installed(host):
    apache = host.package("httpd")
    assert apache.is_installed


def test_apache_config(host):
    apache = host.file('/etc/httpd/conf/httpd.conf')
    assert apache.exists


def test_apache_running_and_enabled(host):
    apache = host.service("httpd")
    assert apache.is_running
    assert apache.is_enabled