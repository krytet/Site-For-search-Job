<template>
  <div id="nav">
    <Header />
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> |
    <router-link to="/vacancy">Vacancy</router-link> |
    <router-link to="/vacancy/5">Vacancy-detail</router-link> |
    <router-link to="/signin">Sign In</router-link> |
    <router-link to="/signup">Sign Up Reg</router-link> |
    <router-link to="/vacancy/create">Vacancy Create</router-link> |
    <router-link to="/responses">Responses</router-link> |
    <router-link to="/resume/create">Create Resume</router-link> |
  </div>
  <router-view/>
  <Footer />
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue'
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import axios from 'axios'

export default {
  name: 'Head',
  data() {
    return {
      isAuth: false,
      isComp: false,
    }
  },
  components: {
    Header,
    Footer
  },
  created() {
    window.addEventListener('storage', () => {
      if (localStorage.getItem('token')) {
        this.isAuth = true
        this.isComp = localStorage.getItem('isComp')
      }else {
        this.isAuth = false
      }
    }
    ) 
  }
}
</script>



<style>
  body{
      margin: 0px;
      background-color: #F3F4F6;
      font-size: 14px;
      font-family: 'Helvetica', 'Neue';
      color: #18181B;
  }
</style>
