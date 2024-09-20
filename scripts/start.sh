#!/bin/bash

./check_requirements.sh

if [ ! -d "../autovenv" ]; then
  echo "Папка autovenv не найдена. Создаем виртуальное окружение..."
  virtualenv ../autovenv
  if [ $? -ne 0 ]; then
    echo "Ошибка при создании виртуального окружения. Запустите скрипт update.sh для обновления."
    exit 1
  fi
fi

cd ..
source autovenv/bin/activate

python3.12 -m server &
SERVER_PID=$!
sleep 5

if ! ps -p $SERVER_PID > /dev/null; then
  echo "Ошибка при запуске сервера."
  exit 1
fi

pkill -f 'python3.12 -m server'

echo "Запуск сервера в фоновом режиме..."

nohup python3.12 -m server > server.log 2>&1 &
if [ $? -ne 0 ]; then
  echo "Ошибка при запуске сервера через nohup. Запустите скрипт update.sh для обновления."
  exit 1
fi

echo "Все хорошо. Сервер запущен в фоновом режиме. Логи можно найти в server.log"