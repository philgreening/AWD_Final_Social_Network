<template>
  <div class="container p-4">
    <div class="row">
      <div class="col-12 offset-md-3">
        <div class="shadow p-3 my-3 bg-white rounded w-50">
          <p class="h1">
            <template v-if="!profile_image">
              <img class="rounded-circle me-3" src="../assets/mrx.jpg" width="75" height="75" />
            </template>
            <template v-else>
              <img class="rounded-circle me-3" v-bind:src="profile_image" width="75" height="75" />
            </template>
            @{{user}}
          </p>
          <p class="p-3">{{bio}}</p>
          <h6 class="text-muted"> {{ getFollowingCount }} Following
            {{ getFollowedByCount }} Followers</h6>
        </div>
        <template v-if="ifFollowing">
          <button v-on:click="unfollowUser" type="button"
            class="btn btn-danger text-white shadow mb-5">Unfollow</button>
        </template>
        <template v-else>
          <button v-on:click="followUser" type="button" class="btn btn-info text-white shadow mb-5">Follow</button>
        </template>
        <div class="post" v-for="post in posts" v-bind:key="post">
          <template v-if="post.user == user">
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
  </div>
</template>

<script>
// Import axios to make api calls  
import axios from 'axios';

// import dependancies to format timestamp
import dayjs from 'dayjs';
import relativeTime from 'dayjs/plugin/relativeTime';

export default {
  name: 'UserFeed',
  data() {
    return {
      posts: [],
      following: [],
      following_id: null,
      post_text: '',
      user: '',
      bio: '',
      post_date: 'Now',
      loggedInUser: this.$store.state.user.username,
      profile_image: null,
      following_count: 0,
      followed_by_count: 0,
    }
  },
  async mounted() {
    document.title = 'User Feed | Social Network'

    dayjs.extend(relativeTime);

    //get username from current url by taking the string from the last 
    let currentURL = window.location.pathname;
    const lastItem = currentURL.substring(currentURL.lastIndexOf('/') + 1)
    this.user = lastItem;

    // retrieve posts from api
    await axios
      .get("/api/v1/posts/")
      .then(response => {
        this.posts = response.data;
      })

    // retrieve user details from api
    await axios
      .get("/api/v1/profile/" + this.user)
      .then(response => {
        this.bio = response.data.bio;
        this.profile_image = response.data.profile_image;
      })
      .catch(error => {
        console.log(error)
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
    })

    await axios
      // retrieve user details from api
      .get("/api/v1/following_list/")
      .then(response => {
        this.following = response.data;
      })
      .catch(error => {
        console.log(error)
      })

  },
  methods: {
    async followUser() {

      let following = {
        'user': this.loggedInUser,
        'following': this.user
      }

      await axios
        .post("/api/v1/following_list/", following)
        .then(response => {
          window.location.reload();
        })
        .catch((error) => {
          console.log(error);
        });

    },
    // Gets following id and removes user relationship
    async unfollowUser() {

      for (let i = 0; i < this.following.length; i++) {
        if (this.following[i].following === this.user) {
          this.following_id = this.following[i].id;
        }
      }
      //  deletes user relationship from api
      await axios
        .delete("/api/v1/following/" + this.following_id)
        .then(response => {
          window.location.reload();
        })
        .catch((error) => {
          console.log(error);
        });
    },
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
        if (this.following[i].following == this.user &&
          this.loggedInUser == this.following[i].user) {
          return true;
        }
      }
      return false;
    },
    // calculates following count
    getFollowingCount() {
      for (let i = 0; i < this.following.length; i++) {
        if (this.user === this.following[i].user) {
          this.following_count += 1;
        }
      }
      return this.following_count;
    },
    // calulates followed by count 
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
