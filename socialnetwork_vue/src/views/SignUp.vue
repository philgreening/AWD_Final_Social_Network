<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-4 m-4">
        <h1 class="text-center p-4">Sign Up</h1>
        <form @submit.prevent="submitForm">
          <div class="input-group mb-3">
            <div class="input-group-prepend">
              <span class="input-group-text" id="username">Username</span>
            </div>
            <input type="text" class="form-control" placeholder="Username" v-model="username">
          </div>
          <div class="input-group mb-3">
            <div class="input-group-prepend">
              <span class="input-group-text" id="email">Email Address</span>
            </div>
            <input type="email" class="form-control" placeholder="example@email.com" v-model="email">
          </div>
          <div class="input-group mb-3">
            <div class="input-group-prepend">
              <span class="input-group-text" id="password">Password</span>
            </div>
            <input type="password" class="form-control" placeholder="Password" v-model="password">
          </div>
          <div class="input-group mb-3">
            <div class="input-group-prepend">
              <span class="input-group-text" id="password2">Repeat Password</span>
            </div>
            <input type="password" class="form-control" placeholder="Repeat Password" v-model="password2">
          </div>
          <div class="alert alert-danger mb-3" v-if="errors.length">
            <p class="text-center" v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>
          <button type="submit" class="btn btn-primary pull-left">Sign Up</button>

          <hr>
          Or <router-link to="/log-in">click here</router-link> to log in
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'SignUp',
  data() {
    return {
      username: '',
      email:'',
      password: '',
      password2: '',
      errors: []
    }
  },
  methods: {
    submitForm() {
      this.errors = []
      console.log(this.errors);

      if (this.username === '') {
        this.errors.push('Please enter a username')
      }
      if (this.password === '') {
        this.errors.push('Please enter a password')
      }
      if (this.password !== this.password2) {
        this.errors.push('the Passwords don\'t match')
      }
      if (!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password,
          email: this.email
        }
        axios
          .post("/api/v1/users/", formData)
          .then(Response => {
            localStorage.setItem('username', this.username)
            this.$router.push('/create-profile')
          })
          .catch(error => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(`${property}: ${error.response.data[property]}`)
              }
              console.log(JSON.stringify(error.response.data))
            } else if (error.message) {
              this.errors.push('Something went wrong. Please try again')

              console.log(JSON.stringify(error))
            }
          })
      }
    }
  }
}
</script>