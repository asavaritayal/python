#
# Dockerfile for Python
#
FROM python:3.6.5-stretch
LABEL maintainer="Azure App Service Container Images <appsvc-images@microsoft.com>"

# Web Site Home
ENV HOME_SITE "/home/site/wwwroot"

#Install venv
RUN pip install --upgrade pip \
	&& pip install virtualenv \
    && pip install gunicorn

COPY entrypoint.sh /usr/local/bin

RUN set -ex \
    && mkdir -p $HOME_SITE 

WORKDIR ${HOME_SITE}

EXPOSE 8000

RUN chmod u+x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
