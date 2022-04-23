### Sublime's custom image

<p align="center">
  <img src="https://github.com/joaofds/App-Flask/raw/master/app_screen.png?raw=true" alt="Flask First App"/>
</p>

## Run Flask

### Run flask for develop

```
$ python src/main.py
```

In flask, Default port is `5000`

Swagger document page: `http://127.0.0.1:5000/`

### Run flask for production

** Run with gunicorn **

In src/

```
$ gunicorn -w 4 -b 127.0.0.1:5000 run:app

```

- -w : number of worker
- -b : Socket to bind

### Run with Docker

```
$ docker build -t flask-example .

$ docker run -p 5000:5000 --name flask-example flask-example

```

In image building, the webapp folder will also add into the image
