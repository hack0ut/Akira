# Акира - Система удаленного управления [RU]
Акира - это проект, который позволит его пользователям управлять событиями вашей операционной системой даже без доступа к персональному компьютеру. Инструкция по установке:

=== Для пользователей Windows 10/Windows 11:
1. Установите репозиторий на свой личный компьютер
2. Разархивируйте установленный файл в удобное вам место
3. Открыть файл по расположению install/Akira.msi
4. Следовать указаниям установщика
5. Запустить программу.
6. В папке с установленной программой появится файл config.json. Откройте его любым текстовым редактором и проследуйте в Telegram.
7. Создайте своего бота при помощи https://t.me/BotFather
8. Внесите токен вашего бота в config.json в соответствующее поле.
9. Напишите боту https://t.me/getmyid_bot, после чего он отправит сообщение по типу:
Your user ID: 1234567890
Current chat ID: 1234567890
10. Скопируйте любое из значений, и внесите его в config.json (Поле trusted_id)
ВАЖНО!!! Скопированный ID должен быть в кавычках! Пример: https://imgur.com/a/p81N7RZ
11. Напишите вашему боту сообщение с любым содержанием (Ссылку на вашего бота выдает BotFather вместе с токеном)
12. Запустите программу akira.exe
Если вы сделали все правильно, бот пришлет вам сообщение о появлении нового устройства в сети.

=== Если вы хотите чтобы Акира запускалась вместе с системой:
1. Создайте ярлык установленного приложения akira.exe 
Нажмите правой кнопкой мыши по приложению (Если у вас Windows 11, выделите приложение и нажмите SHIFT + F10) -> Отправить -> Рабочий стол (создать ярлык)
2. Нажмите WIN + R
3. Введите в открывшееся окно "shell:startup" (без кавычек)
4. Перетащите туда ваш ярлык
5. Перезапустите систему

=== Если вы опытный пользователь, и хотите запустить Акиру при помощи исходного кода:
1. Установите репозиторий на свой личный компьютер
2. Разархивируйте установленный файл в удобное вам место
3. Удалите папку installer
4. Установите зависимости из файла requirements.txt (pip install -r requirements.txt)
5. Запустите программу main.py (python main.py). В случае успеха появится окно о создании config.json
6. Откройте config.json любым текстовым редактором и проследуйте в Telegram.
7. Создайте своего бота при помощи https://t.me/BotFather
8. Внесите токен вашего бота в config.json в соответствующее поле.
9. Напишите боту https://t.me/getmyid_bot, после чего он отправит сообщение по типу:
Your user ID: 1234567890
Current chat ID: 1234567890
10. Скопируйте любое из значений, и внесите его в config.json (Поле trusted_id)
ВАЖНО!!! Скопированный ID должен быть в кавычках! Пример: https://imgur.com/a/p81N7RZ
11. Напишите вашему боту сообщение с любым содержанием (Ссылку на вашего бота выдает BotFather вместе с токеном)
12. Запустите программу main.py
В случае успеха, Акира будет запущена и будет работать до тех пор, пока вы не завершите работу кода (Файла main.py)

# Akira - Remote control system [EN]
Akira is a project that will allow its users to manage the events of your operating system even without access to a personal computer. Installation Instructions:

=== For Windows 10/Windows 11 users:
1. Install the repository on your personal computer
2. Unzip the installed file to a convenient location
3. Open the file by location install/Akira.msi
4. Follow the instructions of the installer
5. Launch the program.
6. The config.json file will appear in the folder with the installed program. Open it with any text editor and follow it to Telegram.
7. Create your bot using https://t.me/BotFather
8. Enter your bot's token in config.json in the corresponding field.
9. Write to the bot https://t.me/getmyid_bot , after which it will send a message by type:
Your user ID: 1234567890
Current chat ID: 1234567890
10. Copy any of the values and add it to config.json (trusted_id field)
important!!! The copied ID must be in quotes! Example: https://imgur.com/a/p81N7RZ
11. Write your bot a message with any content (A link to your bot is issued by BotFather along with a token)
12. Run the program akira.exe
If you have done everything correctly, the bot will send you a message about the appearance of a new device on the network.

=== If you want Akira to run with the system:
1. Create a shortcut of the installed application akira.exe 
Right-click on the application (If you have Windows 11, highlight the application and press SHIFT + F10) -> Send -> Desktop (create shortcut)
2. Press WIN + R
3. Enter "shell:startup" (without quotes) in the window that opens
4. Drag your shortcut there
5. Restart the system

=== If you are an experienced user and want to run Akira using the source code:
1. Install the repository on your personal computer
2. Unzip the installed file to a convenient location
3. Delete the installer folder
4. Install the dependencies from the file requirements.txt (pip install -r requirements.txt )
5. Run the program main.py (python main.py ). If successful, a window will appear about creating config.json
6. Open config.json with any text editor and follow in Telegram.
7. Create your bot using https://t.me/BotFather
8. Enter your bot's token in config.json in the corresponding field.
9. Write to the bot https://t.me/getmyid_bot , after which it will send a message by type:
Your user ID: 1234567890
Current chat ID: 1234567890
10. Copy any of the values and add it to config.json (trusted_id field)
important!!! The copied ID must be in quotes! Example: https://imgur.com/a/p81N7RZ
11. Write your bot a message with any content (A link to your bot is issued by BotFather along with a token)
12. Run the program main.py
If successful, Akira will be launched and will run until you finish the code (File main.py )