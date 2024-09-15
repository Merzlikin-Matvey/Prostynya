<template>
  <RouterView />
  <h1 class="title">Тригонометрия</h1>
  <div class="form">
    <div class="input">
      <input type="text" class="input__field" placeholder=" " id="text-input" />
      <label for="text-input" class="input__label">Заголовок</label>
    </div>
    <div class="input-group">
      <div class="input half-width">
        <select class="input__field" id="select-input" required>
          <option value="" disabled selected></option>
          <option value="option1">Одна ошибка - балл долой</option>
          <option value="option2">Одна ошибка - 2</option>
          <option value="option3">Всем 2!</option>
        </select>
        <label for="select-input" class="input__label">Система оценивания</label>
      </div>
      <div class="input half-width">
        <input type="number" class="input__field" placeholder=" " id="number-input" />
        <label for="number-input" class="input__label">Число задач</label>
      </div>
    </div>
    <div class="star-rating">
      <span class="star" @click="setRating(1)" @mouseover="handleMouseOver(0)" @mouseout="handleMouseOut">&#9733;</span>
      <span class="star" @click="setRating(2)" @mouseover="handleMouseOver(1)" @mouseout="handleMouseOut">&#9733;</span>
      <span class="star" @click="setRating(3)" @mouseover="handleMouseOver(2)" @mouseout="handleMouseOut">&#9733;</span>
      <span class="star" @click="setRating(4)" @mouseover="handleMouseOver(3)" @mouseout="handleMouseOut">&#9733;</span>
      <span class="star" @click="setRating(5)" @mouseover="handleMouseOver(4)" @mouseout="handleMouseOut">&#9733;</span>
    </div>
    <button>Bebra</button>
  </div>
</template>

<script setup lang="ts">
import '../assets/styles.css';
import '../assets/form.css';

import { ref, watch, onMounted } from 'vue';

const rating = ref(0);

const setRating = (value: number) => {
  rating.value = value;
};

const updateStars = (newRating: number) => {
  const stars = document.querySelectorAll('.star');
  stars.forEach((star, index) => {
    if (index < newRating) {
      star.classList.add('selected');
    } else {
      star.classList.remove('selected');
    }
  });
};

const handleMouseOver = (index: number) => {
  const stars = document.querySelectorAll('.star');
  stars.forEach((star, i) => {
    if (i <= index) {
      star.classList.add('hovered');
    } else {
      star.classList.remove('hovered');
    }
  });
};

const handleMouseOut = () => {
  const stars = document.querySelectorAll('.star');
  stars.forEach((star) => {
    star.classList.remove('hovered');
  });
  updateStars(rating.value);
};

watch(rating, (newRating) => {
  updateStars(newRating);
});

onMounted(() => {
  updateStars(rating.value);
});
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