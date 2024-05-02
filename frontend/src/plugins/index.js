/**
 * plugins/index.js
 *
 * Automatically included in `./src/main.js`
 */

// Plugins
import vuetify from './vuetify'
import router from './router'
import instance from './axios'

export function registerPlugins (app) {
  app.use(vuetify)
  app.use(router)
  app.provide('axios', instance)
}
