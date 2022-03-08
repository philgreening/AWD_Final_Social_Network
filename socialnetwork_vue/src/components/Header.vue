<template>
  <nav class="navbar navbar-expand navbar-dark bg-dark p-4">
    <div class="container-fluid">
      <router-link to="/" class="navbar-brand"><strong>Social Network</strong></router-link>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navcollapse"
        aria-controls="navcollapse" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navcollapse">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item mx-2">
            <router-link to="/feed" class="nav-link"><strong>My Feed</strong></router-link>
          </li>
           <li class="nav-item mx-2">
            <router-link to="/my-profile" class="nav-link"><strong>My Profile</strong></router-link>
          </li>
          <li class="nav-item mx-2">
            <router-link to="/profile" class="nav-link"><strong>Edit Profile</strong></router-link>
          </li>
        </ul>
      
        <!-- <div v-if="this.$store.state.isauthenticated"> -->

        <!-- </div> -->
        <!-- <div v-else> -->
        <!-- </div> -->
        <!-- <router-link to="/log-in" class="btn btn-light"><strong>Log In</strong></router-link>
        <form @submit.prevent="logout">
            <button type="submit" class="btn btn-danger">Log Out</button>
        </form> -->
        <!-- <router-link to="/" class="btn btn-danger"><strong>Log Out</strong></router-link> -->
        <form action="/search" method="get" id="search-form" >
          <div class="input-group mx-auto ">
            <input type="text" class="form-control" name="q" placeholder="Search " required>
            <div class="input-group-append">
              <button class="btn btn-success" type="submit" form="search-form">
                <!-- <i class="fa fa-search"></i> -->Search
              </button>
            </div>
          </div>
        </form>
        </div>

        <div class="navbar-end mx-2">
          <router-link to="/log-in" class="btn btn-light"><strong>Log In</strong></router-link>
        </div>


        <div class="navbar-end mx-2">
          <form @submit.prevent="logout">
            <button type="submit" class="btn btn-danger">Log Out</button>
          </form>
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