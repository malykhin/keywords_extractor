FROM python:3.6

WORKDIR /usr/src/app

COPY requirements.txt ./
#RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install flask
RUN pip3 install spacy
RUN pip3 install textacy
RUN python3 -m spacy download en
COPY . .

CMD [ "python3", "./server.py" ]
