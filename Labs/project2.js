//This is a script to display a log file when the link for it is clicked on the main index page
var http = require("http"); 
var fs = require("fs");

var server = http.createServer(function(req, res){
    if(req.url === "/") {
        fs.readFile("./public/index.html","UTF-8",function(err, body){
            res.writeHead(200, {"Content-Type":"text/html"}); 
            res.end(body);
        });
    }

    else if(req.url.match("/public/rando.log")){
        fs.readFile("./public/rando.log","UTF-8")
        res.writeHead(200, {"Content-Type":"text/plain"});
        res.end(html);
    }

    else {
        res.writeHead(404, {"Content-Type":"text/plain"});
        res.end(`404 File Not Found at ${req.url}`); 
    }
});

server.listen(3000); 
console.log("Server listening on port 3000"); 