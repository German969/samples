var express = require('express');
var exphbs = require('express-handlebars');

var saludador = require('./controllers/saludadorController');
var routes = require('./config/routes');

var bodyParser = require('body-parser');

var app = express();

//middleware
function logMiddleware (req, res, next){
  console.log('url: ' + req.url);
  next();
};

//app.use(logMiddleware)

app.use(express.static('public'));//voy a servir contenido estatico

//body parser
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

//handlebars
var hbs = exphbs.create({
  defaultLayout: 'main',
  helpers: {
    list: function (elementos, options) {
      var ans = "<ul>";

      elementos.forEach(function(elemento) {
        ans += "<li>" + options.fn(elemento) + "</li>";
      });

      ans += "</ul>";
      return ans
    }
  }
});

app.engine('handlebars', hbs.engine);
app.set('view engine', 'handlebars');

routes(app);

app.get('/', [logMiddleware, function (req, res) {
  var html = '<p>Un Parrafo</p>';

  var usuarios = [
    {nombre: 'Jose', apellido: 'Perez'},
    {nombre: 'Juan', apellido: 'Martinez'},
    {nombre: 'Santiago', apellido: 'Orozco'}
  ];

  res.render('inicio', {parrafo: html, usuarios: usuarios});
}]);


var usuarios = require('./modules/users/index');

app.use('/usuario', usuarios);

app.use(function(req, res, next) {
  console.log(err);
  res.status(404).send('Pagina no encontrada');
});

app.use(function(err, req, res, next){
  res.status(500).send('Ups, hubo un error');
});

app.listen(8000, function () {
  console.log("Esperando requests en el puerto 8000");
});

