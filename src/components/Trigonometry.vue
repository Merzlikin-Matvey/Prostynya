<template>
  <RouterView />
  <h1 class="title">Тригонометрия</h1>
  <div class="form">
    <div class="input">
      <input type="text" class="input__field" placeholder=" "  id="title-input"/>
      <label for="text-input" class="input__label" >Заголовок</label>
    </div>
    <div class="input-group">
      <div class="input half-width">
        <select class="input__field" id="mark-system-input" required>
          <option value="" disabled selected></option>
          <option value="mark-system-1">Одна ошибка - балл долой</option>
          <option value="mark-system-2">Одна ошибка - 2</option>
          <option value="mark-system-3">Всем 2!</option>
        </select>
        <label for="select-input" class="input__label">Система оценивания</label>
      </div>
      <div class="input half-width">
        <input type="number" class="input__field" placeholder=" " id="number-input" />
        <label for="number-input" class="input__label">Число задач</label>
      </div>
    </div>
    <h1 class="level">Сложность</h1>
    <div class="skull-rating">
      <span class="skull" @click="setRating(1)" @mouseover="handleMouseOver(0)" @mouseout="handleMouseOut">&#128128;</span>
      <span class="skull" @click="setRating(2)" @mouseover="handleMouseOver(1)" @mouseout="handleMouseOut">&#128128;</span>
      <span class="skull" @click="setRating(3)" @mouseover="handleMouseOver(2)" @mouseout="handleMouseOut">&#128128;</span>
      <span class="skull" @click="setRating(4)" @mouseover="handleMouseOver(3)" @mouseout="handleMouseOut">&#128128;</span>
      <span class="skull" @click="setRating(5)" @mouseover="handleMouseOver(4)" @mouseout="handleMouseOut">&#128128;</span>
    </div>
    <h1 class="level_name"></h1>
    <button class="button" id="generate" @click="sendForm()">Сгенерировать</button>
  </div>
</template>

<script setup lang="ts">
import '../assets/styles.css';
import '../assets/form.css';
import '../assets/button.css'

import { watch, onMounted } from 'vue';
import { updateStars, rating, handleMouseOut, handleMouseOver, setRating } from "@/skulls";

handleMouseOut();
handleMouseOver();

watch(rating, (newRating) => {
  updateStars(newRating);
});

onMounted(() => {
  updateStars(rating.value);
});


function sendForm() {
  let title = (document.getElementById('title-input') as HTMLInputElement).value;
  let mark_system = (document.getElementById('mark-system-input') as HTMLSelectElement).value;
  let task_number = (document.getElementById('number-input') as HTMLInputElement).value;
  let level = rating.value;

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
</style>