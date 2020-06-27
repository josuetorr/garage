const express = require('express');
const path = require('path');
const fs = require('fs');
const app = express();

const bodyParser = require('body-parser');

//Setting middleware
app.use(bodyParser.urlencoded({ extended:false }));
app.use(bodyParser.json());

// Setting static content
app.use(express.static(path.join(__dirname, './')));

// app.get('/', (req, res) => {
//     res.send('<h1>Hello from NODE</h1>');
//     res.status(200);
// });


const data = {};
fs.readFile('user.test', 'utf8', (err, info) => {
    if(err) {
        console.log(err);
    }
    else {
        console.log(`Async read: ${info}`);
        data.username = info.split("\n")[0];
        data.password = info.split("\n")[1];
        console.log(data)
    }
});

// Compare the content posted to the content read.
// Definitely not the right way of doing it. 
// Simply for testing purposes
app.post('/', (req, res) => {
    if(data.username == req.body.username && data.password == req.body.password) {
        console.log("OK! You can proceed.");
    }
    else {
        console.log("GTFO");
    }
});

module.exports = app;
