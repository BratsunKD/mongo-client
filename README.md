# mongo-client

Клиент сервис для MongoDB

Поднять сервис 
```
docker-compose build 
docker-compose up
```

Отправить запрос:
```
curl http://localhost:5000/all
```
```
curl http://localhost:5000/sold
```
```
curl http://localhost:5000/not_sold
```
```
curl http://localhost:5000/search_by_name?name=ExampleName
```
```
curl http://localhost:5000/mark_as_sold?_id=60b725f10c9d9e0b2b57
```
```
curl -X POST http://localhost:5000/add \
    -d "name=NewItem" \
    -d "date=2024-11-09" \
    -d "category=Electronics" \
    -d "microcategory=MobilePhones"
```
```
curl http://localhost:5000/delete_by_name?name=ExampleName
```


