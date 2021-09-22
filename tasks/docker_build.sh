echo ' criando nova imagem';
docker build -t teste .. &&
docker run teste;
echo 'processo finalizado'