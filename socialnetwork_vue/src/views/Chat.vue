<template>

  <div class="container my-3 p-4">
    <div class="row">
      <div class="col-2 shadow bg-white p-4 offset-md-1">
        <!-- <input id="room-name-input" ref="room_input" @keyup.enter="keyUp" type="text" size="100"><br> -->
        <label class="h5" for="gen_btn">General: </label>
        <button  class="btn btn-primary m-2" value="General" name="gen_btn" @click="enterRoom($event)">Enter</button><br>
        <label class="h5" for="gen_btn2">Room 2: </label>
        <button class="btn btn-primary m-2" value="Room 2" name="gen_btn2" @click="enterRoom($event)">Enter</button><br>
        <label class="h5" for="gen_btn3">Room 3: </label>
        <button class="btn btn-primary m-2" value="Room 3" name="gen_btn3" @click="enterRoom($event)">Enter</button>

        <!-- <input id="room-name-submit" @click="getStoreRoom" type="button" value="Enter"> -->
      </div>
      <div class="col-6 shadow bg-white p-4 offset-md-1 w-50">
        <div v-if="roomName.length < 1">
          <p class="h1 text-center my-3">Please select a room</p>
        </div>
        <div v-else>
        <p class="h1 text-center my-3">{{roomName}}</p>
        <textarea class="shadow bg-white p-4 w-100 mb-3" id="chat-log" cols="100" rows="20"></textarea><br>
        <input class="shadow w-100 mb-3" id="chat-message-input" ref="message_input" @keyup.enter="submitMessage" type="text" size="100"><br>
        <input class="btn btn-success shadow" id="chat-message-submit" @click="submitMessage" type="button" value="Send">
        </div>
      </div>
    </diV>
  </div>

</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
      roomName: '',
      user: this.$store.state.user.username,
      chatSocket: '',
    }

  },
  mounted() {
    console.log(this.user)
  },

  methods: {
    enterRoom(e) {
      this.roomName = e.target.value;
      this.chatSocket = new WebSocket('ws://127.0.0.1:8000' + '/ws/' + this.roomName + '/');

      let chatMessages = document.querySelector('#chat-log');
      if(chatMessages){
      chatMessages.value = '';
      }
   
    },
    keyUp() {

      this.getStoreRoom();
    },
    submitMessage() {

    const username = this.user
    this.chatSocket.onmessage = function (e) {
      const data = JSON.parse(e.data);
      // console.log(this.user)
      document.querySelector('#chat-log').value += (data.message + '\n');
    };

    this.chatSocket.onclose = function (e) {
      console.error('Chat socket closed unexpectedly');
    };

      const messageInputDom = document.querySelector('#chat-message-input');
      const message = messageInputDom.value;
      const user = this.user;
      this.chatSocket.send(JSON.stringify({
        'message': message,
        'username': user
      }));
      messageInputDom.value = '';
    }

  },

}
</script>