# Python off raspberry

app in python to turn off raspberry pi

## Run app with docker

1. create image with dockerfile
    ```bash
    docker build -t off-raspberry:latest .
    ```

2. run image
    ```bash
    docker run off-raspberry:latest
    ```