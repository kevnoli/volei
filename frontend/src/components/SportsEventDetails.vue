<template>
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
                        <template #item.name="{ item }">
                            {{ item.first_name }} {{ item.last_name }}
                        </template>
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
                                :title="`Time ${team.players[0].first_name} ${team.players[0].last_name} (média ${teamRating(team.players)})`" />
                            <v-list-item v-for="player in team.players">
                                <v-list-item-title>{{ player.first_name }} {{ player.last_name }}</v-list-item-title>
                                <v-list-item-subtitle>{{ player.overall_rating }}</v-list-item-subtitle>
                            </v-list-item>
                            <v-divider></v-divider>
                        </div>
                    </v-list>
                </v-window-item>
            </v-window>
        </v-card-text>
        <div class="text-end pointer-events-none" style="position: fixed; bottom: 0; right: 0; margin: 16px;">
            <v-fab-transition>
                <v-btn
                    v-if="isWithinInterval(new Date(), { start: sportsEvent.checkin_from, end: sportsEvent.checkin_until })"
                    color="primary" elevation="8" icon="mdi-check" size="large" />
            </v-fab-transition>
        </div>
        <v-layout-item class="text-end pointer-events-none" model-value position="bottom" size="30" />
    </v-card>
</template>
<script setup>
import { onMounted, ref, computed, inject } from 'vue';
import { formatRelative, isAfter, isWithinInterval, parseISO } from 'date-fns'
import Rate from './Rate.vue';
import { useRoute } from 'vue-router';

const axios = inject("axios")

const route = useRoute()

const playersHeaders = [
    { value: 'name', title: 'Nome' },
    { value: 'rated', title: 'Avaliado', align: 'center' },
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
    axios.get(`/events/${route.params.id}`)
        .then(({ data }) => {
            sportsEvent.value = data
        })
        .then(() => {
            axios.get(`/events/${route.params.id}/teams`)
                .then(({ data }) => {
                    teams.value = data
                })
        })
}

const teamRating = (players) => {
    if (players.length === 0) return 0
    return (players.reduce((s, x) => parseFloat(s) + parseFloat(x['overall_rating']), 0) / players.length).toFixed(2)
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
