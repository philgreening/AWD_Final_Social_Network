<template>
<div>
        <div v-for="user in users" v-bind:key="user">
            <h2>{{ user.user }}</h2>
        </div>

        
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
