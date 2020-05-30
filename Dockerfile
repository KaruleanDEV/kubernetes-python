FROM python:3

WORKDIR /home/karulean/testlab

COPY requirements.txt ./
RUN pip install --nocache-dir -r requirements.txt

COPY . .

CMD [ "python", "./src/TEST.py" ]