
    FROM python:3
    COPY . /
    RUN pip install subprocess.run
    CMD [ "python", "hello.py" ]