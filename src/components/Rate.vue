<template>
    <v-dialog v-model="dialog" persistent max-width="600px">
        <v-card :title="item.name">
            <v-card-text class="text-center">
                <v-container>
                    <v-row class="text-caption">1 = Precisa melhorar, 5 = Excelente</v-row>
                    <v-row v-for="rating in ratings" class="align-center ">
                        <v-col cols="3">{{ rating.name }}</v-col>
                        <v-col>
                            <v-rating v-model="playerRating[rating.id]" :readonly="!votingOpen" :size="35" hover :length="5"
                                half-increments active-color="primary" />
                        </v-col>
                        <v-col v-if="votingOpen" cols="1">
                            <v-row>
                                <v-icon icon="mdi-menu-up" @click="increaseRating(playerRating[rating.id])" />
                            </v-row>
                            <v-row>
                                <v-icon icon="mdi-menu-down" @click="decreaseRating(playerRating[rating.id])" />
                            </v-row>
                        </v-col>
                    </v-row>
                </v-container>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn v-if="votingOpen" color="error" text @click="closeDialog">Cancelar</v-btn>
                <v-btn color="primary" text @click="saveRating">{{ votingOpen ? 'Salvar' : 'Fechar' }}</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>
  
<script setup>
import { ref, watchEffect } from 'vue';

const props = defineProps({
    item: Object,
    showDialog: Boolean,
    votingOpen: Boolean,
});

const dialog = ref(props.showDialog);

const ratings = [
    { id: 'serving', name: 'Saque' },
    { id: 'defense', name: 'Defesa' },
    { id: 'attacking', name: 'Ataque' },
    { id: 'passing', name: 'Passe' },
    { id: 'teamWork', name: 'Trabalho em equipe' }
]

const playerRating = ref({
    serving: 3,
    defense: 3,
    attacking: 3,
    passing: 3,
    teamWork: 3
})

watchEffect(() => {
    dialog.value = props.showDialog;
});

const emit = defineEmits(['update:showDialog']);

const closeDialog = () => {
    emit('update:showDialog', false);
    playerRating.value = {
        serving: 3,
        defense: 3,
        attacking: 3,
        passing: 3,
        teamWork: 3
    }
};

const increaseRating = (rating) => {
    if(rating <= 5) rating += 0.5
}

const decreaseRating = (rating) => {
    if(rating >= 0) rating -= 0.5
}

const saveRating = () => {
    closeDialog()
}
</script>
  