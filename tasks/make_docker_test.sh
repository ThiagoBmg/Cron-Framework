echo 'removendo imagens anteriores';
docker rm -f cron_job_teste;
docker rmi -f cron_job_teste_image;
echo ' criando nova imagem';
docker build -t cron_job_teste_image .  &&
docker run --name "cron_job_teste" cron_job_teste_image;
echo 'processo finalizado'