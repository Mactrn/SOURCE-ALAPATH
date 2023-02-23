FROM thejmthon/jmub:slim-buster

استنساخ بوابة RUN https://github.com/Alapath1/jmub.git / root / jmub

WORKDIR /root/jmub

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/jmub/bin:$PATH"

CMD ["python3","-m","jmub"]
