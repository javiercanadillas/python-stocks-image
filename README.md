# Containerizing a basic Python CLI app with dependencies

This container image containerizes a Python application that you've already built and practiced with, using external dependencies that are installed with `pip`. 

Once the application has been developed, if you want to distribute it, you need to make sure that:

- the user that's going to run the app has the Python interpreter version that your application requires is properly installed.
- the user has installed any Python libraries that the application depends on, like the Google Cloud Storage library that's being used here.
- there's an actual way to download the application to the user's local computer

Containerizing the app solves all these problems. The only thing that's required is that the user has a Linux system. Now, this is most useful when we're talking about _server side_ applications. If you were to make this app a web app, then the container could have been deployed in a web server and you could access its UI using a browser.

## Setting up the environment

Clone this repo and switch to the `gcs` branch:

```bash
git clone https://github.com/javiercanadillas/python-stocks-image
cd python-stocks-image
git checkout gcs
```

Check that you're in the right branch:

```bash
git branch
```

The output should be something like this, with the `gcs` branch having an asterisk in the left side, marking it as the active branch:

```text
* gcs
  main
  web
```

This time, you'll need to copy the csv file to Google Cloud Storage, as the application (that is, your container image) is not packaging this file anymore, but it will be pulled instead from Cloud Storage each time you create a container from the container image. First, create a Google Cloud Storage Bucket:

```bash
qwiklabs_user=<write your qwiklabs user here>
export BUCKET_NAME=stocks
gcloud storage buckets create "gs://$qwiklabs_user/$BUCKET_NAME"
```

Then, copy the file into the newly created bucket:
```bash
export FILE_NAME=all_stocks_5yr.csv
gsutil cp "$FILE_NAME" "gs://$qwiklabs_user/$BUCKET_NAME"
```

## Test that the app works

Now that the app is taking the file from GCS, test the application:

```bash
python stocks.py
```

## Baking the image

To bake/build/create the image:

```bash
cd python-stocks-image
docker build -t stocks-gcs .
```

## Testing that the image works

```bash
docker run --name local_stocks_gcs -it -e BUCKET_NAME=$BUCKET_NAME -e FILE_NAME=$FILE_NAME -e LOG_LEVEL=DEBUG stocks-gcs
```

### Cleaning up

Remove both the container and the image:

```bash
docker container rm local_stocks_gcs
docker image rm stocks-gcs
```