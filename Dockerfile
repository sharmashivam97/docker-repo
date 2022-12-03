FROM python:alpine

LABEL maintainer="mkf@mkf.com"

COPY . .

ENV NAME=Batman

# ENTRYPOINT [ "python", "main.py" ]
CMD [ "python", "main.py" ]