<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-4 m-4">
           <div class="text-center my-2">
          <p class="h1">@{{ user }}</p>
          <p class="h3">Create a Profile</p>
        </div>
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
                                        <!-- <img src={{profile_imgage}}> -->

            <div class="input-group-prepend">
              <span class="input-group-text" id="profileimage">Profile Image</span>
            </div>
            <input type="file" class="form-control" @change="onFileUpload">
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
      profile_image: '',
      success: '',
      errors: []
    }
  },
  mounted() {
    document.title = 'Create User Profile | Social Network'
  },
  methods: {
    // gets selected file and passes it to the profile image variable
    onFileUpload(img) {
      this.profile_image = img.target.files[0];
    },
    async submitForm() {
      this.errors = []

      if (this.first_name === '') {
        this.errors.push('Please enter your first name')
      }
      if (this.last_name === '') {
        this.errors.push('Please eter your surmane')
      }
      if (!this.errors.length) {

        // create and append data collected from form
        const formData = new FormData();

        formData.append('user', this.user)
        formData.append('first_name', this.first_name)
        formData.append('last_name', this.last_name)
        formData.append('bio', this.bio)
        formData.append('profile_image', this.profile_image)

        // post form data to api endpoint
        await axios
          .post("api/v1/updateprofile/" + this.user, formData)
          .then(Response => {
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