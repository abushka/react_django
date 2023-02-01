FROM node:16

# Create and define the node_modules's cache directory.
RUN mkdir /usr/src/cache
WORKDIR /usr/src/cache

# Install the application's dependencies into the node_modules's cache directory.
COPY package*.json ./
RUN npm install

RUN mkdir /node
WORKDIR /node

COPY package.json /node/

COPY . /node/