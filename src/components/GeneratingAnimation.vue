<template>
  <div v-if="isGenerating" :class="['generating', { fadeOut: !isGenerating }]" ref="generatingText">
    Генерируется{{ dots }}
  </div>
</template>

<script setup lang="ts">
import { ref, watch, toRef, nextTick } from 'vue';

const props = defineProps<{ isGenerating: boolean }>();
const isGeneratingRef = toRef(props, 'isGenerating');
const dots = ref('');
const generatingText = ref<HTMLElement | null>(null);

let interval: number;
watch(isGeneratingRef, (newVal) => {
  if (newVal) {
    interval = setInterval(() => {
      dots.value = dots.value.length < 3 ? dots.value + '.' : '';
    }, 500);
    nextTick(() => {
      if (generatingText.value) {
        generatingText.value.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    });
  } else {
    clearInterval(interval);
    dots.value = '';
  }
});
</script>

<style scoped>
.generating {
  text-align: center;
  font-size: 1.5rem;
  margin-top: 20px;
  opacity: 0;
  animation: fadeIn 0.3s forwards;
}


@keyframes fadeIn {
  to {
    opacity: 1;
  }
}

@keyframes fadeOut {
  to {
    opacity: 0;
  }
}
</style>