import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Vacancy from '../views/Vacancy.vue'
import VacancyDetail from '@/views/VacancyDetail.vue'
import VacancyCreate from '@/views/VacancyCreate.vue'
import ResumeCreate from '@/views/ResumeCreate.vue'
import SingUp from '@/views/SingUp.vue'
import SingIn from '@/views/SingIn.vue'
import Responses from '@/views/Responses.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SingUp
  },
  {
    path: '/signin',
    name: 'SignIn',
    component: SingIn
  },
  {
    path: '/vacancy',
    name: 'Vacancy',
    component: Vacancy
  },
  {
    path: '/vacancy/create',
    name: 'VacancyCreate',
    component: VacancyCreate
  },
  {
    path: '/vacancy/:id',
    name: 'Vacancy-Detail',
    component: VacancyDetail
  },
  {
    path: '/resume/create',
    name: 'ResumeCreate',
    component: ResumeCreate
  },
  {
    path: '/responses',
    name: 'Responses',
    component: Responses
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
