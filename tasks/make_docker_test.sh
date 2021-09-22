echo 'removendo imagens anteriores'
docker rm -f $(docker ps -a -q);
docker rmi -f $(docker images -q);
./docker_build.sh