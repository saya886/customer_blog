import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import i18n from './i18n'
import axios from 'axios'
import VueAxios from 'vue-axios'
 
Vue.use(VueAxios, axios)
Vue.config.productionTip = false
Vue.prototype.$axios = axios
Vue.axios.defaults.baseURL = "http://198.13.41.56:8000"


new Vue({
  i18n,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
