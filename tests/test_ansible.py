import pytest


@pytest.fixture()
def AnsibleDefaults(Ansible):
    return Ansible("include_vars", "defaults/main.yml")["ansible_facts"]


def test_tomcat_user(User, Group, AnsibleDefaults):
    assert User(AnsibleDefaults["tomcat_user"]).exists
    assert Group(AnsibleDefaults["tomcat_group"]).exists
    assert User(AnsibleDefaults["tomcat_user"]).group == AnsibleDefaults["tomcat_group"]


def test_tomcat_version(File):
    assert File("/opt/tomcat").exists


def test_tomcat_service(File, Service, Socket, AnsibleDefaults):
    ajp_port = AnsibleDefaults["tomcat_ajp_connector_port"]
    http_port = AnsibleDefaults["tomcat_http_connector_port"]

    assert File("/lib/systemd/system/tomcat.service").exists
    assert Service("tomcat").is_enabled
    assert Service("tomcat").is_running
    assert Socket("tcp://:::" + str(ajp_port)).is_listening
    assert Socket("tcp://:::" + str(http_port)).is_listening
