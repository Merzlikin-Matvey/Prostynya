#!/bin/bash


git pull

if [ ! -d "../autovenv" ]; then
  echo "Папка autovenv не найдена. Создаем виртуальное окружение..."
  virtualenv ../autovenv
  if [ $? -ne 0 ]; then
    echo "Ошибка при создании виртуального окружения."
    exit 1
  fi
fi

cd ..
source autovenv/bin/activate

python3.12 -m pip install -r requirements.txt
npm run build
