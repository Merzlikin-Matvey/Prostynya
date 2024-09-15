import { ref } from 'vue';

export const selectedOption = ref('Система оценивания');

export const toggleDropdown = () => {
    const dropdown = document.querySelector('.select-items');
    dropdown.classList.toggle('select-hide');
    dropdown.classList.toggle('select-show');
};

export const selectOption = (option: string) => {
    selectedOption.value = option;
    toggleDropdown();
};