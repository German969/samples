var mongo = require('mongodb');
var _ = require('lodash');

var db = mongo('mongodb://localhost:27017/test');

function validar (obj) {
	var model = _.pick(obj, 'nombre');
	if (!model.hasOwnProperty('nombre')) {
		return null;
	}
	return obj;
}

exports.listar = function () {
	return db.then(function (base) {
		return base.collection('usuarios').find().toArray();	
	});
};

exports.insertar = function (obj) {
	obj = validar(obj);
	if (obj) {
		return db.then(function (base) {
			return base.collection('usuarios').insert(obj);
		})
	} else {
		return Promise.reject('Modelo invalido');
	}
};


