let myAnswers = [];
let realAnswers = [];
let currentTask = 0;

let urlParams = new URLSearchParams(window.location.search);
let tasks = parseInt(urlParams.get("num"), 10);
let size = parseInt(urlParams.get("size"), 10);

function whatToDo(event) {
  if (currentTask < tasks) {
    generateNewTask(event);
    getNewAnswer();
    updateStats(currentTask, tasks);
  } else if (currentTask === tasks) {
    getNewAnswer();
    checkAnswers();
  }
  currentTask += 1;
}

function updateStats(currentTask, tasks) {
  document.getElementById("stats").textContent = currentTask + 1 + "/" + tasks;
}

function checkAnswers() {
  var result = 0;
  for (let i = 0; i < myAnswers.length; i++) {
    if (myAnswers[i] === realAnswers[i]) {
      result += 1;
    }
  }
  window.location.assign("/resultPage" + "?num=" + tasks + "&result=" + result);
}

function getNewAnswer() {
  var answerInput = document.getElementById("answer");
  var newAnswer = answerInput.value;
  if (newAnswer.trim() !== "") {
    myAnswers.push(newAnswer);
  }
  answerInput.value = "";
}

function generateNewTask(event) {
  event.preventDefault();

  const xhr = new XMLHttpRequest();

  xhr.open("POST", "/new_task", true);

  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      let responseArray = JSON.parse(xhr.responseText);
      if (Array.isArray(responseArray) && responseArray.length >= 1) {
        var firstValue = responseArray[0];
        var secondValue = Number(responseArray[1]);
        document.getElementById("task").textContent = firstValue;
        realAnswers.push(secondValue);
      }
    }
  };

  const data = "size=" + encodeURIComponent(size);
  xhr.send(data);
}

document.addEventListener("DOMContentLoaded", whatToDo);

document.getElementById("form").addEventListener("submit", generateNewTask);

document.getElementById("answer").addEventListener("keydown", function (event) {
  if (event.key === "Enter") {
    whatToDo(event);
  }
});
