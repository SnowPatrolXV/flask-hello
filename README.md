[BUILD]
sudo docker build --tag flask-hello .

[RUN]
#local
sudo docker run -p 5000:5000 flask-hello
