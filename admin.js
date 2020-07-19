const rl = require('readline');
const mongoose = require('mongoose');
    output: process.stdout

const stream = rl.createInterface({
    input: process.stdin,
    output: process.stdout
});

stream.question('What is your name?', name => {console.log(name)
    stream.close();
});
