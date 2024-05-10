# Проект по тестированию онлайн кинотеатра Старт

**START** — российский онлайн-кинотеатр, запущенный в октябре 2017 года компанией «Yellow, Black and White».  
**Сайт** [start.ru](https://start.ru/)

![](assets/start.png)

<!-- Список проверок-->
## Список проверок, реализованных в автотестах:

### UI автотесты:

* ✅ Проверка успешной авторизации по email
* ✅ Проверка показа виртуальному пользователю popup о регистрации при добавлении контента в избранное
* ✅ Проверка добавления контента в Избранное авторизованным пользователем  
* ✅ Проверка перехода по логотипу Start на главную страницу
* ✅ Проверка названий разделов в хэдере для детского профиля
* ✅ Проверка успешной регистрации по email
* ✅ Проверка показа 1 результата запроса поиска в dropdown хэдера
* ✅ Проверка отображения множественных результатов запроса на странице поиска
* ✅ Проверка отображения текста заглушки при отсутсвующем результате запроса на странице поиска

### API автотесты:  

* ✅ Проверка ответа и его схемы на запрос карточки фильма
* ✅ Проверка ответа и его схемы на запрос карточки сериала
* ✅ Проверка ответа и его схемы на запрос Избранного авторизованного пользователя
* ✅ Проверка ответа на запрос раздела "Новинки"
* ✅ Проверка ответа и его схемы на запрос поиска контента с 1 результатом в ответе

<!-- Tools -->

## Проект реализован с использованием:

<p  align="center">
<code><img width="5%" title="python" src="assets/python.png"></code>
<code><img width="5.5%" title="selene" src="assets/selene.png"></code>
<code><img width="4.5%" title="selenium" src="assets/selenium.png"></code>
<code><img width="5%" title="pytest" src="assets/pytest.png"></code>
<code><img width="5%" title="selenoid" src="assets/selenoid.png"></code>
<code><img width="5%" title="jenkins" src="assets/jenkins.png"></code>
<code><img width="5%" title="allure" src="assets/allure_report.png"></code>
<code><img width="5%" title="alluretestops" src="assets/allure_testops.png"></code>
<code><img width="5.7%" title="github" src="assets/github.png"></code>  
<code><img width="5%" title="telegram" src="assets/tg.png"></code>   
<code><img width="5%" title="pycharm" src="assets/intellij_pycharm.png"></code>
<code><img width="5%" title="postman" src="assets/postman.png"></code>
<code><img width="5%" title="jira" src="assets/jira.png"></code>
<code><img width="4%" title="requests" src="assets/requests.png"></code>

>
Для написания UI-тестов используется фреймворк `Selene`, современная «обёртка» вокруг `Selenium WebDriver`
Библиотека модульного тестирования: `PyTest`  
`Jenkins` выполняет удаленный запуск тестов в графическом интерфейсе. Установки дополнительных приложений на компьютер
пользователя не требуется.  
`Selenoid` запускает браузер с тестами в контейнерах `Docker` (и записывает видео)  
Фреймворк `Allure Report` собирает графический отчет о прохождении тестов  
После завершения тестов `Telegram Bot` отправляет в `Telegram` краткий вариант `Allure Report`

## Локальный запуск UI и API тестов  

1. Скачать проект и открыть в IDE 
2. Создайте следующий файл:
   * `.env`  для запуска UI тестов локально и заполнить его актуальными тестовыми параметрами.
   * Пример заполнения файла указан в файле с расширением `.env.example`
3. Создайте и активируйте виртуальное окружение
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
4. Установите зависимости с помощью pip
   ```bash
   pip install -r requirements.txt
   ```
5. Для локального запуска необходимо выполнить команду в терминале:
    * Все тесты:<br>
    ```bash
    pytest ./tests --context=web_local --browser_name=BROWSER_NAME --browser_version=
    ```
    * UI тесты:<br>
    ```bash
    pytest tests/web --context=web_local --browser_name=BROWSER_NAME --browser_version=
    ```
   
   * API тесты:<br>
    ```bash
    pytest tests/API --context= --browser_name= --browser_version=
    ```
   Параметры:
      * --context=web_local для локального запуска. Для запуска через Selenoid будет web_selenoid
      * --browser_name= на выбор доступны `chrome` и `firefox`
      * --browser_version= оставить пустым, чтобы был скачан актуальный вебдрайвер
      
6. Выполнить запрос на формирование отчета:
* команда для Windows
```bash
allure serve
```
* команда для MacOS
```bash
allure serve allure-results
```

<!-- Jenkins -->
##  Удаленный запуск автотестов выполняется на сервере Jenkins

<a target="_blank" href="https://jenkins.autotests.cloud/job/AD_qa_guru_diploma/">Ссылка на проект в Jenkins</a>

### Параметры сборки
Данные параметры не обязательны для заполнения.

* `TESTS_FOLDER` - параметр определяет какие тесты будут запущены, по умолчанию ./tests/web - тесты WEB UI
* `COMMENT` - комментарий, который будет отправлен в сообщении от бота в Телеграм
* `BROWSER_NAME` - выбор браузера для запуска тестов, по умолчанию chrome
* `BROWSER_VERSION` - выбор версии браузера для запуска тестов, по умолчанию 100.0

![This is an image](assets/jenkins_parametrize.png)

### Запуск автотестов в Jenkins

1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/AD_qa_guru_diploma/">проект</a>

![This is an image](assets/jenkins_build_start.png)

2. Выбрать пункт **Build with Parameters**

3. Внести изменения в конфигурации сборки, при необходимости

4. Нажать **Build**

5. Результат запуска сборки можно посмотреть в классическом формате Allure Results

### Allure отчет

![image](assets/allure_results_jenkins_overview.png)
Отчет позволяет получить детальную информацию по все шагам тестов, включая скриншоты и log - файлы

![image](assets/allure_results_jenkins.png)

## Интеграция с Allure TestOps

<a target="_blank" href="https://allure.autotests.cloud/project/4217/dashboards">Ссылка на проект в
AllureTestOps</a> (запрос доступа `admin@qa.guru`)

#### Список всех кейсов, имеющихся в проекте

![This is an image](assets/alluretestops_test_cases.png)

#### Отображение результатов прогона тестов

![This is an image](assets/alluretestops_all_test_results.png)

## Интеграция с Jira

<a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-1218">Ссылка на проект в Jira</a>

![This is an image](assets/jira_all_tests.png)

## Видео прохождения теста:

Видеозапись каждого теста генерируется с помощью `Selenoid` после успешного запуска контейнера c тестами в `Docker`.

![video](assets/test_video.gif)

## Получение уведомлений о прохождении тестов в Telegram

После завершения сборки специальный Telegram-бот отправляет сообщение с отчетом.  

<img src="assets/tg_message.png" width="300" height="300">
