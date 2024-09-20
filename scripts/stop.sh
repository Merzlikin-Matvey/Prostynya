#!/bin/bash

PID=$(ps aux | grep '[p]ython3.12 -m server' | awk '{print $2}')

if [ -z "$PID" ]; then
  echo "Сервер не запущен."
else
  kill $PID
  echo "Сервер остановлен."
fi