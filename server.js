require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const mustache = require('mustache-express');

const app = express();

app.engine('html', mustache());
app.set('view engine', 'html');
app.set('views', __dirname + '/views');

app.use(bodyParser.urlencoded({ extended: false }));

// Connect to Mongo
mongoose.connect(process.env.DB_HOST, { useNewUrlParser: true })
    .then(() => console.log('MongoDB connected...'))
    .catch(err => console.log(err));


const Item = require('./models/Item');

app.get('/', (req, res) => {
    Item.find()
        .then(items => res.render('index', { items }))
        .catch(err => res.status(404).json({ msg: 'No items found' }));
});

app.post('/item/add', (req, res) => {
    const newItem = new Item({
        name: req.body.name
    });

    newItem.save().then(item => res.redirect('/'));
});

const port = 3000;

app.listen(port, () => console.log(`Server runing on port ${port}...`))
