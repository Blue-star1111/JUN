import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import VueRouter from 'vue-router';
import router from './router'
import axios from 'axios'

Vue.use(VueRouter)
Vue.use(axios)
Vue.prototype.$axios = axios
// Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
