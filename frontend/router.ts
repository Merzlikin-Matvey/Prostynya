import { createRouter, createWebHistory } from 'vue-router';
import Home from './components/Home.vue';
import Trigonometry from './components/Trigonometry.vue';

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
    },
    {
        path: '/trigonometry',
        name: 'Trigonometry',
        component: Trigonometry,
    },
];

const router = createRouter({
    history: createWebHistory(import.meta.env.VITE_BASE_URL),
    routes,
});

export default router;