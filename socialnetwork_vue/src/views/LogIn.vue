<template>
  <div class="container">
    <div class="row justify-content-center">
      <h1 class="text-center my-4">Log In</h1>

      <div class="col-4 shadow bg-white p-4">
        <form @submit.prevent="submitForm">
          <div class="input-group mb-3">
            <div class="input-group-prepend">
              <span class="input-group-text" id="username">Username</span>
            </div>
            <input type="text" class="form-control" placeholder="username" v-model="username">
          </div>
          <div class="input-group mb-3">
            <div class="input-group-prepend">
              <span class="input-group-text" id="password">Password</span>
            </div>
            <input type="password" class="form-control" placeholder="Password" v-model="password">
          </div>
          <div class="alert alert-danger mb-3" v-if="errors.length">
            <p class="text-center" v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>
          <button type="submit" class="btn btn-primary pull-left">Log in</button>

          <hr>
          Or <router-link to="/sign-up">click here</router-link> to sign up
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LogIn',
  data() {
    return {
      username: '',
      password: '',
      errors: []
    }
  },
  mounted() {
    document.title = 'Log In | Social Network'
  },
  methods: {
    // submits form and authentication headers
    async submitForm() {
      axios.defaults.headers.common["Authorization"] = ""

      localStorage.removeItem("token")

      const formData = {
        username: this.username,
        password: this.password
      }
      // sends username and password to api
      await axios
        .post("/api/v1/token/login/", formData)
        // recieves auth token and stores it 
        .then(response => {
          const token = response.data.auth_token
          this.$store.commit('setToken', token)

          axios.defaults.headers.common["Authorization"] = "Token " + token
          localStorage.setItem("token", token)
        })
        .catch(error => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`)
            }
          } else {
            this.errors.push('Something went wrong. Please try again')

            console.log(JSON.stringify(error))
          }
        })
      // retrieves current username an id from api
      await axios
        .get('/api/v1/users/me/')
        .then(response => {
          this.$store.commit('setUser', {
            'id': response.data.id,
            'username': response.data.username
          })
          localStorage.setItem('username', response.data.username)
          localStorage.setItem('userid', response.data.id)
        })

      const toPath = this.$route.query.to || '/feed'
      this.$router.push(toPath)

        .catch(error => {
          console.log(error)
        })
    }
  }
}


</script>