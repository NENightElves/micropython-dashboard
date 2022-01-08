import Vue from 'vue'
import App from './App'
import uView from 'uview-ui'
import axios from 'axios'


Vue.config.productionTip = false
Vue.use(uView);

console.log(uni.$u.config.v);

let baseURL='';
Vue.prototype.$axios=axios.create({baseURL:baseURL});
Vue.prototype.$axios.defaults.headers.post['Content-Type']='application/json'
console.log(Vue.prototype.$axios.config)

App.mpType = 'app'

const app = new Vue({
  ...App
})
app.$mount()
