<template>
    <v-container>
        <v-row justify="center">
            <v-col cols="12" sm="8" md="6">
                <v-card>
                    <v-card-title>
                        <v-container>
                            <v-row>
                                <v-col>
                                    {{ sportsEventName }}
                                </v-col>
                            </v-row>
                        </v-container>
                    </v-card-title>
                    <v-card-text>
                        <v-tabs v-model="tab">
                            <v-tab value="players">Jogadores</v-tab>
                            <v-tab value="teams">Times</v-tab>
                        </v-tabs>
                        <v-window v-model="tab">
                            <v-window-item value="players">
                                <v-data-table :headers="playersHeaders" :items="sportsEvent.players" :sort-by="sortBy"
                                    @click:row="openRating">
                                    <template #item.rated="{ item }">
                                        <v-icon :icon="item.rated ? 'mdi-check' : 'mdi-close'"></v-icon>
                                    </template>
                                </v-data-table>
                                <rate :item="selectedItem" :votingOpen="isAfter(sportsEvent.voting_until, new Date())"
                                    :show-dialog="dialog" @update:showDialog="dialog = $event" />
                            </v-window-item>
                            <v-window-item value="teams">
                                <v-list>
                                    <div v-for="team in teams">
                                        <v-list-subheader
                                            :title="`Time ${team.players[0].name} (média ${teamRating(team.players)})`" />
                                        <v-list-item v-for="player in team.players" :title="player.name" />
                                        <v-divider></v-divider>
                                    </div>
                                </v-list>
                            </v-window-item>
                        </v-window>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
        <div class="text-end pointer-events-none" style="position: fixed; bottom: 0; right: 0; margin: 16px;">
            <v-fab-transition>
                <v-btn
                    v-if="isWithinInterval(new Date(), { start: sportsEvent.checkin_from, end: sportsEvent.checkin_until })"
                    color="primary" elevation="8" icon="mdi-check" size="large" />
            </v-fab-transition>
        </div>
        <v-layout-item class="text-end pointer-events-none" model-value position="bottom" size="30" />
    </v-container>
</template>
<script setup>
import { onMounted } from 'vue';
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router'
import { formatRelative, isAfter, isWithinInterval, parseISO } from 'date-fns'
import Rate from './Rate.vue';
import { computed } from 'vue';

const route = useRoute()

const playersHeaders = [
    { value: 'name', title: 'Nome' },
    { value: 'rating', title: 'Nota' },
    { value: 'rated', title: 'Avaliado' }
]

const sortBy = [
    { key: 'rated', order: 'asc' }
]

const sportsEvent = ref({})
const teams = ref([])

const dialog = ref(false)
const selectedItem = ref({})

const tab = ref(null)

const getSportsEventDetails = () => {
    sportsEvent.value = {
        id: 3,
        event_date: '2024-02-02 20:30:00.000',
        voting_until: '2024-02-08 23:59:59.999',
        checkin_from: '2024-02-02 08:00:00.000',
        checkin_until: '2024-02-08 19:30:00.000',
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
    teams.value = [
        {
            'id': 0, 'players': [
                { 'id': 12, 'name': 'Eduardo', 'rating': 2.95 },
                { 'id': 6, 'name': 'Mateus', 'rating': 4.56 },
                { 'id': 1, 'name': 'Lucas', 'rating': 4.12 },
                { 'id': 14, 'name': 'Henrique', 'rating': 3.67 },
                { 'id': 5, 'name': 'Pedro', 'rating': 3.45 },
            ]
        },
        {
            'id': 1, 'players': [
                { 'id': 8, 'name': 'Felipe', 'rating': 2.87 },
                { 'id': 3, 'name': 'Gabriel', 'rating': 4.73 },
                { 'id': 13, 'name': 'Murilo', 'rating': 4.01 },
                { 'id': 11, 'name': 'Leonardo', 'rating': 3.88 },
                { 'id': 9, 'name': 'Gustavo', 'rating': 3.14 },
            ]
        },
        {
            'id': 2, 'players': [
                { 'id': 15, 'name': 'Bruno', 'rating': 2.77 },
                { 'id': 4, 'name': 'Arthur', 'rating': 2.68 },
                { 'id': 10, 'name': 'Guilherme', 'rating': 4.22 },
                { 'id': 7, 'name': 'Rafael', 'rating': 3.92 },
                { 'id': 2, 'name': 'Miguel', 'rating': 3.59 },
            ]
        }
    ]
}

const teamRating = (players) => {
    return (players.reduce((s, x) => s + x['rating'], 0) / players.length).toFixed(2)
}

const sportsEventName = computed(() => {
    if (sportsEvent.value.event_date && !isNaN(parseISO(sportsEvent.value.event_date).getTime())) {
        return formatRelative(parseISO(sportsEvent.value.event_date), new Date());
    }
    return '';
})

const openRating = (ev, data) => {
    dialog.value = true
    selectedItem.value = data.item
}

onMounted(() => {
    getSportsEventDetails()
})
</script>
