FROM robd003/python3.10

COPY . /opt

RUN pip install torch==1.13.1

RUN pip install -r /opt/requirements.txt

RUN pip install -e .

