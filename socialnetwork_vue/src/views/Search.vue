<template>
  <div class="container p-4 ">
    <div class="col-12 offset-md-3 ">
      <div class="shadow p-2 my-4 bg-white w-50" v-for="user in users" v-bind:key="user">
        <p class="h3 position-relative p-2">

          <template v-if="!user.profile_image">
            <img class="rounded-circle me-3" src="../assets/mrx.jpg" width="50" height="50" />
          </template>
          <template v-else>
            <img class="rounded-circle me-3" v-bind:src="user.profile_image" width="50" height="50" />
          </template>
          @{{ user.user }}
          <router-link :to="{ name: 'UserFeed', params: { user: user.user } }"
            class="btn btn-warning button mx-5 position-absolute end-0 shadow">
            View Profile
          </router-link>

        </p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Search",
  data() {
    return {
      users: [],
      query: "",
    };
  },
  mounted() {
    // get search params from sent url
    document.title = "Search Results | Social Network";
    let uri = window.location.search.substring(1);
    let params = new URLSearchParams(uri);
    if (params.get("q")) {
      this.query = params.get("q");
      this.performSearch();
    }
  },
  methods: {
    // uses search params to query api
    async performSearch() {
      await axios
        .get("/api/v1/search/?q=" + this.query)
        .then((response) => {
          this.users = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
