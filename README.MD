Directions For Grading:

Migrated to a Book API that does not require a key, you should be able to just run this in pyCharm

pyBook/__init__.py

is the file to run
it is currenty set to only run for local host

at the bottom of __init__.py
if you add change

if __name__ == '__main__':
    app.run()
to

if __name__ == '__main__':
    app.run(host='0.0.0.0')

you will be able to access this from an external client

It is best to run this behind a reverse-proxying web server with ssl certs installed,
you need to do that in order to have the iOS app interact with the api

thanks

