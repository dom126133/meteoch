FROM python:3.11-bookworm

RUN apt update && apt upgrade -y
RUN apt install curl build-essential gcc make -y
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

ADD requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /meteoch
ADD meteoch .


WORKDIR /meteoch
RUN pwd; ls

CMD ["uvicorn", "asgi:app", "--host",  "0.0.0.0", "--port", "8001"]