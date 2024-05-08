<template>
    <v-card title="Eventos">
        <v-card-text>
            <v-data-table v-model:sort-by="sortBy" :headers="headers" :items="sportsEvents"
                @click:row.prevent="openDetails">
                <template #item.start_date="{ item }">
                    {{ formatDate(item.start_date) }}
                </template>
                <template #item.status="{ item }">
                    <v-tooltip :text="getStatus(item).description">
                        <template #activator="{ props }">
                            <v-icon v-bind="props">{{ getStatus(item)['icon'] }}</v-icon>
                        </template>
                    </v-tooltip>
                </template>
                <template #loading>
                    <v-skeleton-loader type="table-row@10"></v-skeleton-loader>
                </template>
            </v-data-table>
        </v-card-text>
    </v-card>
</template>
<script setup>
import { inject, onMounted } from 'vue';
import { ref } from 'vue';
import { formatRelative, isAfter, parseISO } from 'date-fns'
import { useRouter } from 'vue-router'

const router = useRouter()
const axios = inject("axios")

const headers = [
    { key: 'start_date', title: 'Data' },
    { key: 'status', title: 'Status' },
]

const sortBy = [{ key: 'event_date', order: 'desc' }]

const sportsEvents = ref([])

function getSportsEvents() {
    axios
        .get("events")
        .then((resp) => {
            sportsEvents.value = resp.data
        })
}

const formatDate = (date) => {
    if (!date) return null
    return formatRelative(parseISO(date), new Date())
}

const openDetails = (ev, data) => {
    return router.push(
        {
            name: 'event',
            params: {
                id: data.item.id
            }
        }
    );
}

const getStatus = (item) => {
    const now = new Date();

    // Event Finished
    if (isAfter(now, item.event_date)) {
        // Rating still open
        if (isAfter(item.voting_until, now)) {
            return {
                icon: 'mdi-vote',
                description: 'Avaliações abertas'
            };
        }
        // Rating closed
        else {
            return {
                icon: 'mdi-lock',
                description: 'Avaliações fechadas'
            };
        }
    }
    // Event Open
    else {
        // Check-in hasn't started
        if (isAfter(item.checkin_from, now)) {
            return {
                icon: 'mdi-timer-sand',
                description: 'O check-in ainda não começou'
            };
        }
        // Check-in started but not finished
        else if (isAfter(item.checkin_until, now)) {
            return {
                icon: 'mdi-check-circle',
                description: 'O check-in começou'
            };
        }
        // Check-in finished
        else {
            return {
                icon: 'mdi-calendar-check',
                description: 'O check-in já acabou'
            };
        }
    }
}

onMounted(() => {
    getSportsEvents()
})
</script>