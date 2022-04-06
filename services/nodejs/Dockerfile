FROM node:14.3.0-alpine

RUN mkdir -p /home/app
WORKDIR /home/app

RUN npm install -g nodemon

COPY package.json package.json

RUN npm install

RUN rm package.json package-lock.json

COPY ./src .

ENTRYPOINT ["nodemon", "server.js"]
