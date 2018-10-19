// node server.js from inside the directory to start up the server, then using postman,
// or your api tool of choice, send a request to http://localhost:{PORT}/rpc containing the following json body




'use strict';

let http = require('http');
let url = require('url');
let methods = require('./methods');
let types = require('./types');

let server = http.createServer(requestListener);
const PORT = process.env.PORT || 9090;

// we'll use a very very very simple routing mechanism
// don't do something like this in production, ok technically you can...
// probably could even be faster than using a routing library :-D

let routes = {
    // this is the rpc endpoint
    // every operation request will come through here
    '/rpc': function (body) {
        return new Promise((resolve, reject) => {
            if (!body) {
                throw new (`rpc request was expecting some data...!`);
            }
            let _json = JSON.parse(body); // might throw error
            let keys = Object.keys(_json);
            let promiseArr = [];

            for (let key of keys) {
                if (methods[key] && typeof (methods[key].exec) === 'function') {
                    let execPromise = methods[key].exec.call(null, _json[key]);
                    if (!(execPromise instanceof Promise)) {
                        throw new Error(`exec on ${key} did not return a promise`);
                    }
                    promiseArr.push(execPromise);
                } else {
                    let execPromise = Promise.resolve({
                        error: 'method not defined'
                    })
                    promiseArr.push(execPromise);
                }
            }

            Promise.all(promiseArr).then(iter => {
                console.log(iter);
                let response = {};
                iter.forEach((val, index) => {
                    response[keys[index]] = val;
                });

                resolve(response);
            }).catch(err => {
                reject(err);
            });
        });
    },

    // this is our docs endpoint
    // through this the clients should know
    // what methods and datatypes are available
    '/describe': function () {
        // load the type descriptions
        return new Promise(resolve => {
            let type = {};
            let method = {};

            // set types
            type = types;

            //set methods
            for(let m in methods) {
                let _m = JSON.parse(JSON.stringify(methods[m]));
                method[m] = _m;
            }

            resolve({
                types: type,
                methods: method
            });
        });
    }
};


var add = (function () {
    var counter=0;
    return function(){counter +=1;}

    }

)