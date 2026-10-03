import { createServer } from "node:http";

const page = `<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Chat</title>
    <style>
      :root {
        color-scheme: light;
        font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      }

      * {
        box-sizing: border-box;
      }

      body {
        align-items: center;
        background: #f4f4f5;
        display: flex;
        justify-content: center;
        margin: 0;
        min-height: 100vh;
        padding: 1rem;
      }

      form {
        background: #ffffff;
        border: 1px solid #e4e4e7;
        border-radius: 0.75rem;
        box-shadow: 0 0.5rem 1.5rem rgb(0 0 0 / 8%);
        display: flex;
        max-width: 34rem;
        padding: 0.5rem;
        width: 100%;
      }

      input {
        background: transparent;
        border: 0;
        color: #18181b;
        flex: 1;
        font: inherit;
        min-width: 0;
        outline: 0;
        padding: 0.75rem;
      }

      input::placeholder {
        color: #a1a1aa;
      }
    </style>
  </head>
  <body>
    <form id="chat-form">
      <input
        id="message"
        name="message"
        type="text"
        aria-label="Message"
        autocomplete="off"
        placeholder="Type a message..."
        autofocus
      />
    </form>
    <script>
      document.getElementById("chat-form").addEventListener("submit", (event) => {
        event.preventDefault();
        document.getElementById("message").value = "";
      });
    </script>
  </body>
</html>`;

const server = createServer((request, response) => {
  if (request.method !== "GET" || request.url !== "/") {
    response.writeHead(404, { "Content-Type": "text/plain; charset=utf-8" });
    response.end("Not found");
    return;
  }

  response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
  response.end(page);
});

const port = Number(process.env.PORT) || 3000;

server.listen(port, () => {
  console.log(`Chat website available at http://localhost:${port}`);
});
