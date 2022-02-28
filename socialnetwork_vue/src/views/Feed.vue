<template>
  <div class="container p-4">
    <div class="row">
      <div class="col-12">
        <form @submit.prevent="submitPost">
          <div class="form-group">
            <textarea class="form-control mb-3" v-model="post_text" placeholder="Make a post"></textarea>
          </div>
          <div class="form-group mb-5">
            <button type="submit" class="btn btn-success">Submit</button>
          </div>
        </form>
      </div>

      <!-- <div class="wrapper">
        <div class="post" v-for="post in posts" v-bind:key="post">
          <p>{{ post.user }}</p>
          <p>{{ post.post_text }}</p>
          <p>{{ post.post_date }}</p>
        </div>
      </div> -->

      <div class="post" v-for="post in posts" v-bind:key="post">
        <div class="card border-info mb-3">
          <div class="card-header">
            <p> @{{ post.user }}</p>
          </div>
          <div class="card-body text-info">
            <p class="card-text">{{ post.post_text }}</p>
            <p class="card-text h6">{{ post.post_date }}</p>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Feed',
  data() {
    return {
      posts: [],
      post_text: '',
      user: this.$store.state.user.username,
      post_date: 'Now'
    }
  },
  mounted() {
    document.title = 'Feed | Social Network'
    axios
      .get("/api/v1/posts/")
      .then(response =>{
        console.log(response);
        this.posts = response.data
      })

  },
  methods: {
    submitPost() {
      console.log('submitPost');

      //submit post if there is an entry
      if (this.post_text.length > 0) {
        let post_data = {
          'post_text': this.post_text,
          'user': this.user,
          'post_date': this.post_date
        };
        //sent post to the top of the stack
        this.posts.unshift(post_data);

        //send post and auth token to api end point
        axios
          .post("/api/v1/posts/", post_data)
          .then(response => {
            // const token = response.data.auth_token
            // axios.defaults.headers.common["Authorization"] = "Token " + token
          })
          .catch((error) => {
            console.log(error);
          });
      }
      // clear post text for next post   
      this.post_text = '';
    }
  }
}
</script>
