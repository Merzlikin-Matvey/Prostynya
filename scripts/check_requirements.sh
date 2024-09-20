#!/bin/bash

if ! command -v python3.12 &> /dev/null; then
  echo "Python 3.12 не установлен. Устанавливаем Python 3.12..."
  sudo apt update
  sudo add-apt-repository ppa:deadsnakes/ppa -y
  sudo apt install python3.12-{tk,dev,dbg,venv,gdbm,distutils}
  if [ $? -ne 0 ]; then
    echo "Не удалось установить Python 3.12. Пожалуйста, установите его вручную"
    exit 1
  fi
fi

if ! command -v virtualenv &> /dev/null; then
  echo "virtualenv не установлен. Устанавливаем virtualenv..."
  python3.12 -m pip install virtualenv
  if [ $? -ne 0 ]; then
    echo "Не удалось установить virtualenv. Пожалуйста, установите его вручную"
    exit 1
  fi
fi