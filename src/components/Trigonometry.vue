<template>
  <RouterView />
  <h1 class="title">Тригонометрия</h1>
  <div class="form">
    <div class="input">
      <input type="text" class="input__field" placeholder=" " id="title-input" @input="resetDownloadState" />
      <label for="text-input" class="input__label">Заголовок</label>
    </div>
    <div class="input mark">
      <select class="input__field" id="mark-system-input" required @change="resetDownloadState">
        <option value="" disabled selected></option>
        <option value="mark-system-1">Одна ошибка - балл долой</option>
        <option value="mark-system-2">Одна ошибка - 2</option>
        <option value="mark-system-3">Всем 2!</option>
      </select>
      <label for="select-input" class="input__label">Система оценивания</label>
    </div>

    <h1 class="num_tasks_label">Количество задач</h1>

    <div class="num_tasks_input_div">
      <h2 class="task_text" id="calculations_text">Табличные углы</h2>
      <div class="num_task_wrapper">
        <input class="num_task_input" id="calculations">
      </div>
    </div>

    <div class="num_tasks_input_div">
      <h2 class="task_text" id="relationships_text">Формулы приведения</h2>
      <div class="num_task_wrapper">
        <input class="num_task_input" id="relationships">
      </div>
    </div>

    <div class="num_tasks_input_div">
      <h2 class="task_text" id="formulas_text">Формулы</h2>
      <div class="num_task_wrapper">
        <input class="num_task_input" id="formulas">
      </div>
    </div>

    <div class="num_tasks_input_div">
      <h2 class="task_text">Арк функции</h2>
      <div class="num_task_wrapper">
        <input class="num_task_input">
      </div>
    </div>

    <h1 class="level">Сложность</h1>
    <div class="skull-rating">
      <span class="skull" @click="setRatingAndReset(1)" @mouseover="handleMouseOver(0)" @mouseout="handleMouseOut">&#128128;</span>
      <span class="skull" @click="setRatingAndReset(2)" @mouseover="handleMouseOver(1)" @mouseout="handleMouseOut">&#128128;</span>
      <span class="skull" @click="setRatingAndReset(3)" @mouseover="handleMouseOver(2)" @mouseout="handleMouseOut">&#128128;</span>
      <span class="skull" @click="setRatingAndReset(4)" @mouseover="handleMouseOver(3)" @mouseout="handleMouseOut">&#128128;</span>
      <span class="skull" @click="setRatingAndReset(5)" @mouseover="handleMouseOver(4)" @mouseout="handleMouseOut">&#128128;</span>
    </div>
    <h1 class="level_name"></h1>
    <button class="button" id="generate" @click="sendForm()">Сгенерировать</button>
  </div>
  <GeneratingAnimation :isGenerating="isGenerating" />
  <div v-if="id" class="download-buttons">
    <button class="button" @click="downloadFile(id)" id="download_tasks">Скачать задания</button>
    <button class="button" @click="downloadFile(id + '_solutions')" id="download_solutions">Скачать ответы</button>
  </div>
</template>

<script setup lang="ts">
import '../assets/styles.css';
import '../assets/form.css';
import '../assets/button.css';
import { watch, onMounted, ref } from 'vue';
import { updateStars, rating, handleMouseOut, handleMouseOver, setRating } from "../skulls";
import GeneratingAnimation from './GeneratingAnimation.vue';

handleMouseOut();
handleMouseOver(0);

watch(rating, (newRating) => {
  updateStars(newRating);
});

onMounted(() => {
  updateStars(rating.value);
});

const id = ref<string | null>(null);
const isGenerating = ref(false);

function sendForm() {
  resetDownloadState();
  isGenerating.value = true;
  let title = (document.getElementById('title-input') as HTMLInputElement).value;
  let grading_system = (document.getElementById('mark-system-input') as HTMLSelectElement).value;
  let num_calculations = (document.getElementById('calculations') as HTMLInputElement).value;
  let num_relationships = (document.getElementById('relationships') as HTMLInputElement).value;
  let num_formulas = (document.getElementById('formulas') as HTMLInputElement).value;
  let difficulty = rating.value;

  let grading_system_name;
  if (grading_system == 'mark-system-1') {
    grading_system_name = 'Одна ошибка - балл долой';
  }
  else if (grading_system == 'mark-system-2') {
    grading_system_name = 'Одна ошибка - 2';
  }
  else {
    grading_system_name = 'Всем 2!';
  }

  const data = {
    title,
    grading_system_name,
    num_calculations: parseInt(num_calculations),
    num_relationships: parseInt(num_relationships),
    num_formulas: parseInt(num_formulas),
    difficulty
  };

  fetch('/generate_trigonometry', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
      .then(response => response.json())
      .then(result => {
        id.value = result.id;
        isGenerating.value = false;
        console.log('Generated ID:', id.value);
      })
      .catch(error => {
        isGenerating.value = false;
        console.error('Error:', error);
      });
}

function downloadFile(fileId: string) {
  window.location.href = `/download/${fileId}`;
}

function resetDownloadState() {
  id.value = null;
}

function setRatingAndReset(value: number) {
  setRating(value);
  resetDownloadState();
}
</script>

<style>
html, body {
  width: 100%;
  height: 100%;
  margin: 0;
  background-color: var(--background-color);
}

.title {
  font-size: 3rem;
  text-align: center;
  margin-top: 50px;
}

.download-buttons {
  text-align: center;
  margin-top: 20px;
}

.button {
  margin: 5px;
}

#download_tasks {
  width: 20vw;
  margin-right: 1.5vw;
}

#download_solutions {
  width: 20vw;
  margin-left: 1.5vw;
}

@media screen and (orientation: portrait) {
  .title {
    font-size: 2.2rem;
  }
  .form {
    width: 90vw;
  }
  .skull {
    font-size: 2.2rem;
  }
  .skull-rating {
    margin-top: 6vh;
  }

  #download_tasks {
    width: 80vw;
    margin-right: 1.5vw;
  }

  #download_solutions {
    width: 80vw;
    margin-left: 1.5vw;
  }

  .input__label {
    margin-left: 2vw;
  }

  .num_tasks_label {
    font-size: 1.5rem;
    white-space: nowrap;
  }
}



</style>