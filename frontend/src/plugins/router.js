import { createRouter, createWebHistory } from "vue-router";

import DefaultLayout from '@/layouts/default/Default.vue'

import Login from '@/components/Login.vue'
import SportsEvents from '@/components/SportsEvents.vue'
import SportsEvent from '@/components/SportsEventDetails.vue'

const routes = [
    {
        name: 'login',
        path: '/login',
        component: Login
    },
    {
        path: '/',
        component: DefaultLayout,
        children: [
            {
                name: 'events',
                path: 'events',
                component: SportsEvents
            },
            {
                name: 'event',
                path: 'event/:id',
                component: SportsEvent
            }
        ]
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router