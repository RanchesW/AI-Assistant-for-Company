# AI Assistant Roadmap

## 1. Сбор Данных и Настройка Доступа

### Подключение к Базе Данных Oracle: 

**1) Получение Учетных Данных Доступа:**

Сбор учетных данных (имя пользователя, пароль, SID базы данных) у системного администратора или базы данных.

Настройка безопасного хранения учетных данных, используя средства управления секретами (например, AWS Secrets Manager).

**2) Настройка Подключения:**

Использование драйвера Oracle JDBC для подключения к базе данных Oracle.

Настройка сетевой конфигурации и разрешений доступа, включая файрволы и VPN, если требуется, для обеспечения безопасного соединения.

**3) Интеграция с Программой:**

Интеграция подключения к базе данных в приложение используя cx_Oracle — модуль расширения в Python, который включает доступ к базе данных Oracle, обеспечив возможность выполнения SQL-запросов для получения необходимых данных.

Обработка данных, полученных из базы данных, для дальнейшего использования в ИИ модели и других компонентах системы.

### Сбор дополнительных данных:

Разработать или приобрести словарь рабочего жаргона, специфичного для работы на АЗС, для улучшения поисковых возможностей.

Собрать информацию о типичных инцидентах и процедурах для создания комплексной базы знаний.

## 2. Технические Спецификации и Настройка Инфраструктуры
   
### Технические спецификации:

