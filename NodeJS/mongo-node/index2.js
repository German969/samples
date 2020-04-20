var MongoClient = require('mongodb').MongoClient;

var pBase = MongoClient.connect('mongodb://localhost:27017/test');

pBase.then(function (base) {
	var usuarios = base.collection('usuarios');
	var pInsert = usuarios.insertOne({nombre: 'Jose'});
	pInsert.then(function (resultado) {
		console.log('id: ', resultado.insertedId);
		base.close();
	});
});
