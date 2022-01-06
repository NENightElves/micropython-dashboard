import Vue from 'vue'
import App from './App'
import uView from 'uview-ui'


Vue.config.productionTip = false
Vue.use(uView);

console.log(uni.$u.config.v)

App.mpType = 'app'

const app = new Vue({
  ...App
})
app.$mount()
