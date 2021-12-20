<template>
  <div id="nav">
    <Header />
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> |
    <router-link to="/vacancy">Vacancy</router-link> |
    <router-link to="/vacancy/5">Vacancy-detail</router-link> |
    <router-link to="/signin/">Sign In</router-link> |
  </div>
  <router-view/>
  <Footer />
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue'
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: 'Head',
  components: {
    Header,
    Footer
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
