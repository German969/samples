var MongoClient = require('mongodb').MongoClient;

var url = 'mongodb://localhost:27017/test';
MongoClient.connect(url, function (err, base) {
	if (err) {
		console.log(err);
		return;
	}
	var usuarios = base.collection('usuarios');

	var hernan = {nombre: 'Hernan'};
	usuarios.insertOne(hernan, function (err, result) {
		if (err) {
			console.log(err);
			return;
		}
		console.log('id: ', result.insertedId);
		//base.close();	
	});

	//usuarios.find({}).skip(20).limit(10);
	usuarios.find({}).toArray(function (err, usuarios) {
		if (err) {
			console.log(err);
			return;
		}
		console.log('Los usuarios son: ', usuarios);
		base.close();
	});
	
});


