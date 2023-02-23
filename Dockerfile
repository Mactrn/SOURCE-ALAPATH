FROM Alapath1/zthon:slim-buster

استنساخ بوابة RUN https://github.com/Alapath1/zthon.git / root / zthon

WORKDIR /root/zthon

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/zthon/bin:$PATH"

CMD ["python3","-m","zthon"]
