# parser_csv

Компактный парсер csv-файлов, генерирующихся программой DipTrace.

#### Требования
1) lxwt
2) csv (python utils)

#### Установка зависимостей:
> virtualenv env

> . env/bin/activate (активация виртуальной среды)

> pip install -r requirements/base.txt


#### Обработка csv-файла
> python /src/%project%/run.py d %path_to_file.csv%

На выходе получаем xls-документ с табличкой, в соответствии с требованиям ЕСКД.
