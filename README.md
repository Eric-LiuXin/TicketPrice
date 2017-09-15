## Overview

Crawl the ticket data from ctrip and display on the dashboard.

## Environment

Download [Splunk Enterprise](https://www.splunk.com/en_us/download.html) to the folder TicketPrice. Maybe you need create splunk account

Download [PhantomJS](https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2) to the folder TicketPrice

## Build/rebuild docker image

To build/rebuild the ticket_price docker image, just run

    docker build -t ticket_price.

## First time run

Just run

    docker run -dit -p "8000:8000/tcp" -p "514:514/udp" ticket_price /bin/bash -c "splunk start --accept-license;splunk install app ./ticket_price.spl -update 1 -auth admin:changeme;python ./src/TicketPrice.py AutoRun"

    
## Login dashboard
    
    The http://localhost:8000 used in browser, default admin user: admin&changeme.
    
    View dashboard in app `Ticket Price`.