![image](https://github.com/user-attachments/assets/b020bdb9-0495-40b0-a8a7-6a67bf7f3ed8)

**Эти сервера были выбраны среди других так как:**

Серия инференциальных инстансов inf2 AWS использует специализированные чипы Inferentia2, которые оптимизированы для работы с моделями машинного обучения, такими как Llama.
Эти инстансы обеспечивают высокую производительность и энергоэффективность, что важно для обработки больших объемов данных и работы с сложными моделями.
Большие объемы оперативной памяти и пропускная способность сети позволяют эффективно обрабатывать данные и уменьшать задержки.


### Настройка инфраструктуры:

Настроить необходимую инфраструктуру на AWS, включая EC2-инстансы, S3-хранилище и другие релевантные сервисы.

Настроить окружение для поддержки развертывания AI модели и обработки данных.

## 3. Разработка ИИ Модели и Бота 
   
### Интеграция модели:

Интегрировать модель Llama 8B в систему, обеспечив её способность эффективно обрабатывать и понимать запросы.

Реализовать возможности понимания естественного языка (NLU) и генерации естественного языка (NLG) для бота.

### Разработка бота:

Разработать универсального чатбота, способного выполнять широкий спектр задач, включая предоставление инструкций, генерацию отчетов и ответы на запросы.

Реализовать способность бота работать с различными форматами данных (JSON, CSV, XML).

## 4. OCR и Обработка Данных 

### Рассмотрим варианты использования OCR:

Google Document AI: Платное, но мощное решение с AI.

ABBYY FineReader: Обновленный OCR с встроенным AI.

Yandex OCR: Хорошо работающая на русском языке.

**Можно использовать Google Document AI, платная но очень сильную OCR:**
![image](https://github.com/user-attachments/assets/67bb9e3f-04c5-4052-901f-ada0a4eb5762)

**Можно использовать новый OCR со встроенным AI от ABBY FineReader:**
![image](https://github.com/user-attachments/assets/eb0b9ba3-a811-42ec-87ce-77c72a72ecc6)

**Можно использовать Yandex Vision OCR разработана впервую очередь для русского языка:**
![image](https://github.com/user-attachments/assets/5b5748af-d9db-4c8c-8167-4143a49e3ea0)

Интегрировать решение OCR в систему, обеспечив возможность конвертации данных из изображений в текст.

### Можно обойтись бесплатной версией OCR Tesseract:
Однако, чтобы повысить качество вывода русского текста, нужно будет обучить его с помощью ИИ.

### Интерпретация и форматирование данных:

Разработать конвейер для обработки данных OCR, конвертируя их в структурированные форматы данных, такие как JSON, CSV или XML.

Реализовать функции поиска и извлечения, чтобы сделать извлеченные данные легко доступными для ИИ.

## 5. Тестирование и Оптимизация

### Обучение модели на данных:

Подключите ИИ к базе данных Oracle для обучения. Используйте данные, полученные через OCR, для обучения модели. Это включает предварительную обработку данных, настройку гиперпараметров и тестирование модели для достижения высокой точности.
   
### Функциональное тестирование:

ИИ Ассистент почти готов к использованию, и мы уже реализовали анализ данных из различных форматов документов. Проведена работа по поиску и суммаризации данных в каждом загруженном файле, что позволяет пользователям загружать документы для анализа. Осталось подключить ИИ для обучения на данных, поступающих из базы данных Oracle, чтобы программа молга эффективно обрабатывать и понимать всю получаемую информацию. Это позволит полностью автоматизировать процесс анализа и обработки данных, обеспечивая пользователям удобный доступ к необходимой информации.

### Оптимизация производительности:

Оптимизировать производительность системы, сосредоточив внимание на времени отклика и точности модели ИИ.
Обеспечить способность системы справляться с одновременными запросами и большими объемами данных.

## 6. Внедрение и Обучение 
   
### Развертывание системы:

Развернуть систему на инфраструктуре AWS, убедившись, что все компоненты правильно настроены и защищены.
Настроить мониторинг и ведение логов для отслеживания производительности системы и выявления потенциальных проблем.

### Обучение пользователей и документация:

Провести обучающие сессии для конечных пользователей, включая операторов, руководителей и других сотрудников.
Разработать полную документацию, включая руководства пользователя, технические руководства и часто задаваемые вопросы.

## 7. Работа Программы для Пользователей и Примеры Сценариев

### 1) Обучение и Поддержка Операторов АЗС:

**Пример:** Оператор может запросить инструкцию по определенному типу оборудования или процедуре. Бот ищет релевантную информацию в базе знаний и предоставляет инструкции шаг за шагом.

**Описание:** Программа предоставляет ответы на часто задаваемые вопросы, инструкции по безопасной эксплуатации оборудования и решению инцидентов.

### 2) Анализ Данных и Отчетность:

**Пример:** Руководитель АЗС хочет получить отчет о последних инцидентах на станции. Бот генерирует отчет, собирая данные из базы данных и OCR-обработанных документов.

**Описание:** Система может автоматически создавать отчеты по различным параметрам, таким как типы инцидентов, время их возникновения и принятые меры.

### 3) Поддержка Клиентов и Обратная Связь:

**Пример:** Клиент сообщает о проблеме с автозаправкой через онлайн-форму. Бот автоматически обрабатывает запрос, классифицирует его и передает ответственным лицам.

**Описание:** Программа помогает в обработке запросов клиентов, обеспечивая быстрое и точное реагирование на возникающие проблемы.

### 4) Интеграция с OCR и Обработка Документов:

**Пример:** Оператор загружает фотографию отчета о проверке оборудования. OCR конвертирует изображение в текст, который затем используется для обновления базы данных.

**Описание:** Программа интегрирована с OCR-системой для конвертации изображений в текст, что позволяет автоматизировать обработку документов и улучшить точность данных.

## 8. Поддержка и Постоянное Улучшение

### Мониторинг и Обратная Связь:

Постоянный мониторинг производительности системы и сбор отзывов пользователей.
Обеспечение регулярных обновлений и исправлений, основываясь на пользовательских отзывах и изменениях в бизнес-процессах.

### Улучшение системы:

Реализовывать обновления и новые функции на основе отзывов пользователей и изменяющихся бизнес-потребностей.
Расширять базу знаний и возможности бота по мере необходимости.

## Другой путь

**Если делать ИИ полностью под нужды компании, то его придется полностью обучать на данных с БД Oracle.**

### Обучение модели LLaMA на базе данных Oracle

**1. Подготовка данных**

Экспорт данных: Извлечение данных из Oracle в форматы CSV, JSON или Parquet. Это позволяет легко интегрировать данные в процесс обучения.

Очистка и разметка: Удаление ошибок, дубликатов и приведение данных к единому формату. Разметка данных, если это необходимо для понимания контекста.

**2. Настройка инфраструктуры**

Аппаратное обеспечение: Использование мощных GPU (например, NVIDIA A100) или AWS Trainium для обработки больших объемов данных и сложных моделей.

![image](https://github.com/user-attachments/assets/fef609ae-5307-4249-a79f-5c5a08ac72c5)


Программное обеспечение: Установка PyTorch или TensorFlow и необходимых библиотек, таких как Hugging Face Transformers, для работы с LLaMA.

**3. Обучение модели**

**RLHF Метод:** Обучение с подкреплением на основе обратной связи от человека (RLHF) — это метод, при котором ИИ улучшает свои навыки, получая обратную связь от людей. 
Таким образом, ИИ обогащает процесс обучения реальными человеческими интуициями. 
В RLHF ИИ не просто использует данные для принятия решений, но и учитывает, что люди считают полезным или релевантным. 
Это особенно полезно для задач обработки естественного языка, где требуется человеческий подход, например, для создания контента, который действительно находит отклик у людей. 
Включение обратной связи от людей позволяет моделям более точно соответствовать человеческим целям и предпочтениям, что является значительным шагом вперед в приложениях генеративного ИИ, включая большие языковые модели.

**Импорт предобученной модели:** Загрузка LLaMA из библиотек, таких как Hugging Face.

**Fine-tuning:** Настройка модели на ваших данных. Это включает подбор гиперпараметров, таких как скорость обучения и количество эпох, для оптимальной производительности.

**Мониторинг процесса:** Постоянное отслеживание метрик, таких как потеря и точность, для корректировки процесса обучения.

**4. Оценка и оптимизация**

Тестирование: Проведение тестирования модели на тестовых данных, чтобы оценить её способность обрабатывать новые данные.

Оптимизация: При необходимости, настройка гиперпараметров или изменение архитектуры модели для улучшения результатов.

**5. Развертывание и мониторинг**

Развертывание: Подготовка модели для работы в реальной среде, интеграция с системами компании.

Мониторинг: Постоянный мониторинг производительности модели и её адаптация к изменениям в данных или требованиях.

**Результаты и выгоды**

Повышение точности анализа данных: Модель LLaMA, обученная на специфических данных компании, будет лучше понимать контекст и специфику бизнеса.

Оптимизация ресурсов: Использование облачных сервисов и распределенного обучения позволяет сократить время и затраты на обучение.

Персонализация и адаптация: Модель адаптирована к уникальным требованиям компании, что повышает её полезность и точность.


