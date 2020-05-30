FROM python:3

WORKDIR /home/karulean/testlab

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "TEST.py" ]