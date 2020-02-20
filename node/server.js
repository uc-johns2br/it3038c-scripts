var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require("ip");


http.createServer(function(req, res){
    
    if(req.url === "/"){
        fs.readFile("./public/index.html", "UTF-8", function(err, body)){
        res.writeHead(200,{"Content-Type": "text/html"});
        res.end(body);
        });
    }
}
    else if(req.url.match("/sysinfo")){
        myHostname=os.hostname();
        html=`
        <!DOCTYPE html>
        <html>
            <head>
                <title>System Info</title>
            </head>
            <body>
                <p>Hostname: ${myHostname}</p>
        `
    }
    


server.listen(3000);

console.log("Server listening on port 3000");