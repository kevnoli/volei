import { createRouter, createWebHistory } from "vue-router";

import DefaultLayout from '@/layouts/default/Default.vue'

import Login from '@/components/Login.vue'
import Lists from '@/components/Lists.vue'
import List from '@/components/ListDetails.vue'

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
                name: 'lists',
                path: 'lists',
                component: Lists
            },
            {
                name: 'list',
                path: 'list/:id',
                component: List
            }
        ]
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router