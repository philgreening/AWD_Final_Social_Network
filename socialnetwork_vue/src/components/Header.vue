<template>
    <nav class="navbar navbar-expand navbar-dark bg-dark p-4">
      <div class="container-fluid">
        <router-link to="/" class="navbar-brand"><strong>Social Network</strong></router-link>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navcollapse" aria-controls="navcollapse" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        
      <div class="collapse navbar-collapse" id="navcollapse">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item ">
            <router-link to="/feed" class="nav-link"><strong>Feed</strong></router-link>
          </li>
          <li class="nav-item ">
            <router-link to="/profile" class="nav-link"><strong>My Profile</strong></router-link>
          </li>
        </ul>
        <!-- <div v-if="this.$store.state.isauthenticated"> -->
            <form @submit.prevent="logout">
                <button type="submit" class="btn btn-danger">Log Out</button>
            </form>
        <!-- </div> -->
        <!-- <div v-else> -->
            <router-link to="/log-in" class="btn btn-light"><strong>Log In</strong></router-link>
        <!-- </div> -->
        <!-- <router-link to="/log-in" class="btn btn-light"><strong>Log In</strong></router-link>
        <form @submit.prevent="logout">
            <button type="submit" class="btn btn-danger">Log Out</button>
        </form> -->
        <!-- <router-link to="/" class="btn btn-danger"><strong>Log Out</strong></router-link> -->
        </div>
      </div>
    </nav>
</template>

<script>

import axios from 'axios'

export default {
  name: 'Header',
    methods: {
      async logout() {
        // call logout api end point and send token
        await axios
          .post('api/v1/token/logout/')
          .then(response => {
            console.log('logged out')
          })
          .catch(error => {
            console.log(JSON.stringify(error))
          })
          // remove authentication token and data
          axios.defaults.headers.common["Authorization"] = ""
          localStorage.removeItem("token")
          localStorage.removeItem('username')
          localStorage.removeItem('userid')
          this.$store.commit('removeToken')
          this.$router.push('/')
        },
    },
}

</script>