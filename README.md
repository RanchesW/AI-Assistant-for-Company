# AI Assistant Roadmap

## Содержание

1. Сбор Данных и Настройка Доступа
   - [Подключение к Базе Данных Oracle](#подключение-к-базе-данных-oracle)
   - [Сбор дополнительных данных](#сбор-дополнительных-данных)

2. Выбор облачного сервера: AWS или Azure
   - [Сравнение мощностей](#сравнение-мощностей)
   - [Детальное сравнение AWS Trn1.2xlarge и Azure NVv4-Series](#детальное-сравнение-aws-trn12xlarge-и-azure-nvv4-series)

3. Развертывание AWS сервера
   - [Настройка инфраструктуры](#настройка-инфраструктуры)
   - [Технические Спецификации](#технические-спецификации)
   - [Подготовка данных](#подготовка-данных)
   - [Обучение модели](#обучение-модели)
   - [Оценка и оптимизация](#оценка-и-оптимизация)
   - [Развертывание и мониторинг](#развертывание-и-мониторинг)
   - [Результаты и выгоды](#результаты-и-выгоды)

4. Техническая часть внедрения
   - [Развертывание инфраструктуры AWS](#развертывание-инфраструктуры-aws)
   - [Подключение базы данных Oracle к AWS](#подключение-базы-данных-oracle-к-aws)
   - [Запуск кода Python с использованием Llama 3 8B через AWS](#запуск-кода-python-с-использованием-llama-3-8b-через-aws)
   - [Связывание базы данных Oracle с ИИ (Llama 3)](#связывание-базы-данных-oracle-с-ии-llama-3)
   - [Мониторинг, безопасность и оптимизация](#мониторинг-безопасность-и-оптимизация)

5. OCR и Обработка Данных
   - [Рассмотрим варианты использования OCR](#рассмотрим-варианты-использования-ocr)
   - [Интерпретация и форматирование данных](#интерпретация-и-форматирование-данных)

6. Тестирование и Оптимизация
   - [Обучение модели на данных](#обучение-модели-на-данных)
   - [Функциональное тестирование](#функциональное-тестирование)
   - [Оптимизация производительности](#оптимизация-производительности)

7. Внедрение и Обучение
   - [Развертывание системы](#развертывание-системы)
   - [Обучение пользователей и документация](#обучение-пользователей-и-документация)

8. Работа Программы для Пользователей и Примеры Сценариев
   - [Обучение и Поддержка Операторов АЗС](#обучение-и-поддержка-операторов-азс)
   - [Анализ Данных и Отчетность](#анализ-данных-и-отчетность)
   - [Поддержка Клиентов и Обратная Связь](#поддержка-клиентов-и-обратная-связь)
   - [Интеграция с OCR и Обработка Документов](#интеграция-с-ocr-и-обработка-документов)

9. Поддержка и Постоянное Улучшение
   - [Мониторинг и Обратная Связь](#мониторинг-и-обратная-связь)
   - [Улучшение системы](#улучшение-системы)

10. Роли в проекте
    - [Data-Scientist](#data-scientist)
    - [Инженер ИИ/МО](#инженер-иимо)
    - [Бэкенд-разработчик](#бэкенд-разработчик)

11. [План по времени для разработки AI ассистента с использованием AWS и Tesseract](#план-по-времени-для-разработки-ai-ассистента-с-использованием-aws-и-tesseract)



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

## 2. Выбор облачного сервера: AWS или Azure

**AWS:**

AWS — безусловный лидер, предлагающий наибольшее количество сервисов и глобальную инфраструктуру. Подходит для сложных проектов и корпораций благодаря гибкости и надежности. AWS имеет наиболее зрелую экосистему и лучший выбор для предприятий, стремящихся к максимальной универсальности и поддержке.

**Azure:**

Azure занимает нишу между AWS и Google Cloud, с сильными сторонами в интеграции с продуктами Microsoft. Он подходит для организаций, использующих экосистему Microsoft, но уступает AWS по охвату и стабильности.

**Вывод:**

### Сравнение мощностей

AWS — лучший выбор для крупных и сложных проектов. Google Cloud и Azure хороши для специфических задач, но не достигают универсальности AWS.

### Детальное сравнение AWS Trn1.2xlarge и Azure NVv4-Series

| Характеристика        | AWS Trn1.2xlarge                        | Azure NVv4-Series (NV8as_v4)                |
|-----------------------|-----------------------------------------|--------------------------------------------|
| **Процессор**         | 8 vCPU                                  | 8 vCPU                                     |
| **Память**            | 32 ГБ                                   | 28-32 ГБ                                   |
| **Тип GPU**           | AWS Trainium, 1 чип                     | AMD EPYC 7V12 (1/8 до полной GPU)         |
| **Хранилище**         | 0.5 ТБ NVMe SSD                         | Варьируется в зависимости от конфигурации |
| **Сеть**              | До 12.5 Гбит/с                          | До 10 Гбит/с                              |
| **Стоимость**         | $1.34 за час (on-demand), $0.79 за час (1 год резервирования), $0.4744 за час (3 года резервирования) | Примерно $1.20 за час (1/8 GPU), до $4.30 за час (полная GPU, on-demand) |
| **Особенности**       | Поддерживает широкий спектр типов данных (FP32, TF32, BF16 и другие) | Различные конфигурации GPU, от 1/8 до полной GPU |

**Источник данных**:
- Amazon Web Services, Inc.
- Vantage
- Microsoft Azure официальные данные

### Итог:

**AWS Trn1.2xlarge** обеспечивает высокую производительность для глубокого обучения благодаря **AWS Trainium** чипам и специализированной инфраструктуре, оптимизированной для ИИ задач. Он лучше подходит для крупных проектов, где требуется максимальная производительность и поддержка различных типов данных.

**Azure** предлагает конфигурации **NVv4-Series** с гибкими вариантами GPU и конкурентоспособными ценами, но для задач глубокого обучения может потребоваться полная GPU конфигурация, что увеличивает стоимость. Azure может быть менее подходящим выбором для специализированных задач ИИ по сравнению с AWS.

Таким образом, **AWS Trn1.2xlarge** является лучшим выбором для высокопроизводительных задач глубокого обучения, в то время как Azure может подойти для менее интенсивных задач или когда требуется интеграция с экосистемой Microsoft.

## 3. Развертывания AWS сервера
   
### Настройка инфраструктуры

Аппаратное обеспечение: Использование мощных GPU (например, NVIDIA A100) или AWS Trainium для обработки больших объемов данных и сложных моделей.

![image](https://github.com/user-attachments/assets/fef609ae-5307-4249-a79f-5c5a08ac72c5)

Программное обеспечение: Установка PyTorch или TensorFlow и необходимых библиотек, таких как Hugging Face Transformers, для работы с LLaMA.

### Технические Спецификации

AWS Trainium был выбран для обучения модели LLaMA из-за ряда преимуществ, которые он предлагает. Trainium — это процессор, разработанный Amazon специально для машинного обучения, с упором на эффективность и производительность. 

**Он обеспечивает:**

**Высокую производительность:** Trainium оптимизирован для выполнения задач машинного обучения с высокой скоростью, что особенно важно при обучении моделей глубокого обучения, таких как LLaMA.

**Снижение затрат:** Использование Trainium может быть более экономически выгодным по сравнению с другими решениями, благодаря его энергоэффективности и оптимизации для рабочих нагрузок ИИ.

**Широкая поддержка фреймворков:** AWS Trainium поддерживает основные фреймворки машинного обучения, такие как TensorFlow и PyTorch, что облегчает интеграцию и работу с существующими проектами.

### Подготовка данных

Экспорт данных: Извлечение данных из Oracle в форматы CSV, JSON или Parquet. Это позволяет легко интегрировать данные в процесс обучения.

Очистка и разметка: Удаление ошибок, дубликатов и приведение данных к единому формату. Разметка данных, если это необходимо для понимания контекста.

### Для запуска своего сервера требуется:

**Процессор:** Высокопроизводительный многоядерный процессор, например, AMD Threadripper или Intel Xeon.

**Оперативная память:** 128 ГБ и больше.

**Графическая карта:** Несколько высокопроизводительных GPU, таких как NVIDIA A100 или RTX 3090, желательно с большим объемом видеопамяти (24 ГБ и выше).

**Хранилище:** SSD на 2 ТБ или больше, предпочтительно с высокой скоростью чтения/записи.

**Операционная система:** Современная версия Linux для лучшей поддержки многопроцессорности и работы с GPU.

### Обучение модели

**Импорт предобученной модели:** Загрузка LLaMA из библиотек, таких как Hugging Face.

**Fine-tuning:** Настройка модели на ваших данных. Это включает подбор гиперпараметров, таких как скорость обучения и количество эпох, для оптимальной производительности.

**RLHF Метод:** Обучение с подкреплением на основе обратной связи от человека (RLHF) — это метод, при котором ИИ улучшает свои навыки, получая обратную связь от людей. 
Таким образом, ИИ обогащает процесс обучения реальными человеческими интуициями. 
В RLHF ИИ не просто использует данные для принятия решений, но и учитывает, что люди считают полезным или релевантным. 
Это особенно полезно для задач обработки естественного языка, где требуется человеческий подход, например, для создания контента, который действительно находит отклик у людей. 
Включение обратной связи от людей позволяет моделям более точно соответствовать человеческим целям и предпочтениям, что является значительным шагом вперед в приложениях генеративного ИИ, включая большие языковые модели.

**Мониторинг процесса:** Постоянное отслеживание метрик, таких как потеря и точность, для корректировки процесса обучения.

### Оценка и оптимизация

**Тестирование:** Проведение тестирования модели на тестовых данных, чтобы оценить её способность обрабатывать новые данные.

**Оптимизация:** При необходимости, настройка гиперпараметров или изменение архитектуры модели для улучшения результатов.

### Развертывание и мониторинг

**Развертывание:** Подготовка модели для работы в реальной среде, интеграция с системами компании.

**Мониторинг:** Постоянный мониторинг производительности модели и её адаптация к изменениям в данных или требованиях.

### Результаты и выгоды

**Повышение точности анализа данных:** Модель LLaMA, обученная на специфических данных компании, будет лучше понимать контекст и специфику бизнеса.

**Оптимизация ресурсов:** Использование облачных сервисов и распределенного обучения позволяет сократить время и затраты на обучение.

**Персонализация и адаптация:** Модель адаптирована к уникальным требованиям компании, что повышает её полезность и точность.

## 4. Техническая часть внедрения

### Развертывание инфраструктуры AWS

-   **1.1. Создание и настройка AWS инфраструктуры**
   
      Выбор региона и зоны доступности:
      
      Выберите регион, соответствующий вашим требованиям по задержкам и безопасности.
      
      Создание VPC (Virtual Private Cloud):
      
      Создайте VPC для изоляции ресурсов, настройте подсети (публичные и приватные), таблицы маршрутизации и шлюзы (NAT или Internet Gateway).
      
      Настройка безопасности:
      
      Определите Security Groups и Network ACLs для управления трафиком. Убедитесь, что только необходимые порты открыты для необходимых ресурсов.

### Подключение базы данных Oracle к AWS

-   **2.1. Настройка базы данных Oracle**
   
      Опции подключения:
      
      Вы можете использовать Amazon RDS for Oracle, если ваш выбор базы данных поддерживает миграцию на RDS.
      
      Если вы остаетесь на собственной базе данных Oracle, необходимо обеспечить надежное подключение к AWS через VPN или AWS Direct Connect для безопасного и высокопроизводительного соединения.
      
      Настройка Oracle Database на AWS:
      
      Убедитесь, что базы данных имеют соответствующие настройки производительности и безопасности. Это включает в себя управление учетными данными, настройку резервного копирования и мониторинга.

-   **2.2. Установка и настройка cx_Oracle**
   
      Установите Oracle Instant Client на вашей AWS инфраструктуре (EC2 инстанс или Lambda). Это необходимо для использования cx_Oracle с Python для подключения к базе данных Oracle.

### Запуск кода Python с использованием Llama 3 8B через AWS

-   **3.1. Развертывание Llama 3 на AWS**
   
      Использование Amazon EC2:
      
      Запуск инстансов EC2 с соответствующими характеристиками для запуска модели Llama 3 8B. Убедитесь, что у вас достаточно памяти и процессорных мощностей для работы модели.
      
      Использование контейнеров или AMI:
      
      Настройте Docker контейнеры с необходимыми зависимостями или используйте предварительно настроенные AMI (Amazon Machine Images) для быстрого развертывания.

-   **3.2. Запуск Python кода с Llama 3**
   
      Настройка окружения:
      
      Установите все необходимые библиотеки и зависимости, включая Llama 3 SDK или клиентский API.
      
      Пример кода для взаимодействия с Llama 3:
   
      ```
      python
      
      import requests
      
      # URL API Llama 3
      url = "https://api.llama3.example.com/process"
      headers = {
          "Authorization": "Bearer YOUR_API_KEY",
          "Content-Type": "application/json"
      }
      
      # Отправка данных на анализ
      data = {
          "input": "Пример текста для анализа"
      }
      
      response = requests.post(url, headers=headers, json=data)
      result = response.json()
      print(result)
      ```

### Связывание базы данных Oracle с ИИ (Llama 3)

-   **4.1. Извлечение данных из базы данных Oracle**
   
      Использование SQL запросов:
      
      Извлекайте необходимые данные из базы данных Oracle для анализа. Например, получение текстовых данных для дальнейшей обработки ИИ.
      
      ```
      python
      
      import cx_Oracle
      
      dsn_tns = cx_Oracle.makedsn('host', 'port', service_name='service_name')
      connection = cx_Oracle.connect(user='username', password='password', dsn=dsn_tns)
      cursor = connection.cursor()
      cursor.execute("SELECT text_column FROM my_table")
      texts = cursor.fetchall()
      cursor.close()
      connection.close()
      ```

-   **4.2. Анализ данных с помощью Llama 3**
   
      Отправка данных в Llama 3:
      
      После получения данных из базы данных Oracle, отправьте их в Llama 3 для анализа. Пример кода:
      
      ```
      python
      
      for text in texts:
          data = {"input": text[0]}
          response = requests.post(url, headers=headers, json=data)
          result = response.json()
          print(result)
      ```

### Мониторинг, безопасность и оптимизация

- **5.1. Мониторинг и логирование**
  
  - **Amazon CloudWatch:**
    - Настройте Amazon CloudWatch для мониторинга производительности и логирования. Определите ключевые метрики, такие как использование CPU, памяти, сетевого трафика и производительности базы данных. Создайте дашборды для визуализации данных и оповещений для своевременного реагирования на аномалии.
  
  - **Настройка оповещений:**
    - Используйте Amazon CloudWatch Alarms для создания оповещений на основе определенных условий (например, высокое использование ресурсов, неудачные запросы). Оповещения могут быть отправлены по электронной почте или через другие уведомления.

- **5.2. Безопасность**

  **Общие меры безопасности:**
  
  - **AWS IAM (Identity and Access Management):**
    - Определите роли и политики доступа для каждого компонента системы, чтобы обеспечить минимально необходимый доступ.
    - Используйте роли IAM для ограниченного доступа к ресурсам AWS, включая EC2 инстансы, базы данных и хранилище S3.
    - Настройте многофакторную аутентификацию (MFA) для администраторов и ключевых пользователей системы.
  
  - **AWS Secrets Manager:**
    - Используйте AWS Secrets Manager для безопасного хранения и управления секретами, такими как учетные данные для доступа к базе данных Oracle и API-ключи.
    - Автоматическое обновление и ротация секретов для повышения безопасности.

  **Безопасность подключения к базе данных Oracle:**

  - **VPN или AWS Direct Connect:**
    - Используйте VPN или AWS Direct Connect для обеспечения безопасного и высокопроизводительного соединения между вашей локальной инфраструктурой и AWS.
    - Настройка IPsec VPN с шифрованием данных в движении для защиты от прослушивания.

  - **VPC (Virtual Private Cloud):**
    - Разместите базы данных и чувствительные данные в приватных подсетях VPC для ограничения доступа только к необходимым системам и сервисам.
    - Используйте Security Groups и Network ACLs для управления входящим и исходящим трафиком, обеспечивая доступ только из доверенных источников.

  - **Шифрование данных:**
    - Шифруйте данные на уровне базы данных (TDE - Transparent Data Encryption) для защиты данных в покое.
    - Используйте шифрование данных в движении с помощью SSL/TLS для соединений между клиентом и сервером базы данных.

  - **Аудит и логирование:**
    - Включите аудит базы данных для отслеживания доступа к данным и выполнения критически важных команд.
    - Храните журналы аудита в защищенном месте и регулярно проверяйте их на предмет подозрительных действий.

- **5.3. Оптимизация и масштабирование**
  
  - **Авто-масштабирование:**
    - Настройте авто-масштабирование для EC2 инстансов и других компонентов, чтобы автоматически адаптировать ресурсы к изменению нагрузки.
    - Определите метрики для запуска масштабирования, такие как использование CPU или время отклика приложений.
  
  - **Оптимизация производительности базы данных:**
    - Используйте AWS RDS Performance Insights для анализа производительности базы данных и выявления узких мест.
    - Оптимизируйте запросы SQL и индексы для улучшения времени отклика и уменьшения нагрузки на базу данных.
  
  - **Кэширование данных:**
    - Используйте AWS ElastiCache для кэширования часто запрашиваемых данных, чтобы снизить нагрузку на базу данных и улучшить время отклика.
    - Настройте кэширование на уровне приложения для уменьшения обращений к базе данных.
  
  - **Регулярное обновление и патчи:**
    - Обеспечьте регулярное обновление операционных систем, программного обеспечения и баз данных для защиты от известных уязвимостей.
    - Используйте автоматические обновления и уведомления о новых версиях и патчах для своевременного обновления.

## 5. OCR и Обработка Данных 

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

**Можно обойтись бесплатной версией OCR Tesseract:**
Однако, чтобы повысить качество вывода русского текста, нужно будет обучить его с помощью ИИ.

**Сравнение:**

![cd70e96c5dbf47cc2609d8959d9dc2e7](https://github.com/user-attachments/assets/eac82066-5d2a-4f5c-b27b-f3624c5a1d18)

*Рисунок 3 – изображение с плохим освещением, расфокусировкой, наклоном*

**Google Document AI:**

```
1 Bias (Сдвиг цветов спектра областей к тому или иному
диапазона шума);
7 Edge (Ширина перепадов между светлыми и темными участками).
Фильтр Lens Effects Focus
Фильтр Lens Effects Focus (Линзовые эффекты: фокусировка) позволяет
имитировать эффекты расфокусировки изображения или конечной глубины
резкости снимка, приводящей к тому, что в фокусе оказываются только
объекты на определенной дальности от камеры. Для воспроизведения эф-
фекта расфокусировки фильтр использует информацию об удалении объек-
тов от съемочной камеры, хранящуюся в 2-буфере сцены.
Для настройки фильтра фокусировки служит окно диалога Lens Effects Focus
(Линзовые эффекты: фокусировка), появляющееся после щелчка на кнопке
Setup (Настройка) в окне диалога добавления или редактирования фильтра
(рис. 15.35).
Элементы управления просмотром эффекта, сохранением и загрузкой на
бора параметров данного окна аналогичны соответствующим элементам
рассмотренного выше окна диалога Lens Effects Flare (Линзовые эффекты:
блики).
асфокусировки, выполните в окне диалога Lens
```

**FineReader:**

```
Bias (Сдвиг цветов спектра областей к тому или ииожуп диапазона шума);	'
g Edge (Ширина перепадов между светлыми и темными участка^
фильтр Lens Effects Focus
Фильтр Lens Effects Focus (Линзовые эффекты: фокусировка) поз| имитировать эффекты расфокусировки изображения или конечной г; резкости снимка, приводящей к тому, что в фокусе оказываются объекты на определен on лдыюсти от камеры. Для воспроизведения фекта расфокуепро в <	использует информацию об удалении
тов от съемочн	>си в/-буфере сцены.	'Яа
Для настройки	.к и служит окно диалога Lens Effects
(Линзовые эффск	• появляющееся после щелчка на кн
Setup Н..строп к	ciioia добавления или редактирования фг
НИЯ д рос МО гром эффекта, сохранением и загрузке энного окна аналогичны соответствующим эле]
.с окна диалога Lens Effects Flare (Линзовые
пжчЬокусировки, выполните в окне
```

**Tesseract:**

```
p Lens Effects Focus\n\nmp Lens Effects Focus\n\nBrosare эффек\nи снимка\nKTBI на опре\nса расфокус\nот съемоч\n\n \n\nокна J\n\n(Линзовые эффекты: фоку@\nировки изображения HIM\nтому, что в фокусе Okada\nru от камеры. Для BOCHP\nyer информацию об У\n1 в 7-буфере сцены\n\nь\nлужит окно диалога\nзляющееся после\n\n„вления или редактирс\n\n›уфекта, сохраненнО\n\nнотром\n\nго окна ана\nдиалога Lens Effects\n\x0c
OasyOCR:
["цветов спектра областей к Tonу H111 11110 Bins (Сдвиг днапазона шума) ; темными участками ). Edge (Ширина перепадов между светлыми Фильтр Lens Effects Focus эффскты :  фокусировка) позволяся Фильтр   Lens Effects Focus (Линзовыс изображсния или конечной глубины имитировать эффекты расфокусировки фокусс оказываются Толъ0 снимка , приводящей ToMу '10 резкостк от кямеры   Шля воспроизведения эф объекты ня определенной дальности используст информацию об удалении объек- ректа расфокуспровки фильр съемочной камеры , хранящуюся Z-буфере сцены. TOB Lens Effects Focus фокусировки служит окно диалога Для настройки фильтра появляющееся после щелчка на кнопке Линзовые эффекты: фокусироока добявления Цлк редактирования фильтра Sctup ( Настройка) 6 окне дналога IPИC  15.35). сохранением загрузкой I(;1- Элементы управления просмотром эффикна сораетствующим элементам окна аналогичны боре   парамстров ланного Lens Effects Flare (Линзовые эффекты: Bs !@ окна дналога DSCCу отрснного Окики ) выполните окне диалога Dens куспровки , 8"]
```

**Yandex Vision OCR:**

```
Bias (Сдвиг цветов спектра областей
диапазона шума);
Edge (Ширина перепадов между светлыми и темными участками).
Фильтр Lens Effects Focus
Фильтр Lens Effects Focus (Линзовые эффекты: фокусировка) позволяет
имитировать эффекты расфокусировки изображения или конечной глубины
резкости снимка, приводящей к тому, что в фокусе оказываются только
объекты на определенной дальности от камеры. Для воспроизведения эф-
фекта расфокусировки фильтр использует информацию об удалении объек-
тов от съемочной камеры, хранящуюся в Z-буфере сцены.
Для настройки фильтра фокусировки служит окно диалога Lens Effects Focus
(Линзовые эффекты: фокусировка), появляющееся после щелчка на кнопке
Setup (Настройка) в окне диалога добавления или редактирования фильтра
(рис. 15.35).
Элементы управления просмотром эффекта, сохранением и загрузкой на-
бора параметров данного окна аналогичны соответствующим элементам
рассмотренного выше окна диалога Lens Effects Flare (Линзовые эффекты:
блики).
окусировки, в
и выполните в окне диалога Lens
```

### Интерпретация и форматирование данных:

Разработать конвейер для обработки данных OCR, конвертируя их в структурированные форматы данных, такие как JSON, CSV или XML.

Реализовать функции поиска и извлечения, чтобы сделать извлеченные данные легко доступными для ИИ.

## 6. Тестирование и Оптимизация

### Обучение модели на данных:

Подключите ИИ к базе данных Oracle для обучения. Используйте данные, полученные через OCR, для обучения модели. Это включает предварительную обработку данных, настройку гиперпараметров и тестирование модели для достижения высокой точности.
   
### Функциональное тестирование:

ИИ Ассистент почти готов к использованию, и мы уже реализовали анализ данных из различных форматов документов. Проведена работа по поиску и суммаризации данных в каждом загруженном файле, что позволяет пользователям загружать документы для анализа. Осталось подключить ИИ для обучения на данных, поступающих из базы данных Oracle, чтобы программа молга эффективно обрабатывать и понимать всю получаемую информацию. Это позволит полностью автоматизировать процесс анализа и обработки данных, обеспечивая пользователям удобный доступ к необходимой информации.

### Оптимизация производительности:

Оптимизировать производительность системы, сосредоточив внимание на времени отклика и точности модели ИИ.
Обеспечить способность системы справляться с одновременными запросами и большими объемами данных.

## 7. Внедрение и Обучение 
   
### Развертывание системы:

Развернуть систему на инфраструктуре AWS, убедившись, что все компоненты правильно настроены и защищены.
Настроить мониторинг и ведение логов для отслеживания производительности системы и выявления потенциальных проблем.

### Обучение пользователей и документация:

Провести обучающие сессии для конечных пользователей, включая операторов, руководителей и других сотрудников.
Разработать полную документацию, включая руководства пользователя, технические руководства и часто задаваемые вопросы.

## 8. Работа Программы для Пользователей и Примеры Сценариев

### Обучение и Поддержка Операторов АЗС:

**Пример:** Оператор может запросить инструкцию по определенному типу оборудования или процедуре. Бот ищет релевантную информацию в базе знаний и предоставляет инструкции шаг за шагом.

**Описание:** Программа предоставляет ответы на часто задаваемые вопросы, инструкции по безопасной эксплуатации оборудования и решению инцидентов.

### Анализ Данных и Отчетность:

**Пример:** Руководитель АЗС хочет получить отчет о последних инцидентах на станции. Бот генерирует отчет, собирая данные из базы данных и OCR-обработанных документов.

**Описание:** Система может автоматически создавать отчеты по различным параметрам, таким как типы инцидентов, время их возникновения и принятые меры.

### Поддержка Клиентов и Обратная Связь:

**Пример:** Клиент сообщает о проблеме с автозаправкой через онлайн-форму. Бот автоматически обрабатывает запрос, классифицирует его и передает ответственным лицам.

**Описание:** Программа помогает в обработке запросов клиентов, обеспечивая быстрое и точное реагирование на возникающие проблемы.

### Интеграция с OCR и Обработка Документов:

**Пример:** Оператор загружает фотографию отчета о проверке оборудования. OCR конвертирует изображение в текст, который затем используется для обновления базы данных.

**Описание:** Программа интегрирована с OCR-системой для конвертации изображений в текст, что позволяет автоматизировать обработку документов и улучшить точность данных.

## 9. Поддержка и Постоянное Улучшение

### Мониторинг и Обратная Связь:

Постоянный мониторинг производительности системы и сбор отзывов пользователей.
Обеспечение регулярных обновлений и исправлений, основываясь на пользовательских отзывах и изменениях в бизнес-процессах.

### Улучшение системы:

Реализовывать обновления и новые функции на основе отзывов пользователей и изменяющихся бизнес-потребностей.
Расширять базу знаний и возможности бота по мере необходимости.

## 10. Роли в проекте:
  
### Data-Scientist
**от 500,000 KZT до 750,000 KZT**  
**Роль:** Разработка и внедрение моделей машинного обучения, предобработка и анализ данных.

**Обязанности:**

+ Сбор и предобработка данных.

+ Выбор и обучение моделей.

+ Оценка и оптимизация производительности.

**Требования:**

+ Владение алгоритмами машинного обучения.

+ Опыт работы с Python, R или аналогичными языками программирования.

+ Сильные навыки статистического анализа.

+ Знание инструментов, таких как TensorFlow, PyTorch и т.д.

### Инженер ИИ/МО 
**от 590,000 KZT до 786,600 KZT**

**Роль:** Внедрение и поддержка решений ИИ/МО, оптимизация алгоритмов для производительности.

**Обязанности:**

+ Разработка и развертывание моделей ИИ.

+ Оптимизация алгоритмов для эффективности и масштабируемости.

+ Интеграция моделей в существующие системы.

**Требования:**

+ Сильные навыки программирования (Python, Java, C++ и т.д.).

+ Опыт работы с облачными платформами (AWS, GCP, Azure).

+ Понимание фреймворков глубокого обучения.

+ Знание практик DevOps.

### Бэкенд-разработчик 
**от 416,667 KZT до 666,667 KZT**

**Роль:** Разработка и поддержка серверной логики, баз данных и обеспечение высокой производительности.

**Обязанности:**

+ Разработка и интеграция API.

+ Проектирование и управление базами данных.

+ Обеспечение масштабируемости и производительности.

**Требования:**

+ Владение языками бэкенд-разработки (Node.js, Python, Java и т.д.).

+ Опыт работы с системами управления базами данных (MySQL, PostgreSQL и т.д.).

+ Знание RESTful API и микросервисной архитектуры.


## План по времени для разработки AI ассистента с использованием AWS и Tesseract

Проект разработки AI ассистента включает в себя несколько этапов, каждый из которых требует времени и ресурсов для выполнения. Учитывая выбор AWS для облачной инфраструктуры и Tesseract для OCR, давайте детализируем план с оценкой времени.

### 1. Сбор и настройка данных (2.5 недели)

**1.1. Настройка подключения к базе данных Oracle (1 неделя)**
- **Получение учетных данных:** Обеспечение доступа к базе данных.
- **Настройка подключения:** Использование драйвера Oracle JDBC или cx_Oracle для Python.
- **Безопасность и управление секретами:** Настройка безопасного хранения учетных данных (например, AWS Secrets Manager).

**1.2. Настройка и интеграция OCR (1.5 недели)**
- **Интеграция Tesseract OCR:** Установка и настройка Tesseract на AWS.
- **Оптимизация изображений для OCR:** Подготовка изображений для улучшения распознавания (например, увеличение контрастности).

### 2. Настройка облачной инфраструктуры (3 недели)

**2.1. Настройка инфраструктуры (3 недели)**
- **Создание и настройка VPC, подсетей и безопасности:** Настройка сети и безопасности.
- **Развертывание серверов и баз данных:** Настройка EC2 инстансов, баз данных RDS.
- **Настройка мониторинга и логирования:** Использование CloudWatch для отслеживания производительности и логов.

### 3. Разработка и обучение моделей ИИ (2-3 месяца)

**3.1. Сбор и предобработка данных (1 месяц)**
- **Экспорт данных из Oracle:** Извлечение и очистка данных для обучения.
- **Подготовка данных для обучения:** Нормализация и разметка данных.

**3.2. Разработка и обучение моделей (1-2 месяца)**
- **Разработка моделей на основе глубокого обучения:** Использование PyTorch или TensorFlow.
- **Обучение моделей на AWS:** Использование GPU-инстансов для ускорения обучения.
- **Тестирование и валидация моделей:** Проверка точности и эффективности.

### 4. Разработка серверной логики и API (1.5 месяца)

**4.1. Разработка серверной части (1 месяц)**
- **Создание бэкенд-сервиса:** Реализация логики обработки запросов.
- **Интеграция с базой данных и моделями ИИ.**

**4.2. Разработка и интеграция API (2 недели)**
- **Разработка API для взаимодействия с Telegram ботом и другими системами.**
- **Документация API.**

### 5. Интеграция и тестирование системы (1-2 месяца)

**5.1. Интеграция компонентов системы (1 месяц)**
- **Объединение всех модулей в единую систему.**
- **Проверка взаимодействия всех компонентов.**

**5.2. Тестирование системы (1 месяц)**
- **Функциональное тестирование:** Проверка на соответствие требованиям.
- **Оптимизация производительности:** Настройка системы для лучшей производительности.

### 6. Внедрение и обучение пользователей (3 недели)

**6.1. Развертывание системы (2 недели)**
- **Запуск в продакшн:** Подготовка и развертывание системы.
- **Настройка резервного копирования и отказоустойчивости.**

**6.2. Обучение пользователей и документация (1 неделя)**
- **Подготовка обучающих материалов:** Руководства и инструкции.
- **Проведение обучающих сессий.**

### Причины оценки времени:

**Комплексность системы:** Включает множество компонентов, таких как OCR, обработка естественного языка, взаимодействие с базой данных и облачной инфраструктурой.

**Требования к данным:** Сбор, очистка и подготовка данных требуют значительного времени, особенно если данные находятся в различных форматах.

**Интеграция и тестирование:** Интеграция различных компонентов системы и тестирование на предмет совместимости и производительности требуют тщательной работы.

**Безопасность и соответствие требованиям:** Обеспечение безопасности данных и соответствие нормативным требованиям также требуют времени на реализацию и проверку.
