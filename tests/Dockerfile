FROM idealista/java-role:latest

# This is to override Testinfra issue with Idealista Java Docker image
RUN touch /tmp/systemd
RUN ln -s /tmp/systemd /sbin/init
