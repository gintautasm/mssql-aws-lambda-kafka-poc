test and run on local containers

all containers has to be on the same network then you can use internal hostnames from docker-compose

```
# launch containers

docker network create main-backend
docker compose up -d

# restore database
docker exec -it mssql-db \
    /opt/mssql-tools/bin/sqlcmd -S 'mssql-db' -U SA -P 'yourStrong(!)Password' \
    -Q "RESTORE DATABASE AdventureWorks2017 FROM DISK = '/sql-bak/AdventureWorks2017.bak' \
    WITH MOVE 'AdventureWorks2017' TO '/MSSQL/Data/AdventureWorks2017.mdf', \
    MOVE 'AdventureWorks2017_log' TO '/MSSQL/Data/AdventureWorks2017.ldf';"

# build and invoke producer lambda
sam build
sam local invoke --docker-network 'main-backend'

# verify connection to Kafka broker
docker run --rm -it --add-host=host.docker.internal:host-gateway \
    --network="main-backend" \
    -v $(pwd)/config.yml:/etc/kafkactl/config.yml \
    deviceinsight/kafkactl \
    describe broker 1

# start consuming messages (launch in separate shell)
docker run --rm -it --add-host=host.docker.internal:host-gateway \
    --network="main-backend" \
    -v $(pwd)/config.yml:/etc/kafkactl/config.yml deviceinsight/kafkactl \
    consume purchases \
    --group dotnet-shared-code-delivery-community \
    --parse-headers

# destroy environment
docker compose down
```
