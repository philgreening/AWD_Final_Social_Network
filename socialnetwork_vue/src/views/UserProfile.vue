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
              <span class="input-group-text" id="bio">Bio</span>
            </div>
            <textarea class="form-control" placeholder="Create a Bio..." v-model="bio"></textarea>
          </div>
          <div class="input-group mb-3">
            <div class="input-group-prepend">
            </div>
            <input type="file" class="form-control" placeholder="Upload profile image">
          </div>
          <!-- <div class="alert alert-danger mb-3" v-if="errors.length">
            <p class="text-center" v-for="error in errors" v-bind:key="error">{{ error }}</p>
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
      user: this.$store.state.user.username,
      first_name: '',
      last_name: '',
      bio: '',
      errors: []
    }
  },
//   methods: {
//     submitForm() {
//       this.errors = []
//       console.log(this.errors);

//       if (this.username === '') {
//         this.errors.push('Please enter a username')
//       }
//       if (this.password === '') {
//         this.errors.push('Please enter a password')
//       }
//       if (this.password !== this.password2) {
//         this.errors.push('the Passwords don\'t match')
//       }
//       if (!this.errors.length) {
//         const formData = {
//           username: this.username,
//           password: this.password
//         }
//         axios
//           .post("/api/v1/users/", formData)
//           .then(Response => {
//             this.$router.push('/log-in')
//           })
//           .catch(error => {
//             if (error.response) {
//               for (const property in error.response.data) {
//                 this.errors.push(`${property}: ${error.response.data[property]}`)
//               }
//               console.log(JSON.stringify(error.response.data))
//             } else if (error.message) {
//               this.errors.push('Something went wrong. Please try again')

//               console.log(JSON.stringify(error))
//             }
//           })
//       }
//     }
//   }
}
</script>