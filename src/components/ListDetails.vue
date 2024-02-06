<template>
    <v-card>
        <v-card-title>
            <v-container>
                <v-row>
                    {{ formatDate(list.event_date) }}
                </v-row>
            </v-container>
        </v-card-title>
        <v-card-text>
            <v-data-table :headers="headers" :items="list.players" :sort-by="sortBy" @click:row="openRating">
                <template #item.rated="{ item }">
                    <v-icon :icon="item.rated ? 'mdi-check' : 'mdi-close'"></v-icon>
                </template>
            </v-data-table>
            <rate :item="selectedItem" :votingOpen="isAfter(list.voting_until, new Date())" :show-dialog="dialog"
                @update:showDialog="dialog = $event" />
        </v-card-text>
    </v-card>
</template>
<script setup>
import { onMounted } from 'vue';
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router'
import { formatRelative, isAfter } from 'date-fns'
import Rate from './Rate.vue';

const route = useRoute()

const headers = [
    { value: 'name', title: 'Nome' },
    { value: 'rating', title: 'Nota' },
    { value: 'rated', title: 'Avaliado' }
]

const sortBy = [
    { key: 'rated', order: 'asc' }
]

const list = ref({})

const dialog = ref(false)
const selectedItem = ref({})

const getListDetails = () => {
    list.value = {
        id: 3,
        event_date: new Date('2024-02-02 20:30:00'),
        voting_until: new Date('2024-02-08 23:59:59'),
        checkin_from: new Date('2024-02-02 08:00:00'),
        checkin_until: new Date('2024-02-02 19:30:00'),
        teams_drawn: true,
        players: [
            {
                "id": 1,
                "name": "Lucas",
                "rating": 4.12,
                "rated": true
            },
            {
                "id": 2,
                "name": "Miguel",
                "rating": 3.59,
                "rated": false
            },
            {
                "id": 3,
                "name": "Gabriel",
                "rating": 4.73,
                "rated": true
            },
            {
                "id": 4,
                "name": "Arthur",
                "rating": 2.68,
                "rated": false
            },
            {
                "id": 5,
                "name": "Pedro",
                "rating": 3.45,
                "rated": true
            },
            {
                "id": 6,
                "name": "Mateus",
                "rating": 4.56,
                "rated": false
            },
            {
                "id": 7,
                "name": "Rafael",
                "rating": 3.92,
                "rated": true
            },
            {
                "id": 8,
                "name": "Felipe",
                "rating": 2.87,
                "rated": false
            },
            {
                "id": 9,
                "name": "Gustavo",
                "rating": 3.14,
                "rated": true
            },
            {
                "id": 10,
                "name": "Guilherme",
                "rating": 4.22,
                "rated": false
            },
            {
                "id": 11,
                "name": "Leonardo",
                "rating": 3.88,
                "rated": true
            },
            {
                "id": 12,
                "name": "Eduardo",
                "rating": 2.95,
                "rated": false
            },
            {
                "id": 13,
                "name": "Murilo",
                "rating": 4.01,
                "rated": true
            },
            {
                "id": 14,
                "name": "Henrique",
                "rating": 3.67,
                "rated": false
            },
            {
                "id": 15,
                "name": "Bruno",
                "rating": 2.77,
                "rated": true
            }
        ]
    }
}

const formatDate = (date) => formatRelative(date, new Date())

const openRating = (ev, data) => {
    dialog.value = true
    selectedItem.value = data.item
}

onMounted(() => {
    getListDetails()
})
</script>
