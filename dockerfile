FROM node:latest
WORKDIR /app
COPY server.js .
RUN npm init -y && npm install ws
CMD ["node", "server.js"]
