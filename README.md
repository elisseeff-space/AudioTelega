# AudioTelega
 Try to get Audio from Telegram Bot

Клонируйте репозиторий и перейдите в него в командной строке:

git clone https://github.com/tochilkinva/tg_bot_stt_tts.git
cd tg_bot_stt_tts
Cоздайте и активируйте виртуальное окружение:

python -m venv venv
. env/Scripts/activate
Установите зависимости из файла requirements.txt:

python -m pip install --upgrade pip
pip install -r requirements.txt

Модели Vosk и Silero, а также FFmpeg
Vosk - оффлайн-распознавание аудио и получение из него текста. Модели доступны на сайте проекта. Скачайте модель, разархивируйте и поместите папку model с файлами в папку models/vosk.

vosk-model-ru-0.22 - 1.5 Гб - лучше распознает, но дольше и весит много.
vosk-model-small-ru-0.22 - 45 Мб - хуже распознает, но быстрее и весит мало.
Silero - оффлайн-создание аудио сообщения из текста. В классе TTS проекта указана модель Silero v3.1 ru - 60 Мб, которая сама скачается при первом запуске проекта. Остальные модели можно скачать тут или на сайте проекта.

FFmpeg - набор open-source библиотек для конвертирования аудио- и видео в различных форматах. Скачайте набор exe файлов с сайта проекта и поместите файл ffmpeg.exe в папки models/vosk и models/silero.

Автор
Валентин