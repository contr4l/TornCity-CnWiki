const http = require('http');
const fs = require('fs').promises;
const path = require('path');

const hostname = '127.0.0.1';
const port = 3080;

const server = http.createServer(async (req, res) => {
    const filePath = path.join(__dirname, req.url);
    try {
        const fileContent = await fs.readFile(filePath);
        if (filePath.endsWith(".html")) {
            res.writeHead(200, { 'Content-type': 'text/html' });
        }
        else if (filePath.endsWith(".js")) {
            res.writeHead(200, { 'Content-type': 'application/javascript' });
        }
        res.end(fileContent);
    } catch (err) {
        res.writeHead(404, { 'Content-type': 'text/plain' });
        res.end('404 Not Found');
    }
});

server.listen(port, hostname, () => {
    console.log(`HTTP 服务运行在 http://${hostname}:${port}/`);
});
