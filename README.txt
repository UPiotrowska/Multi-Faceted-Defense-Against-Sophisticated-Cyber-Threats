How all the files work.

1. index.html: The HTML file contains the login form and JavaScript code to handle form submission and WebSocket communication.

2. styles.css: The CSS file contains styles for the login form and other elements on the page.

3.script.js: The JavaScript file handles the form submission event, collects form data, and sends it to the WebSocket server.

4.Dockerfile: The Dockerfile specifies the setup for the WebSocket server. It installs Node.js, sets the working directory, copies the server.js file, installs the 'ws' package, and defines the command to run the server.

5. server.js: The server.js file sets up a WebSocket server using the 'ws' library. It listens for WebSocket connections and handles incoming messages, printing the log data to the console.

6.docker-compose.yml: The docker-compose.yml file defines two services: 'webserver' and 'websocket-server'. The 'webserver' service uses the httpd image and mounts the HTML, CSS, and JavaScript files. The 'websocket-server' service builds an image from the current directory using the Dockerfile and exposes port 8081 for WebSocket communication.

In summary, when a customer fills in the sign-in form and clicks the "SIGN IN" button, the script.js file collects the form data, establishes a WebSocket connection with the WebSocket server, and sends the log data as a message. The server.js file receives the message from the WebSocket connection, converts it to a string, and logs the data to the console, highlighting it in red.
