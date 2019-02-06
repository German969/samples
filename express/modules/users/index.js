var express = require('express');

function obtenerUsuario (req, res, next, id) {
  setTimeout(function () {
    if (id === "1"){
      res.locals.usuario = {nombre: 'Hernan'};
      next();
    } else {
      res.render('usuario/not_usuario');
    }
  }, 1000);
};

var usuarios = express.Router();

//app.all(obtenerUsuario);

usuarios.param('id', obtenerUsuario);

usuarios.get('/nuevo', function (req, res) {
  throw new Error('Oh no!');
  res.render('usuario/nuevo');
});

usuarios.post('/', function (req, res) {
  console.log(req.body);
});

usuarios.get('/:id', function (req, res) {
  console.log(req.params.id);
  res.locals.id = req.params.id;
  res.render('usuario/ver');
});

usuarios.get('/:id/editar', function (req, res) {
  console.log(req.params.id);
  res.locals.id = req.params.id;
  res.render('usuario/editar');
});

module.exports = usuarios;
