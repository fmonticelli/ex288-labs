FROM registry.access.redhat.com/ubi9/nodejs-20

LABEL version="2"

WORKDIR /opt/app-root/src

COPY package.json ./

RUN npm install

COPY server.js ./

EXPOSE 8080

CMD ["node", "server.js"]