var http = require('http');
var fs = require('fs');

var server = http.createServer(function (req, res) {
	console.log(req.url);	
	if(req.url === "/"){
		fs.readFile("./public/index.html", function (err, data) {
			res.writeHead(200, {"Content-Type": "text/html"});
			res.end(data);
		});	
	} else if (req.url === "/img/logo.png") {
		fs.readFile("./public/img/logo.png", function (err, data) {
			res.writeHead(200, {"Content-Type": "image/png"});
			res.end(data);	
		});
	} else {
		res.writeHead(404, {"Content-Type": "text/html"});
		res.end("Pagina no encontrada");
	};
	
});

server.listen(8000);

console.log('Escuchando en el puerto 8000');
