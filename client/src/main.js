import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import VueAxios from './plugins/axios'

Vue.use(VueAxios)
Vue.config.productionTip = false

Vue.prototype.$hostname = 'http://91.122.35.145.:5000';

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
