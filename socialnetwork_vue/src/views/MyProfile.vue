<template>
  <div class="container p-4">
    <div class="row">
      <div class="col-6 offset-md-1">
        <div class="shadow p-3 my-3 bg-white rounded">
          <p class="h1">
            <!-- Displays generic profile image if none found -->
            <template v-if="!profile_image">
              <img class="rounded-circle me-3" src="../assets/mrx.jpg" width="75" height="75" />
            </template>
            <template v-else>
              <!-- Displays user profile image if found -->
              <img class="rounded-circle me-3" v-bind:src="profile_image" width="75" height="75" />
            </template>
            @{{user}}

          </p>

          <p class="p-3">{{bio}}</p>
          <h6 class="text-muted"> {{ getFollowingCount }} Following
            {{ getFollowedByCount }} Followers</h6>
        </div>

        <form @submit.prevent="submitPost">
          <div class="form-group ">
            <textarea class="form-control mb-3 shadow rounded" v-model="post_text" placeholder="Make a post"></textarea>
          </div>
          <div class="form-group mb-5 w-50">
            <button type="submit" class="btn btn-success shadow">Submit</button>
          </div>
        </form>

        <div class="post" v-for="post in posts" v-bind:key="post">
          <template v-if="post.user == user">
            <div class="card shadow mb-3 rounded ">
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
      <div class="col-3 offset-md-1">
        <p class="h1 text-center">Following</p>

        <div v-for="follow in following" v-bind:key="follow">
          <!-- Displays users followed -->
          <template v-if="follow.following && user == follow.user">
            <router-link class="text-decoration-none" :to="{ name: 'UserFeed', params: { user: follow.following } }">
              <div class="shadow p-2 my-4 bg-white">

                <p class="h3 my-2">

                  <template v-if="!follow.profile_image">
                    <img class="rounded-circle me-3" src="../assets/mrx.jpg" width="50" height="50" />


                  </template>
                  <template v-else>
                    <img class="rounded-circle me-3" v-bind:src="follow.profile_image" width="50" height="50" />

                  </template>
                  @{{follow.following}}
                </p>
              </div>

            </router-link>
          </template>

        </div>
      </diV>
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
  name: 'MyProfile',
  data() {
    return {
      posts: [],
      post_text: '',
      user: this.$store.state.user.username,
      bio: '',
      post_date: 'Now',
      following: [],
      profile_image: null,
      following_count: 0,
      followed_by_count: 0,
    }
  },
  async mounted() {
    document.title = 'My Profile | Social Network'

    dayjs.extend(relativeTime);

    // gets posts from api
    await axios
      .get("/api/v1/posts/")
      .then(response => {
        this.posts = response.data;
      })

    // gets user profile from api
    await axios
      .get("/api/v1/profile/" + this.user)
      .then(response => {
        this.bio = response.data.bio;
        this.profile_image = response.data.profile_image;
      })

    // gets follower relationship from api
    await axios
      .get("/api/v1/following_list/")
      .then(response => {
        this.following = response.data;
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

    // get profile picture then match picture to following user
    await axios.get("/api/v1/profiles/").then((response) => {
      for (let i = 0; i < this.following.length; i++) {
        for (let j = 0; j < response.data.length; j++) {
          if (this.following[i].following === response.data[j].user) {
            this.following[i].profile_image = response.data[j].profile_image;
          }
        }
      }
    });

  },
  methods: {
    async submitPost() {

      //submit post if there is an entry
      if (this.post_text.length > 0) {
        let post_data = {
          'post_text': this.post_text,
          'user': this.user,
          'post_date': this.post_date,
          'profile_image': this.profile_image
        };
        //sent post to the top of the stack
        this.posts.unshift(post_data);

        await axios
          .post("/api/v1/posts/", post_data)
          .then(response => {})
          .catch((error) => {
            console.log(error);
          });
      }
      // clear post text for next post   
      this.post_text = '';
      window.location.reload();

    },
    // format date into a more readable format i.e. 2 days ago
    formatDate(dateString) {
      const date = dayjs(dateString);
      return date.fromNow();
    }
  },
  computed: {
    // returns following count
    getFollowingCount() {
      for (let i = 0; i < this.following.length; i++) {
        if (this.user === this.following[i].user) {
          this.following_count += 1;
        }
      }
      return this.following_count;
    },
    // returns followed by count
    getFollowedByCount() {
      for (let i = 0; i < this.following.length; i++) {
        if (this.user === this.following[i].following) {
          this.followed_by_count++;
        }
      }
      return this.followed_by_count;
    }
  }
}

</script>
