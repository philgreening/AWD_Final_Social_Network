<template>
  <div class="container p-4">
    <div class="row">
      <p class="h1 text-center my-4">My Feed</p>
      <p class="h1 text-center " v-if="!ifFollowing">No posts to display </p>
      <template v-else>
        <div class="col-12 offset-md-3">
          <div class="post" v-for="post in posts" v-bind:key="post">
            <div v-for="follow in following" v-bind:key="follow">
              <template v-if="post.user == follow.following && user == follow.user">
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
              </template>
            </div>
          </div>
        </div>
      </template>
    </div>
  </div>
</template>

<script>
// Import axios to make api calls  
import axios from 'axios';

// import dependancies to format timestamp
import dayjs from 'dayjs';
import relativeTime from 'dayjs/plugin/relativeTime';

export default {
  name: 'MyFeed',
  data() {
    return {
      posts: [],
      post_text: '',
      user: this.$store.state.user.username,
      post_date: 'Now',
      following: []
    }
  },
  async mounted() {
    document.title = 'Feed | Social Network'

    dayjs.extend(relativeTime);

    // gets posts from api
    await axios
      .get("/api/v1/posts/")
      .then(response => {
        this.posts = response.data
      })

    // gets follower relationships from api
    await axios
      .get("/api/v1/following_list/")
      .then(response => {
        this.following = response.data
      })

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
    }
  },
  computed: {
    // Returns followed users
    ifFollowing() {
      for (let i = 0; i < this.following.length; i++) {
        if (this.following[i].user == this.user) {
          return true;
        }
      }
      return false;
    }
  }
}
</script>
