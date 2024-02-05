<template>
  <v-btn>
    <v-menu activator="parent">
      <v-list>
        <v-list-item @click="logout"> Logout </v-list-item>
      </v-list>
    </v-menu>
    <v-avatar icon="mdi-account"> </v-avatar>
    <p>{{ user.first_name }}</p>
    <v-icon> mdi-menu-down </v-icon>
  </v-btn>
</template>
<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const user = { first_name: 'Usuário' }

const logout = () => {
  router.push('login')
}
</script>