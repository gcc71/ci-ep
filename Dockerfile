FROM ubuntu
MAINTAINER codeinquisitor
USER root
COPY /app /app
COPY runtxtest.sh /runtxtest.sh
COPY runrxtest.sh /runrxtest.sh
RUN chmod +x runtxtest.sh
RUN chmod +x runrxtest.sh
RUN apt-get update
RUN apt install -y pip
RUN pip install -r app/requirements.txt
