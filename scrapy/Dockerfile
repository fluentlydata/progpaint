FROM python:3.6

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir /usr/src/app/data

COPY . .

# CMD scrapy runspider run.py
CMD scrapy crawl progpaint
