import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './components/HomePage.vue';
import TrigonometryPage from './components/TrigonometryPage.vue';

const routes = [
    {
        path: '/',
        name: 'Home',
        component: HomePage,
    },
    {
        path: '/trigonometry',
        name: 'Trigonometry',
        component: TrigonometryPage,
    },
];

const router = createRouter({
    history: createWebHistory(import.meta.env.VITE_BASE_URL),
    routes,
});

export default router;