const express = require('express');
const mustache = require('mustache-express');

const app = express();

app.engine('html', mustache());

app.set('view engine', 'html');
app.set('views', __dirname + '/views');

const items = [
    {name: 'bob'},
    {name: 'caca'}
];

app.get('/', (req, res) => {
    res.render('index', {items});
});

app.listen(8080, () => console.log('Server running...'));
