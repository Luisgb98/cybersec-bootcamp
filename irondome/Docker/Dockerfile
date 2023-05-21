FROM ubuntu:latest   

RUN set -x -e && apt-get update && \
    apt-get install openssh-server -y && apt-get install vim sudo python3 pip -y

COPY sshd_config /etc/ssh/sshd_config
COPY ssh.sh /ssh.sh

RUN set -x -e && pip3 install psutil watchdog python-daemon && \
    chmod +x /ssh.sh && \
    echo "root:root" | chpasswd

EXPOSE 4242

CMD ["sh", "/ssh.sh"]