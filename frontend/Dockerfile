FROM node:16 as build

WORKDIR /code

COPY package*.json ./

RUN npm install
RUN npm install react-router-dom
RUN npm install formik --save
RUN npm install axios

COPY . .

RUN npm run build


FROM node:16-bullseye-slim

RUN npm install serve -g

WORKDIR /code

COPY --from=build /code/build build