// request Listener
// this is what we'll feed into http.createServer
function requestListener(request, response) {
    let reqUrl = `http://${request.headers.host}${request.url}`;
    let parseUrl = url.parse(reqUrl, true);
    let pathname = parseUrl.pathname;

    // we're doing everything json
    response.setHeader('Content-Type', 'application/json');

    // buffer for incoming data
    let buf = null;

    // listen for incoming data
    request.on('data', data => {
        if (buf === null) {
            buf = data;
        } else {
            buf = buf + data;
        }
    });

    // on end proceed with compute
    request.on('end', () => {
        let body = buf !== null ? buf.toString() : null;

        if (routes[pathname]) {
            let compute = routes[pathname].call(null, body);

            if (!(compute instanceof Promise)) {
                // we're kinda expecting compute to be a promise
                // so if it isn't, just avoid it

                response.statusCode = 500;
                response.end('oops! server error!');
                console.warn(`whatever I got from rpc wasn't a Promise!`);
            } else {
                compute.then(res => {
                    response.end(JSON.stringify(res))
                }).catch(err => {
                    console.error(err);
                    response.statusCode = 500;
                    response.end('oops! server error!');
                });
            }

        } else {
            response.statusCode = 404;
            response.end(`oops! ${pathname} not found here`)
        }
    })
}

// now we can start up the server
server.listen(PORT);