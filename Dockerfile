FROM python:3.10-rc-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN python -m pip install --upgrade pip
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .

CMD flask run --host=0.0.0.0
