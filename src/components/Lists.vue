<template>
    <v-card title="Listas">
        <v-card-text>
            <v-data-table v-model:sort-by="sortBy" :headers="headers" :items="lists" @click:row.prevent="openDetails">
                <template #item.event_date="{ item }">
                    {{ formatDate(item.event_date) }}
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
import { onMounted } from 'vue';
import { ref } from 'vue';
import { formatRelative, isAfter } from 'date-fns'
import { useRouter } from 'vue-router'

const router = useRouter()

const headers = [
    { key: 'event_date', title: 'Data' },
    { key: 'status', title: 'Status' },
]

const sortBy = [{ key: 'event_date', order: 'desc' }]

const lists = ref([])

function getLists() {
    lists.value = [
        {
            id: 1,
            event_date: new Date('2024-01-19 20:30:00'),
            voting_until: new Date('2024-01-25 23:59:59'),
            checkin_from: new Date('2024-01-19 08:00:00'),
            checkin_until: new Date('2024-01-19 19:30:00'),
            teams_drawn: true
        },
        {
            id: 2,
            event_date: new Date('2024-01-26 20:30:00'),
            voting_until: new Date('2024-02-01 23:59:59'),
            checkin_from: new Date('2024-01-26 08:00:00'),
            checkin_until: new Date('2024-01-26 19:30:00'),
            teams_drawn: true
        },
        {
            id: 3,
            event_date: new Date('2024-02-02 20:30:00'),
            voting_until: new Date('2024-02-08 23:59:59'),
            checkin_from: new Date('2024-02-02 08:00:00'),
            checkin_until: new Date('2024-02-02 19:30:00'),
            teams_drawn: true
        },
        {
            id: 4,
            event_date: new Date('2024-02-09 20:30:00'),
            voting_until: new Date('2024-02-15 23:59:59'),
            checkin_from: new Date('2024-02-09 08:00:00'),
            checkin_until: new Date('2024-02-09 19:30:00'),
            teams_drawn: false
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

const getStatus = (item) => {
    const now = new Date();

    // Event Finished
    if (isAfter(now, item.event_date)) {
        // Rating still open
        if (isAfter(item.voting_until, now)) {
            return {
                icon: 'mdi-message-draw',
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
    getLists()
})
</script>