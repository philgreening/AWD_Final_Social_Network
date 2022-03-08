<template>
  <div class="container p-4">
    <div class="row">
      <div class="col-12">
        <div class="border my-2 p-4 ">
          <p class="h2">@{{ user }}</p>
          <p class="h2">{{ bio }}</p>
          <button v-on:click="followUser" type="button" class="btn btn-info text-white">Follow</button>
        </div>

        <div class="post" v-for="post in posts" v-bind:key="post">
          <div v-if="post.user == this.user">
            <p></p>
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
    </div>
  </div>
</template>

<script>
import axios from 'axios'

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
    }
  },
  async mounted() {
    document.title = 'User Feed | Social Network'

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
}
</script>
