# projectparser


## Подготовка окружения

```
pip install -r req.txt
```

## Наполнение данных

* Запуск парсинга 
```
python parserweb/parser.py
```
* Наполнение БД
```
python populate_db.py
```
* Запуск приложения
```
./run.sh
```
## Модель данных

![ER](ER_diag.png)

Link

https://dbdesigner.page.link/wCPjHn8Gwk7iNKeEA



## TODO

[TODO](TODO.md)

## Типовые проблемы

### Проблемы с импортом

если не проходит импорт, например
```
ModuleNotFoundError: No module named 'parser_core'
```
Необходимо проверить:
```
echo $PYTHONPATH
```
если переменная пустая, то в корне проекта выполнить:
```
export PYTHONPATH=$PWD
```