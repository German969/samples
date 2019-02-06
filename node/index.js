var chalk = require('chalk');
var fs = require('fs');

var username = process.argv[2];
var verde = chalk.bold.green;

console.log(verde("hola " + username));

var resultado = fs.readFileSync("prueba.txt");

console.log(resultado.toString());

fs.readFile("prueba.txt", function(err, data){
	if(err) throw err;
	console.log("Imprimiendo resultado async ");
	console.log(data.toString());
});
