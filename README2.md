test and run on local containers

all containers has to be on the same network then you can use internal hostnames from docker-compose

docker network create main-backend
docker-compose up -d

docker exec -it mssql-db \
    /opt/mssql-tools/bin/sqlcmd -S 'mssql-db' -U SA -P 'yourStrong(!)Password' \
    -Q "RESTORE DATABASE AdventureWorks2017 FROM DISK = '/sql-bak/AdventureWorks2017.bak' \
    WITH MOVE 'AdventureWorks2017' TO '/MSSQL/Data/AdventureWorks2017.mdf', \
    MOVE 'AdventureWorks2017_log' TO '/MSSQL/Data/AdventureWorks2017.ldf';"

sam build
sam local invoke --docker-network 'main-backend'

docker-compose down
