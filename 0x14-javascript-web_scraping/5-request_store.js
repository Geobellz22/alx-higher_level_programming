#!/usr/bin/node

const fs = require('fs');
const args = process.argv;
const request = require('request');

const url = args[3];
request(url, (error, response, body) => {
  if (error) {
    console.log(error)
  }

  fs.writeFile(`${args[2]}`, body, (err) => {
    if (err) {
      console.error(err);
    }
   });
 });
