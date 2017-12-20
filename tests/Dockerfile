FROM idealista/java-role:latest

# This is to override Testinfra issue with Debian 9 Docker image
RUN touch /tmp/systemd
RUN ln -s /tmp/systemd /sbin/init
