<template>
  <div class="container p-4">
    <div class="row">
      <div class="col-8">
                    <h1>@{{user}}</h1>
                    <p>{{bio}}</p>

        <form @submit.prevent="submitPost">
          <div class="form-group">
            <textarea class="form-control my-3" v-model="post_text" placeholder="Make a post"></textarea>
          </div>
          <div class="form-group mb-5">
            <button type="submit" class="btn btn-success">Submit</button>
          </div>
        </form>


      <!-- <div class="wrapper">
        <div class="post" v-for="post in posts" v-bind:key="post">
          <p>{{ post.user }}</p>
          <p>{{ post.post_text }}</p>
          <p>{{ post.post_date }}</p>
        </div>
      </div> -->
        <!-- <h1 v-if="following.length === 0" >No posts to display </h1> -->
      <!-- <div v-else> -->

      <div class="post" v-for="post in posts" v-bind:key="post">
          <div v-if="post.user == user">

        <!-- <div v-for="follow in following" v-bind:key="follow">
          <div v-if="post.user == follow.user"> -->

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
              <!-- <h1 v-else>No Posts to display</h1> -->
        </div>
      </div>
          <div class="col-4">
              <h1>Following</h1>
                    <div v-for="follow in following" v-bind:key="follow">
                        <h2>@{{follow.user}}</h2>

    </div>
</diV>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MyProfile',
  data() {
    return {
      posts: [],
      post_text: '',
      user: this.$store.state.user.username,
      bio: '',
      post_date: 'Now',
      following: []
    }
  },
 async mounted() {
    document.title = 'My Profile | Social Network'
    console.log(this.following)

   
   await axios
      .get("/api/v1/posts/")
      .then(response =>{
        console.log(response);
        this.posts = response.data;
        console.log("posts",this.posts)
      })

    await axios
      .get("/api/v1/profile/" + this.user)
      .then(response =>{
        console.log(response);
        this.bio = response.data.bio;
        this.following = response.data.following;
        console.log("following: ", this.following)
      })

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
    }
  }
}
</script>
