<template>
  <div id="container-fluid">    
    <pageHeader></pageHeader>
    <router-view/>
  </div>
</template>

<script>
  import Header from '@/components/Header.vue';
  import axios from 'axios'

  export default {
    name: 'App',
    components: {
      pageHeader: Header,
    },
    beforeCreate() {
      this.$store.commit('initializeStore')

      const token = this.$store.state.token

      if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
      } else {
        axios.defaults.headers.common['Authorization'] = ""
      }
    }
  }
</script>

<style lang="scss">
@import '../node_modules/bootstrap';
body{
  background-color:ghostwhite;
  color:darkblue;
}
</style>
