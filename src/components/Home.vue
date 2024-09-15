<script setup lang="ts">
import '../assets/styles.css';
import { useRouter } from 'vue-router';

const router = useRouter();

const navigateToTrigonometry = () => {
  router.push('/trigonometry');
};
</script>

<template>
  <div class="type-selector">
    <button class="tile" @click="navigateToTrigonometry">
      <img src="../res/trigonometry.png" alt="Trigonometry" class="tile-image" id="trigonometry"/>
    </button>
    <button class="tile">
      <img src="../res/calculator.png" alt="Calculations" class="tile-image" id="calculations"/>
    </button>
  </div>
  <RouterView />
</template>


<style scoped>
.type-selector {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 100%;
}

.tile {
  width: 50vh;
  height: 50vh;
  margin: 0 50px;
  background-color: var(--primary-color);
  color: var(--primary-text-color);
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  transition: background-color 0.5s ease;
  border-radius: 40px;
  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
  display: flex;
  justify-content: center;
  align-items: center;
}

.tile:hover {
  background-color: var(--secondary-color);
}

.tile-image {
  width: 50%;
  height: 50%;
  filter: brightness(0) invert(1);
  border-radius: 40px;
}
</style>