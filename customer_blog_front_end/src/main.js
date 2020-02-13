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

// 添加请求拦截器
axios.interceptors.request.use(function (config) {
  // 在发送请求之前做些什么
  config.headers["langc"] = localStorage.getItem('locale')

  // console.log(config.headers)
  return config;
}, function (error) {
  // 对请求错误做些什么
  return Promise.reject(error);
});


new Vue({
  i18n,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
