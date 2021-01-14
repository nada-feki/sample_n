FROM eu.gcr.io/prevision-enterprise/prevision/pio-components-python:v1


COPY components/sample_n/src /component/sample/src
# COPY requirements.txt /component/sample/requirements.txt

RUN python -m pip install pandas

# ENTRYPOINT python3 component/sample/src/sample.py
