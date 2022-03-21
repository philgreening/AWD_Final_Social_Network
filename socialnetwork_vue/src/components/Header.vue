<template>
  <nav class="navbar navbar-expand navbar-dark bg-dark p-4">
    <div class="container-fluid">
      <router-link to="/" class="navbar-brand"><strong>Social Network</strong></router-link>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navcollapse"
        aria-controls="navcollapse" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>


      <div class="collapse navbar-collapse" id="navcollapse">
        <template v-if="$store.state.isAuthenticated">

          <ul class="navbar-nav mr-auto">
            <li class="nav-item mx-2">
              <router-link to="/feed" class="nav-link"><strong>My Feed</strong></router-link>
            </li>
            <li class="nav-item mx-2">
              <router-link to="/my-profile" class="nav-link"><strong>My Profile</strong></router-link>
            </li>
            <li class="nav-item mx-2">
              <router-link to="/chat" class="nav-link"><strong>Chat</strong></router-link>
            </li>
            <li class="nav-item mx-2">
              <router-link to="/profile" class="nav-link"><strong>Edit Profile</strong></router-link>
            </li>
          </ul>

          <form action="/search" method="get" id="search-form">
            <div class="input-group mx-5">
              <input type="text" class="form-control" name="q" placeholder="Search" required>
              <div class="input-group-append">
                <button class="btn btn-success" type="submit" form="search-form">Search</button>
              </div>
            </div>
          </form>
        </template>
      </div>

      <template v-if="!$store.state.isAuthenticated">


        <div class="navbar-end ">

          <router-link to="/log-in" class="btn btn-light me-4"><strong>Log In</strong></router-link>
        </div>
      </template>
      <template v-else>




        <div class="navbar-end ">
          <form @submit.prevent="logout">
            <button type="submit" class="btn btn-danger me-4"><strong>Log Out</strong></button>
          </form>
        </div>
      </template>


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
          axios.defaults.headers.common["Authorization"] = "";
          localStorage.removeItem("token");
          localStorage.removeItem('username');
          localStorage.removeItem('userid');
          this.$store.commit('removeToken');
          this.$store.state.user.username ='';
          this.$router.push('/');
        },
    },
}

</script>