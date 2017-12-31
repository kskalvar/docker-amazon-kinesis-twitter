FROM amazonlinux

RUN yum update -y
RUN yum -y install aws-cli vim findutils procps

RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py --user

ENV PATH="/root/.local/bin/:${PATH}"
RUN pip install boto3 TwitterAPI

ADD files/*.py /kinesis/

