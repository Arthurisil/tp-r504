docker build -t serveur-tcp ./ClientTCP3
docker build -t client-tcp ./ServeurTCP3
docker run -d --name mon-serveur -p 2016:2016 serveur-tcp
docker run client-tcp java ClientTCP3 localhost






