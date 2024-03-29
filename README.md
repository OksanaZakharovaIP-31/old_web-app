# old_web-app
my bachelor's diploma

# Дипломная бакаларская работа на тему "Разработка web-приложения оперативного мониторинга движения судов для логистических компаний"

Данный проект был придуман для облегчения работы логистов в отслеживании судов на карте.

Разработанное web-приложение будет иметь ряд преимуществ, по сравнению с другими аналогичными существующими web-приложениями. Во-первых, доступ к данным будет только у заранее зарегистрированных пользователей. Следовательно, доступ к данным будет абсолютно бесплатным.
Во-вторых, затрачиваемое время на поиск нужного судна уменьшается в разы, так как логистическая компания сама заносит данные необходимых судов. Так же реализованы возможности поиска и использование фильтров.


# Описание приложения для пользователей

Есть несколь особенностей сайта

1. Нельзя самостоятельно зарегистрироваться. Должен зарагистрировать админ.
2. Добавлена возможность расчёта топлива на заданный путь.
3. Предполагается вида пользователей.
<details><summary>

  *Используемые обозначения на карте*
</summary>

![Используемые обозначения на карте](https://github.com/OksanaZakharovaIP-31/old_web-app/blob/main/pictures/%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0%20%D1%81%D1%83%D0%B4%D0%BE%D0%B2.jpg "Используемые обозначения на карте")
</details>
<details>
<summary>
  
**Типы пользователей**

</summary>

<details>
<summary>
  
  **Пользователь**
  </summary>
  
  + Обычный пользователь имеет доступ только с закрепленным за ним суднами. Может отслеживать судна на карте, а также расчитатывать необходимое количество топлива.
  <details>
  <summary>
    
  *Страница входа*
  </summary>
  
  ![Вход](https://github.com/OksanaZakharovaIP-31/old_web-app/blob/main/pictures/%D0%92%D1%85%D0%BE%D0%B4.jpg "Вход") 
  
  </details>
  <details>
  <summary>
    
  *Главная страница*
  </summary>
  
![Главная страница](https://github.com/OksanaZakharovaIP-31/old_web-app/blob/main/pictures/%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F%20%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0%20user.jpg "Главная страница") 
  
</details>
<details>
  <summary>
    
  *Поиск*
  </summary>
  
  ![Поиск судна](https://github.com/OksanaZakharovaIP-31/old_web-app/blob/main/pictures/%D0%BC%D0%BE%D0%B4%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5%20%D0%BE%D0%BA%D0%BD%D0%BE%20%D1%81%20%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%BE%D0%BC%20%D1%81%D1%83%D0%B4%D0%BD%D0%B0.jpg "Поиск судна")
  
</details>  
<details>
  <summary>
    
  *Фильтр*
  </summary>
  
  ![Фильтр]( https://github.com/OksanaZakharovaIP-31/old_web-app/blob/main/pictures/%D0%BC%D0%BE%D0%B4%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5%20%D0%BE%D0%BA%D0%BD%D0%BE%20%D1%81%20%D1%84%D0%B8%D0%BB%D1%8C%D1%82%D1%80%D0%BE%D0%BC.jpg "Фильтр")
</details> 
<details><summary>

  *Отображение судна на карте*
</summary>

+ Чтобы посмотреть судно на карту нужно ссылку **Открывать в новой вкладке!!!**
  
![На карте](https://github.com/OksanaZakharovaIP-31/old_web-app/blob/main/pictures/%D0%BD%D0%B0%20%D0%BA%D0%B0%D1%80%D1%82%D0%B5.gif "На карте")
</details>
<details><summary>

  *Расчет топлива*
</summary>

![Расчет топлива](https://github.com/OksanaZakharovaIP-31/old_web-app/blob/3198fc0d7a950da43de3f6f12f378f407cf70a7a/pictures/%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%20%D0%B3%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8%20%D0%BF%D0%B0%D1%80%D0%BE%D0%BB%D1%8F.gif "Расчет топлива")
</details>

<details><summary>

  *Редатирование своего профиля*
</summary>

![Редактрование своего профиля](https://github.com/OksanaZakharovaIP-31/old_web-app/blob/main/pictures/%D1%80%D0%B5%D0%B4%D0%B0%D0%BA%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BF%D1%80%D0%B8%D1%84%D0%B8%D0%BB%D1%8F.jpg "Редактирование своего профиля")
</details>
</details> 
<details>
<summary>
  
  **Администратор**
</summary>

+ Администратор имеет те же возможности, что и пользователь. Также может вносить новые судна для отслеживания/удалять/изменять их, вносить новые типы судна, просматривать страницу от имени определенного пользователя, названачать нового пользователя для отслеживания.
<details><summary>

  *Главная страница администратора*
</summary>

![Главная страница администратора](https://github.com/OksanaZakharovaIP-31/old_web-app/blob/3198fc0d7a950da43de3f6f12f378f407cf70a7a/pictures/%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0%20%D0%B0%D0%B4%D0%BC%D0%B8%D0%BD%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%B0.jpg "Главная страница администратора")</details>
<details><summary>

  *Добавление нового судна*
  </summary>
  
  ![Добавление нового судна](https://github.com/OksanaZakharovaIP-31/old_web-app/blob/main/pictures/%D0%BC%D0%BE%D0%B4%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5%20%D0%BE%D0%BA%D0%BD%D0%BE%20%D0%B4%D0%BB%D1%8F%20%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F%20%D1%81%D1%83%D0%B4%D0%BD%D0%B0.jpg "Добавление нового судна")
  <details><summary>

*Пример выбора типа судна при созданиии судна*
    </summary>

    
  ![Пример выбора типа судна](https://github.com/OksanaZakharovaIP-31/old_web-app/blob/main/pictures/%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%20%D0%B2%D1%8B%D0%B1%D0%BE%D1%80%D0%B0%20%D1%82%D0%B8%D0%BF%D0%B0%20%D1%81%D1%83%D0%B4%D0%BD%D0%B0%20%D0%BF%D1%80%D0%B8%20%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B8.jpg "Пример выбора типа судна")
  </details>
  <details><summary>

  *Подсказка при добавлении нового судна*
  </summary>

  ![Подсказка при добавлении нового судна](https://github.com/OksanaZakharovaIP-31/old_web-app/blob/main/pictures/%D0%BF%D0%BE%D0%B4%D1%81%D0%BA%D0%B0%D0%B7%D0%BA%D0%B8%20%D0%BF%D1%80%D0%B8%20%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B8%20%D0%BD%D0%BE%D0%B2%D0%BE%D0%B3%D0%BE%20%D1%81%D1%83%D0%B4%D0%BD%D0%B0.jpg "Подсказка при добвлении нового судна")
  </details>
  <details><summary>

  *Выбор логиста*
  </summary>
  
![Выбор логиста](https://github.com/OksanaZakharovaIP-31/old_web-app/blob/main/pictures/%D0%B2%D1%8B%D0%B1%D0%BE%D1%80%20%D0%BB%D0%BE%D0%B3%D0%B8%D1%81%D1%82%D0%B0%20%D0%BF%D1%80%20%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B8%20%D1%81%D1%83%D0%B4%D0%BD%D0%B0.jpg "Выбор логиста)
  
  </details>
  </details>
<details><summary>

  *Добавление нового типа судна*
</summary>

![Добавление новго типа судна](https://github.com/OksanaZakharovaIP-31/old_web-app/blob/main/pictures/%D0%B4%D0%BE%D0%B1%D0%B0%D0%BB%D0%B2%D0%BD%D0%B8%D0%B5%20%D0%BD%D0%BE%D0%B2%D0%BE%D0%B3%D0%BE%20%D0%B2%D0%B8%D0%B4%D0%B0%20%D1%81%D1%83%D0%B4%D0%BD%D0%B0.jpg "Добавление нового типа судна")
</details>
</details>

<details><summary>
  
  **Creator**</summary>

  + Creator имеет те же возможности, что и Администратор. Также может создавать/удалять/изменять пользователей. Назначать новые права, менять пароли.

<details><summary>

  *Главная страница*
</summary>

![Главная страница](https://github.com/OksanaZakharovaIP-31/old_web-app/blob/main/pictures/%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F%20%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0%20creator.jpg "Главная страница")
</details>
<details><summary>

  *Список судов*
</summary>

![Список судов](https://github.com/OksanaZakharovaIP-31/old_web-app/blob/main/pictures/%D1%81%D0%BF%D0%B8%D1%81%D0%BE%D0%BA%20%D1%81%D1%83%D0%B4%D0%BE%D0%B2%20crreator.jpg "Список судов")
</details>

<details><summary>

  *Список пользователей*
</summary>

![Список пользователей](https://github.com/OksanaZakharovaIP-31/old_web-app/blob/main/pictures/%D1%81%D0%BF%D0%B8%D1%81%D0%BE%D0%BA%20%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D0%B5%D0%B9%20creator.jpg "Список пользователй")
<details><summary>

  *Фильтр по пользователям*
</summary>

![Фильтр по ползователям](https://github.com/OksanaZakharovaIP-31/old_web-app/blob/main/pictures/%D1%84%D0%B8%D0%BB%D1%8C%D1%82%D1%80%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8F%D0%BC%20creator.jpg "Фильтр по пользователям")
</details>
<details><summary>

  *Поиск по пользователям*
</summary>

![Поиск по пользователям](https://github.com/OksanaZakharovaIP-31/old_web-app/blob/main/pictures/%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%20%D0%BF%D0%BE%20%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8F%D0%BC%20creator.jpg "Поиск по пользователям")
</details>
</details>
<details><summary>

  *Создание нового пользователя*
</summary>

![Создание нового пользователя](https://github.com/OksanaZakharovaIP-31/old_web-app/blob/main/pictures/%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20%D0%BD%D0%BE%D0%B2%D0%BE%D0%B3%D0%BE%20%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8F%20creator.jpg "Создание нового пользователя")
<details><summary>

  *Генерация пароля*
</summary>

![Генерация пароля](https://github.com/OksanaZakharovaIP-31/old_web-app/blob/3198fc0d7a950da43de3f6f12f378f407cf70a7a/pictures/%D1%80%D0%B0%D1%81%D1%87%D0%B5%D1%82%20%D1%82%D0%BE%D0%BF%D0%BB%D0%B8%D0%B2%D0%B0.gif "Генерация пароля")
</details>
</details>
</details>
</details>



# Описание приложения для разработчиков

**Используемые технологии**

*Backend*


1. Python
2. Django
3. Beautifulsoup4 - парсинг с сайта [MarineTraffic](https://www.marinetraffic.com/en/ais/home/centerx:27.1/centery:60.1/zoom:7)
4. Request


*Frontend*

1. Bootstrap
2. Jquery
3. HTML
4. CSS

*Database*

1. MySQL

<details><summary>

  **База данных**
</summary>

**Таблицы**

В начале названия таблиц (перед нижним подчеркиванием) стоит название приложения, созданное во фреймворке


1. ***user_person***


Таблица для хранение данняъ о пользователе


| Name | Type | Description |
| --- | --- | --- |
| id | BIGINT | Первичный ключ |
| name | VARCHAR | Полное имя пользователя |
| photo | VARCHAR | Ссылка на фото |
| login | VARCHAR | Логин для входа |
| password | VARCHAR | Пароль для входа |
| type | VARCHAR | Тип |
| first_name | VARCHAR | Имя |
| secomd_name | VARCHAR | Фамилия |


2. ***user_type***

Таблица для хранения типов суден


| Name | Type | Description |
| --- | --- | --- |
| id | BIGINT | Первичный ключ |
| type | VARCHAR | Тип |

3. ***user_fuel***

Таблица используется для хранения постоянных данных и коэффициентов для расчета необходимого количества топлива для заданного судна. Для вычисления используется формула, разработанная Лабораторией топлив и масел ЗАО «ЦНИИМФ». 

**Формула**

$$ 𝐇=((𝐜∗𝐛_𝐫+𝐛_в+𝐊∗𝐛_𝐜 )∗𝐍∗[𝟏𝟎]^𝟑)/(𝐐∗𝐕∗(𝟏−𝐗)) $$


| Name | Type | Description |
| --- | --- | --- |
| vissel_id | BIGINT | Связь с таблицей user_vissel |
| b_r | VARCHAR | Удельный расход топлива главным двигателем по заданной мощности, кг. усл. Топлива/кВт.ч |
| b_b | VARCHAR | Удельный расход топлива на работу вспомогательных механизмов в ходе по построечной мощности, кг. усл. топлива/кВт.ч |
| b_c | VARCHAR | Удельный расход топлива на стояночных и маневренных режимах по построечной мощности, кг. усл. Топлива/кВт.ч |
| N | VARCHAR | Построечная мощность главного двигателя, кВт |
| Q | VARCHAR | Плановая грузоподъемность судна, т |
| V | VARCHAR | Заданная чистая техническая скорость, узлов |
| C | VARCHAR | Коэффициент использования построечной мощности |
| K | VARCHAR | Коэффициент стояночного времени |
| X | VARCHAR | Коэффициент снижения заданной технической скорости, учитывающий планируемые условия эксплуатации |
| E | VARCHAR | Коэффициент влияния на норму прочих, неучтенных факторов |


4. ***user_vessels***


Таблица с данными о судне


| Name | Type | Description |
| --- | --- | --- |
| id | BIGINT | Первичный ключ |
| name | VARCHAR | Название судна |
| photo | VARCHAR | Ссылка на фото |
| type_id  | BIGINT | Тип судна |
| IMO  | INT | IMO судна, т.е. уникальный идентификатор судна |
| User_id | BIGINT | Прикрепленный пользователь |
| Latitude | VARCHAR | Координаты долготы местонахождения судна |
| Longitude | VARCHAR | Координаты широты местонахождения судна |
| Name_in_en | VARCHAR | Названия судна на английском языке |
| Icon | VARCHAR | Иконка, определяющая состояние суда на карте |

<details>
<summary>

 *Схема*
</summary>

  ![База данных](https://github.com/OksanaZakharovaIP-31/old_web-app/blob/main/pictures/bd.jpg "База данных")
</details>
</details>

**Установка зависимостей**

`pip install -r requirements.txt`

Файл находится в папке [mysite](https://github.com/OksanaZakharovaIP-31/old_web-app/tree/main/mysite)
