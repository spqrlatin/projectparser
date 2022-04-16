# projectparser


## Подготовка окружения

```
pip install -r req.txt
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