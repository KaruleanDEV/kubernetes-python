FROM python:3

WORKDIR /home/karulean/testlab

COPY requirements.txt ./
RUN pip install --nocachedir -r requirements.txt

COPY . .

CMD [ "python", "./src/TEST.py" ]