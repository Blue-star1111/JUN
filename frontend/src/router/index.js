import Vue from 'vue';
import VueRouter from 'vue-router';

import HomeView from '@/views/HomeView.vue'
import SafetyView from '../views/safety/SafetyView.vue'
// import SafeDetect from '@/views/safety/SafeDetect.vue'
// import HealthView from '@/views/health/HealthView.vue'
import HealthPoll from '../views/health/HealthPoll.vue'
import EnvironView from '../views/environment/EnvironView.vue'
// import EnvironElectric from '@/views/environment/EnvironElectric.vue'

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    redirect: '/main',
  },
  {
    path: '/main',
    name: 'main',
    component: () => import('@/views/MainView.vue'),
    children: [
      {
        path: 'home',
        name: 'home',
        components: {
          contents: HomeView,
        },
      },
      {
        path: 'safety',
        name: 'safety',
        components: {
          contents: SafetyView,
        },
      },
      {
        path: 'health',
        name: 'health',
        components: {
          contents: HealthPoll,
        },
      },
      {
        path: 'energy',
        name: 'energy',
        components: {
          contents: EnvironView,
        }
      },   
    ]
  },
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
  });
  
  
  export default router;
  