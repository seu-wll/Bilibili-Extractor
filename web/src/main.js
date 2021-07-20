import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui' //element-ui的全部组件
import 'element-ui/lib/theme-chalk/index.css'//element-ui的css
import VideoPlayer from 'vue-video-player'
import VueSplide from '@splidejs/vue-splide';
import VueResource from 'vue-resource'
require('video.js/dist/video-js.css')
require('vue-video-player/src/custom-theme.css')
Vue.use(VideoPlayer)
Vue.use(VueSplide);
Vue.use(ElementUI) //使用elementUI
Vue.use(VueResource)
import Vuex from 'vuex'
Vue.use(Vuex)
import store from './store'
// import VueAwesomeSwiper from 'vue-awesome-swiper'
// import 'swiper/css/swiper.css'
// Vue.use(VueAwesomeSwiper)
import VideoBackground from 'vue-responsive-video-background-player'
Vue.component('video-background', VideoBackground);
const Bus = new Vue()
new Vue({
  router,
  Bus,
  store,
  render: h => h(App),
}).$mount('#app')
