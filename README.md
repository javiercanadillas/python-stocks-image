# Containerizing a basic Python CLI app

This container image containerizes a Python application that you've already built and practiced with.

Once the application has been developed, if you want to distribute it, you need to make sure that:

- the user that's going to run the app has the Python interpreter version that your application requires is properly installed.
- the user has installed any Python libraries that the application depends on (you'll see that later in class)
- there's an actual way to download the application to the user's local computer

Containerizing the app solves all these problems. The only thing that's required is that the user has a Linux system. Now, this is most useful when we're talking about _server side_ applications. If you were to make this app a web app, then the container could have been deployed in a web server and you could access its UI using a browser.

## Running the application

First, clone this repo:

```bash
git clone https://github.com/javiercanadillas/python-stocks-image
```

Get and run the application with one simple command:

```bash
docker run --name python_stocks -it javiercanadillas/stocks
```

### Cleaning up

```bash
docker container rm python_stocks
docker image rm javiercanadillas/stocks
```

## Baking the image

To bake/build/create the image:

```bash
cd python-stocks
docker build -t stocks .
```

## Testing that the image works

```bash
docker run --name local_stocks -it stocks
```

## Pushing the image to Docker Hub

For this to happen, you need to register into Docker Hub creating a user, and then create a public `stocks` repository.

Once this is done, you then need to tag the image:

```bash
dockerhub_username=<your Docker Hub username> # This would be something like dockerhub_username=javiercanadillas, but with your username
docker tag stocks $dockerhub_username/stocks
```

Login into Docker hub using your created user name and password:

```bash
docker login
```

Finally, push the image to the public repository:

```bash
docker push $dockerhub_username/stocks
```
