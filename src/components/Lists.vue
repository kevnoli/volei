<template>
    <v-card title="Listas">
        <v-card-text>
            <v-data-table v-model:sort-by="sortBy" :headers="headers" :items="lists" @click:row.prevent="openDetails">
                <template #item.date="{ item }">
                    {{ formatDate(item.date) }}
                </template>
                <template #item.voting="{ item }">
                    <v-icon>{{ item.voting ? 'mdi-vote' : 'mdi-lock' }}</v-icon>
                </template>
                <template #loading>
                    <v-skeleton-loader type="table-row@10"></v-skeleton-loader>
                </template>
            </v-data-table>
        </v-card-text>
    </v-card>
</template>
<script setup>
import { onMounted } from 'vue';
import { ref } from 'vue';
import { formatRelative } from 'date-fns'
import { ptBR } from 'date-fns/locale'
import { useRouter } from 'vue-router'

const router = useRouter()

const headers = [
    { key: 'date', title: 'Data' },
    { key: 'voting', title: 'Votação' },
]

const sortBy = [{ key: 'date', order: 'desc' }]

const lists = ref([])

const getLists = () => {
    lists.value = [
        {
            id: 1,
            date: new Date('2024-01-19 20:30'),
            voting: false
        },
        {
            id: 2,
            date: new Date('2024-01-26 20:30'),
            voting: false
        },
        {
            id: 3,
            date: new Date('2024-02-02 20:30'),
            voting: true
        },
    ]
}

const formatDate = (date) => formatRelative(date, new Date())

const openDetails = (ev, data) => {
    return router.push(
        {
            name: 'list',
            params: {
                id: data.item.id
            }
        }
    );
}

onMounted(() => {
    getLists()
})
</script>