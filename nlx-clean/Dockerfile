FROM gcr.io/arctic-robot-192514/nlx-base
WORKDIR /usr/src/app
ADD . /usr/src/app

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt
COPY requirements.txt ./

# clone the crypto-cli repository 
RUN git clone https://5c1ff6b9df2a6b896d0dd3da733a431cab17420f@github.com/NeuroLexDiagnostics/crypto-cli/tree/feature/encrypt

# run tests
RUN python tests/run.py

CMD ["python", "/usr/src/app/lib/server.py"]
