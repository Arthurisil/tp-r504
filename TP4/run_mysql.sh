docker run -d \
	--name tp4-sqltest \
	-e MYSQL_ROOT_PASSWORD=foo \
	-p 3307:3306 mysql

