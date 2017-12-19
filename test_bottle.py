from bottle import route, run, template  # type: ignore


@route('/hello/<name>')
def index(name):
	return template('<b>Hello {{name}}</b>!', name=name)


run(host='localhost', port=8080)
