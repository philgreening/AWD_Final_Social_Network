<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-4 m-4">
        <div class="text-center my-2">
          <p class="h1">@{{ user }}</p>
          <p class="h3">Edit Profile</p>
          <img class="shadow rounded" v-bind:src=profile_image>
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
            <div class="input-group-prepend">
              <span class="input-group-text" id="profileimage">Profile Image </span>
            </div>
            <input type="file" class="form-control" @change="onFileUpload" >
          </div>
          <template class="alert alert-danger mb-3" v-if="errors.length">
            <p class="text-center" v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </template>
          <template class="alert alert-success mb-3" v-if="success.length">
            <p class="text-center">{{ success }}</p>
          </template>
          <button type="submit" class="btn btn-primary pull-left">Submit</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'EditUserProfile',
  data() {
    return {
      // userid: this.$store.state.user.id,
      user: this.$store.state.user.username,
      first_name: '',
      last_name: '',
      bio: '',
      profile_image: '',
      new_profile_image: '',
      success: '',
      errors: []
    }
  },
  mounted() {
    document.title = 'Edit User Profile | Social Network'

    //get values from api and populate form
    axios
      .get("/api/v1/updateprofile/" + this.user)
      .then(response => {
        console.log(response)
        this.first_name = response.data.first_name;
        this.last_name = response.data.last_name;
        this.bio = response.data.bio;
        this.profile_image = response.data.profile_image;
        console.log(this.profile_image, 'Profile image');
      })
      .catch(error => {
        console.log(error)
      })


  },
  methods: {
    onFileUpload(img) {
      // this.profile_image = img.target.files[0];
      this.new_profile_image = img.target.files[0];
    },
    submitForm() {
      this.errors = []
      console.log(this.errors);

      if (this.user === '') {
        this.errors.push('Please enter your first name')
      }
      if (this.first_name === '') {
        this.errors.push('Please enter your last name')
      }
      if (this.last_name === '') {
        this.errors.push('Please enter your surmane')
      }
      if (!this.errors.length) {  
       // create and append data collected from form
        const formData = new FormData();

        formData.append('user', this.user)
        formData.append('first_name', this.first_name)
        formData.append('last_name', this.last_name)
        formData.append('bio', this.bio)
        formData.append('profile_image', this.new_profile_image)

      axios
        .put("api/v1/updateprofile/" + this.user, formData)
        .then(Response => {
          this.success = "Profile updated"
          this.$router.push('#')
          setTimeout(function(){ window.location.reload()}, 2000);
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