FROM python:3.6.5-stretch
LABEL maintainer="astay@microsoft.com"

# Web Site Home
ENV HOME_SITE "/home/site/wwwroot"

#Install system dependencies
RUN pip install --upgrade pip \
    && pip install subprocess32 \
    && pip install gunicorn

COPY entrypoint.py /usr/local/bin

WORKDIR ${HOME_SITE}

EXPOSE 8000

ENTRYPOINT ["python3","/usr/local/bin/entrypoint.py"]
