FROM ubuntu:latest
RUN apt-get update -y && \
	apt-get install -y --no-install-recommends apt-utils && \
    apt-get install -y python-pip python-dev
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
ENV FLASK_APP main.py
RUN pip install -r requirements.txt
EXPOSE 80
EXPOSE 5000
COPY . /app
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]