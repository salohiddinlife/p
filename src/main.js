import '@/assets/styles/main.scss'
import {
    createApp
} from 'vue'
import {
    createPinia
} from 'pinia'
import App from './App.vue'
import {
    VueWindowSizePlugin
} from 'vue-window-size/plugin';


const pinia = createPinia()
const app = createApp(App)

app.use(VueWindowSizePlugin)
app.use(pinia)
app.mount('#app')