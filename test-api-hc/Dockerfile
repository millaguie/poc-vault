FROM python
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
ENV FLASK_APP=app
COPY . /app
HEALTHCHECK --interval=10s --timeout=3s CMD curl --fail http://localhost/health || bash -c 'kill -s 15 -1 && (sleep 10; kill -s 9 -1)'
CMD sleep 10 && flask run --host=0.0.0.0 --port=80