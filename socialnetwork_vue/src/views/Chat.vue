<template>
  <div>
    What chat room would you like to enter?<br>
    <input id="room-name-input" ref="room_input" @keyup.enter="keyUp" type="text" size="100"><br>
    <input id="room-name-submit" @click="getStoreRoom" type="button" value="Enter">
  </div>

</template>

<script>

export default {
  name: 'Home',
  mounted() {
    this.$refs.room_input.focus();

  },
  methods: {
    getStoreRoom() {
      let roomName = document.querySelector('#room-name-input').value;
      let url = '/chat/' + roomName;
      this.$store.commit('setChatRoom', url)
      console.log(this.$store.state.room, ' : stored chatroom')
      this.$router.push(url);
    },
    keyUp() {

      this.getStoreRoom();
    }

  }

}
</script>