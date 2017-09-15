FROM python:2.7

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY splunk-6.6.3-e21ee54bc796-Linux-x86_64.tgz ./

RUN tar xvzf splunk-6.6.3-e21ee54bc796-Linux-x86_64.tgz -C /opt

COPY splunk-launch.conf /opt/splunk/etc

RUN ln -s /opt/splunk/bin/splunk /usr/bin/

COPY phantomjs-2.1.1-linux-x86_64.tar.bz2 ./

RUN tar xjf phantomjs-2.1.1-linux-x86_64.tar.bz2 -C /usr/local/

RUN mv /usr/local/phantomjs-2.1.1-linux-x86_64 /usr/local/phantomjs

RUN ln -s /usr/local/phantomjs/bin/phantomjs /usr/bin/

COPY ticket_price.spl ./

COPY ./src ./src
