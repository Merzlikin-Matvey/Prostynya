import {onMounted, ref, watch} from "vue";

const rating = ref(0);

const setRating = (value: number) => {
    rating.value = value;
};

const updateStars = (newRating: number) => {
    const stars = document.querySelectorAll('.skull');
    stars.forEach((skull, index) => {
        if (index < newRating) {
            skull.classList.add('selected');
        } else {
            skull.classList.remove('selected');
        }
    });
};

const handleMouseOver = (index: number) => {
    const stars = document.querySelectorAll('.skull');
    stars.forEach((skull, i) => {
        if (i <= index) {
            skull.classList.add('hovered');
        } else {
            skull.classList.remove('hovered');
        }
    });
};

const handleMouseOut = () => {
    const stars = document.querySelectorAll('.skull');
    stars.forEach((skull) => {
        skull.classList.remove('hovered');
    });
    updateStars(rating.value);
};

export { updateStars, rating, handleMouseOut, handleMouseOver, setRating }