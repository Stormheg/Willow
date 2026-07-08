# This Dockerfile is used to easily run the OpenCV tests without having to install OpenCV on the host machine.
FROM python:3.14-slim-trixie
RUN apt update && apt install -y imagemagick
RUN pip install opencv-contrib-python-headless

WORKDIR /code
COPY . ./
RUN pip install -e .[testing]
CMD [ "python", "./runtests.py", "-v", "--opencv" ]
