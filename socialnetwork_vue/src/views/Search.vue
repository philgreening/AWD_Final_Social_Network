<template>
  <div class="container p-4">
    <row>
      <div class="col-12">
      <div v-for="user in users" v-bind:key="user">
        <router-link :to="{ name: 'UserFeed', params: {user: user.user } }">
          <p class="h2">{{ user.user }}</p>
        </router-link>
      </div>
      </div>
    </row>


  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Search',
  data() {
    return {
      users: [],
      query: '',
    }
  },
  mounted() {
    document.title = 'Search Results | Social Network'
      let uri = window.location.search.substring(1)
        let params = new URLSearchParams(uri)
        if (params.get('q')) {
            this.query = params.get('q')
            this.performSearch()
        }

  },
     methods: {
        async performSearch() {
            await axios
                .get('/api/v1/search/?q=' + this.query)
                .then(response => {
                    this.users = response.data
                    console.log(this.users, ": line 37")
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>
