<template>
  <div class="container p-4">
    <div class="p-5 mb-4 bg-white shadow-sm rounded-3">
      <div class="container-fluid py-5">
        <h1 class="display-5 fw-bold">Welcome to YourSpace</h1>
        <p class="col-8 fs-4">Please sign up or log in</p>
        <router-link to="/sign-up" class="btn btn-lg btn-danger me-2 shadow"><strong>Sign Up</strong></router-link>
        <router-link to="/log-in" class="btn btn-lg btn-success ms-2 shadow"><strong>Log In</strong></router-link>
      </div>
    </div>
    <div class="row">
      <p class="h1 text-center">Latest Posts</p>
      <div class="col-12 offset-md-3">
        <!-- displays the most recent 5 posts -->
        <div class="post" v-for="post in posts.slice(0, 5)" v-bind:key="post">
          <div class="card shadow mb-3 rounded w-50">
            <div class="card-header">
              <p class="h5">
                <template v-if="!post.profile_image">
                  <img class="rounded-circle me-3" src="../assets/mrx.jpg" width="50" height="50" />
                </template>
                <template v-else>
                  <img class="rounded-circle me-3" v-bind:src="post.profile_image" width="50" height="50" />
                </template>
                @{{ post.user }}
                <small class="h6 text-muted">{{ formatDate(post.post_date) }}</small>
              </p>
            </div>
            <div class="card-body">
              <p class="card-text">{{ post.post_text }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// Import axios to make api calls
import axios from "axios";

// import dependancies to format timestamp
import dayjs from "dayjs";
import relativeTime from "dayjs/plugin/relativeTime";

export default {
  name: "Home",
  data() {
    return {
      posts: [],
      post_text: "",
      post_date: "Now",
    };
  },
  async mounted() {
    document.title = "Home: latest posts | Social Network";

    dayjs.extend(relativeTime);

    await axios.get("/api/v1/posts/").then((response) => {
      this.posts = response.data;
    }),
      // get profile picture then match picture to user in posts
      await axios.get("/api/v1/profiles/").then((response) => {
        for (let i = 0; i < this.posts.length; i++) {
          for (let j = 0; j < response.data.length; j++) {
            if (this.posts[i].user === response.data[j].user) {
              this.posts[i].profile_image = response.data[j].profile_image;
            }
          }
        }
      });
  },
  methods: {
    // format date into a more readable format i.e. 2 days ago
    formatDate(dateString) {
      const date = dayjs(dateString);
      return date.fromNow();
    },
  },
};
</script>
