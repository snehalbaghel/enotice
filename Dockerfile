FROM python:3.8
RUN pip install pipenv
COPY Pipfile* /tmp
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY . /tmp/enotice
RUN pip install /tmp/enotice
EXPOSE 5000
RUN python manage.py run