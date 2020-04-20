var express = require('express');

var usuarios = express.Router();

usuarios.param('id', function (req, res, next, id) {
	dal.obtener(id)
	.then(function(usuario) {
		if (usuario) {
			re.locals.usuario = usuario;
			next();
		} else {
			res.status(404).json({error: 'usuario no encontrado'});
		}
	})
	.catch(returnError.bind(this,res));
});

usuarios.get('/', function (req, res) {
	dal.listar()
	.then(function (lista) {
		res.json(lista);
	})
	.catch(returnError.bind(this, res));
});

usuarios.get('/:id', function (req, res) {
	res.json(re.locals.usuario);
});

function returnError (res, err) {
	res.status(500).send('Hubo un error' + err);
}

module.exports = usuarios;
