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
        </div>
        <button v-on:click="followUser" type="button" class="btn btn-info text-white shadow mb-5">Follow</button>
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
      post_text: '',
      user: '',
      userid: '',
      bio: '',
      post_date: 'Now',
      loggedInUser: this.$store.state.user.username,
      loggedInUserId: this.$store.state.user.id,
      profile_image: null
    }
  },
  async mounted() {
    document.title = 'User Feed | Social Network'

        dayjs.extend(relativeTime);

    //get username from current url by taking the string from the last /
    let currentURL = window.location.pathname;
    const lastItem = currentURL.substring(currentURL.lastIndexOf('/') + 1)
    this.user = lastItem;
    console.log(this.user, " :current user");

    await axios
      // retrieve posts from api
      .get("/api/v1/posts/")
      .then(response => {
        // console.log(response);
        this.posts = response.data;
      })

    await axios
      // retrieve user details from api
      .get("/api/v1/profile/" + this.user)
      .then(response => {
        // console.log(response)
        this.bio = response.data.bio;
        this.profile_image = response.data.profile_image;
      })
      .catch(error => {
        console.log(error)
      })




  },
  methods: {
    async followUser() {
      let follows = {
        'following': this.user
      }

      let followed_by = {
        'followed_by': this.loggedInUserId
      }


      await axios
        .patch("/api/v1/profile/" + this.loggedInUser, follows)
        .then(response => {
          console.log(response, ": line 91 userfeed")
        })
        .catch((error) => {
          console.log(error);
        });
        
      await axios
        .patch("/api/v1/profile/" + this.user, followed_by)
        .then(response => {
        // this.$router.push({name:Class, params: { id: classID}})

            console.log(response, ": line 100 userfeed")
        })
        .catch((error) => {
          console.log(error);
        });

    },
            formatDate(dateString) {
            const date = dayjs(dateString);
            return date.fromNow();
        }
  }
    //     submitPost() {
    //       console.log('submitPost');

    //       //submit post if there is an entry
    //       if (this.post_text.length > 0) {
    //         let post_data = {
    //           'post_text': this.post_text,
    //           'user': this.user,
    //           'post_date': this.post_date
    //         };
    //         //sent post to the top of the stack
    //         this.posts.unshift(post_data);

    //         //send post and auth token to api end point
    //         axios
    //           .post("/api/v1/posts/", post_data)
    //           .then(response => {
    //             // const token = response.data.auth_token
    //             // axios.defaults.headers.common["Authorization"] = "Token " + token
    //           })
    //           .catch((error) => {
    //             console.log(error);
    //           });
    //       }
    //       // clear post text for next post   
    //       this.post_text = '';
    //     }
  
}
</script>
