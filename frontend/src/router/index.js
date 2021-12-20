import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Vacancy from '../views/Vacancy.vue'
import VacancyDetail from '@/views/VacancyDetail.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/vacancy',
    name: 'Vacancy',
    component: Vacancy
  },
  {
    path: '/vacancy/:id',
    name: 'Vacancy-Detail',
    component: VacancyDetail
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
