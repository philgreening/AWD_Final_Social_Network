<template>
  <div class="container p-4">
    <div class="row">
      <p class="h1 text-center my-4">My Feed</p>
      <div class="col-12 offset-md-3">
        <p class="h1" v-if="following.length === 0">No posts to display </p>
        <template v-else>
          <div class="post" v-for="post in posts" v-bind:key="post">
            <div v-for="follow in following" v-bind:key="follow">
              <template v-if="post.user == follow.user">
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
        </template>
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
    console.log(this.following)

    dayjs.extend(relativeTime);

   await axios
      .get("/api/v1/posts/")
      .then(response =>{
        console.log(response);
        this.posts = response.data
        console.log("posts",this.posts)
      })

    await axios
      .get("/api/v1/profile/" + this.user)
      .then(response =>{
        console.log(response);
        this.following = response.data.following
        console.log("following: ", this.following)
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
   async submitPost() {
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

        //send post data to api end point
       await axios
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
    },
        formatDate(dateString) {
            const date = dayjs(dateString);
            return date.fromNow();
        }
  }
}
</script>
