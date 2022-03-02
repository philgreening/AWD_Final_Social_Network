<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-4 m-4">
        <h1 class="text-center p-4">{{ user }} Create Profile</h1>
        <form @submit.prevent="submitForm">
          <div class="input-group mb-3">
            <div class="input-group-prepend">
              <span class="input-group-text" id="firstname">First Name</span>
            </div>
            <input type="text" class="form-control" placeholder="First Name" v-model="first_name">
          </div>
          <div class="input-group mb-3">
            <div class="input-group-prepend">
              <span class="input-group-text" id="lastname">Last Name</span>
            </div>
            <input type="text" class="form-control" placeholder="Last Name" v-model="last_name">
          </div>
          <div class="input-group mb-3">
            <div class="input-group-prepend">
              <span class="input-group-text h-100" id="bio">Bio</span>
            </div>
            <textarea class="form-control" placeholder="Create a Bio..." v-model="bio"></textarea>
          </div>
          <div class="input-group mb-3">
            <div class="input-group-prepend">
              <span class="input-group-text" id="profileimage">Profile Image</span>
            </div>
            <input type="file" class="form-control">
          </div>
          <div class="alert alert-danger mb-3" v-if="errors.length">
            <p class="text-center" v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>
          <!-- <div class="alert alert-success mb-3" v-if="success.length">
            <p class="text-center" >{{ success }}</p>
          </div> -->
          <button type="submit" class="btn btn-primary pull-left">Submit</button>

          <!-- <hr>
          Or <router-link to="/log-in">click here</router-link> to log in -->
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'UserProfile',
  data() {
    return {
      userid: localStorage.username,
      user: localStorage.username,
      first_name: '',
      last_name: '',
      bio: '',
      success: '',
      errors: []
    }
  },
    mounted() {
    document.title = 'Create User Profile | Social Network'
  },
  methods: {
    submitForm() {
      this.errors = []
      console.log(this.errors);

      if (this.user === '') {
        this.errors.push('Please enter your first name')
      }
      if (this.first_name === '') {
        this.errors.push('Please enter your first name')
      }
      if (this.last_name === '') {
        this.errors.push('Please eter your surmane')
      }
        if (!this.errors.length) {  
        const formData = {
          user: this.user,
          first_name: this.first_name,
          last_name: this.last_name,
          bio: this.bio,
        }
        
        axios
          .post("api/v1/profile/" + this.user, formData)
          .then(Response => {
            // this.success = "Profile created"
            localStorage.removeItem('username')
            this.$router.push('/log-in')
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