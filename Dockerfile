# We're using Ubuntu 20.10
FROM koala21/kampangbot:buster
#
# Clone repo and prepare working directory
#
RUN git clone -b Petercord-Userbot https://github.com/ilham77mansiz/-PETERCORD- /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/ilham77mansiz/-PETERCORD-/Petercord-Userbot/requirements.txt

CMD ["python3","-m","userbot"]
