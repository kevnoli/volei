<template>
    <v-btn :icon="!!notifications ? 'mdi-message-badge' : 'mdi-message'">
        <v-menu activator="parent">
            <v-list>
                <v-list-item v-for="item in notifications"> {{ item.message }} </v-list-item>
            </v-list>
        </v-menu>
    </v-btn>
</template>
<script setup>
const notifications = [
    {
        message: 'Votação aberta para o último Vôlei de sexta'
    }
]
</script>