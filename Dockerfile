FROM --platform=linux/amd64 python:3.11-slim
EXPOSE 8501
ENV PIP_DEFAULT_TIMEOUT=100
ENV HOST 0.0.0.0
WORKDIR /app
COPY ./backend ./
ENV TMPDIR='/var/tmp'
RUN apt-get update
RUN apt-get install ffmpeg -y
RUN apt-get install libsm6 libxext6  -y
RUN apt-get install git -y
RUN apt-get install python3-tk -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py", "--server.fileWatcherType", "none"]