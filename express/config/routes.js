var saludador = require('../controllers/saludadorController');

module.exports = function(app) {
  app.get('/saludo', saludador.saludo);
};
