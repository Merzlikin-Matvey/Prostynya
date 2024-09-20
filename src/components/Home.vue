<script setup lang="ts">
import '../assets/styles.css';
import { useRouter } from 'vue-router';

const router = useRouter();

const navigateToTrigonometry = () => {
  router.push('/trigonometry');
};
</script>

<template>
  <div class="footer">
    <p class="footer-text">Made by Matvey Merzlikin</p>
    <a href="https://github.com/Merzlikin-Matvey/Prostynya" target="_blank">
      <img src="../res/github.png" alt="GitHub" class="github-logo"/>
    </a>
  </div>
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
.footer {
  position: absolute;
  left: 50%;
  bottom: 20px;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}

.footer-text {
  color: rgba(255, 255, 255, 0.65);
  transition: color 0.5s ease;
}

.footer-text:hover {
  color: white;
}

.github-logo {
  width: auto;
  height: 5vh;
  filter: brightness(0) invert(1);
  margin-top: -15px;
}

.type-selector {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  height: 80vh;
  width: 100%;
  gap: 20px;
}

.tile {
  width: 30vw;
  height: 30vw;
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
  margin: 2vw;
}

.tile:hover {
  background-color: var(--secondary-color);
}

.tile-image {
  width: 20vw;
  height: 20vw;
  filter: brightness(0) invert(1);
  border-radius: 40px;
}

@media screen and (max-width: 768px) {
  .tile {
    width: 45vw;
    height: 45vw;
  }
  .tile-image {
    width: 35vw;
    height: 35vw;
  }
}

@media screen and (max-width: 480px) {
  .type-selector {
    flex-direction: column;
  }
  .tile {
    width: 60vw;
    height: 60vw;
  }
  .tile-image {
    width: 42vw;
    height: 42vw;
  }
}
</style>