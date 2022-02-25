<template>
    <div class="container p-4">
        <div class="row">
            <div class="col-12">
                <form @submit.prevent="submitPost">
                    <div class="form-group">
                        <textarea class="form-control" v-model="post_text" placeholder="Make a post"></textarea>
                    </div> 
                    <div class="form-group">
                        <button type="submit" class="btn btn-success">Submit</button>
                    </div>
                </form>
            </div>
            
            <div class="wrapper">
                <div class="post" v-for="post in posts" v-bind:key="post">
                    <p>{{ post.user }}</p>
                    <p>{{ post.post_text }}</p>
                    <p>{{ post.post_date }}</p>
                </div>
            </div>

        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Feed',
    data() {
        return {
            posts: [],
            post_text: '',
            user: '{{ request.User.user }}',
            post_date: 'Now'
        }
    },
    mounted() {
        document.title = 'Feed | Social Network'
    }, 
    methods: {
        submitPost() {
            console.log('submitPost');

            if(this.post_text.length > 0) {
                let post = {
                'post_text': this.post_text,
                'user': this.user,
                'post_date': this.post_date
                };

                this.posts.unshift(post);

              
        }
        this.body = '';

        //  axios
        // .post("/api/v1/post/", post)
        // .then(Response => {
        //     this.$router.push('/feed')
        // })
        }   
    }
}
</script>
