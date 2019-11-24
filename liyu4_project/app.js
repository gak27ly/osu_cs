var express = require('express');
var app = express();
var handlebars = require('express-handlebars').create({defaultLayout:'main'});
var bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: false }));
app.use('/public', express.static('public'));
app.engine('handlebars', handlebars.engine);
app.set('view engine', 'handlebars');
app.set('port', 7966);


app.get('/', function(req, res) {
    res.render('homePage');
});

app.get('/teams', function(req,res){
	res.render('teams');
});


app.get('/players', function(req,res){
	res.render('players');
});

app.get('/forecast', function(req,res){
	res.render('forecast');
});


app.use(function(req,res){
  res.status(404);
  res.render('404');
});

app.use(function(err, req, res, next){
  console.error(err.stack);
  res.type('plain/text');
  res.status(500);
  res.render('500');
});

app.listen(app.get('port'), function(){
	console.log('express started on port: ' + app.get('port'));
});