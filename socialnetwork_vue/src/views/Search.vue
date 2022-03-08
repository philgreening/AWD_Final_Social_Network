<template>
  <div class="container p-4">
    <div class="col-12">
      <div class="border m-2 p-4 w-50" v-for="user in users" v-bind:key="user">
        <p class="h4">@{{ user.user }}</p>

        <router-link
          :to="{ name: 'UserFeed', params: { user: user.user } }"
          class="btn btn-info button"
        >
          View Profile
        </router-link>
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
    document.title = "Search Results | Social Network";
    let uri = window.location.search.substring(1);
    let params = new URLSearchParams(uri);
    if (params.get("q")) {
      this.query = params.get("q");
      this.performSearch();
    }
  },
  methods: {
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
