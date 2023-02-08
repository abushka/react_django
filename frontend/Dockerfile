FROM node:16 as build

WORKDIR /code

COPY package*.json ./

RUN npm install


COPY . .

RUN npm run build


FROM node:16-bullseye-slim

RUN npm install serve -g

WORKDIR /code

COPY --from=build /code/build build