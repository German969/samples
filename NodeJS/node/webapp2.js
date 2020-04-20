var http = require('http');
var url = require('url');
var saludador = require('./models/saludador');

var server = http.createServer(function (req, res) {
	console.log(req.url);
	var query = url.parse(req.url, true).query;
	console.log(query);	
	res.writeHead(200, {"Content-Type": "text/html"});
	res.end("<h1>" + saludador.saludar(query.nombre) + "!</h1>");		
	
});

server.listen(8000);

console.log('Escuchando en el puerto 8000');
