FROM node:lts-alpine3.14

WORKDIR /usr/app

COPY --chown=node:node package.json .
RUN npm install
COPY --chown=node:node . .

COPY . .

CMD [ "npm", "run", "dev" ]