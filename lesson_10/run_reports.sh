results=./results
rep_history=./report/history
report=./report

rm -rf $results # Удалить папку с результатами
pytest --alluredir=$results # Запустить тесты
mv $rep_history $results # Перенести историю в результаты
rm -rf $report # Удалить отчет
allure generate $results -o $report # Сгенерировать отчет
allure open $report # Открыть отчет