FROM registry.access.redhat.com/rhel7/rhel:7.7-310
# FROM registry.redhat.io/rhel7-minimal:7.7

RUN yum -y install python3.x86_64 python3-pip.noarch

ADD hello-http-time.py /
ADD index.html /

CMD ["python", "./hello-http-time.py"]

