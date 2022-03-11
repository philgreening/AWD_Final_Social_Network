<template>
  <div class="container p-4">
    <div class="row">
      <h1>Latest Posts</h1>

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
  name: 'Home',
  data() {
    return {
      posts: [],
      post_text: '',
      post_date: 'Now'
    }
  },
  async mounted() {
    document.title = 'Home: latest posts | Social Network'
    await axios
      .get("/api/v1/posts/")
      .then(response =>{
        console.log(response);
        this.posts = response.data
      })

  },

}
</script>
