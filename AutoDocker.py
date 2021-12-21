import subprocess
from subprocess import check_output

def createdocker():

    f= open("dockerfile", "w")
    f.write("""
    FROM python:3
    COPY . /
    RUN pip install subprocess.run
    CMD [ "python", "hello.py" ]""")
    f.close()

 
def buildDockerimage():
    subprocess.call('docker build -t helloauto .', shell=True)
    subprocess.call('docker run helloauto', shell=True)

createdocker()
buildDockerimage()