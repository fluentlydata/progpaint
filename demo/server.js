'use strict';

// var http = require('http')
var request = require('request');
const express = require('express');

// Constants
const PORT = 8080;

// App
const app = express();

var requestSettings = {
    url: 'http://progpaint_media:8081/full/4c69f9c4462041bc200b6485e79a10e1bbac160d.jpg',
    method: 'GET',
    encoding: null
};

app.get('/', function (req, res) {
  request(requestSettings, function(err, res2, body) {
    res.set('Content-Type', 'image/jpeg');
    console.log(err);
    res.send(body);
  });
});

app.listen(PORT);
console.log('Running on http://localhost:' + PORT);

