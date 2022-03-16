<template>
  <div>

    <textarea id="chat-log" cols="100" rows="20"></textarea><br>
    <input id="chat-message-input" ref="message_input" @keyup.enter="submitMessage" type="text" size="100"><br>
    <input id="chat-message-submit" @click="submitMessage" type="button" value="Send">
  </div>

</template>

<script>
export default {
  name: 'ChatRoom',
  data() {
    return {
      roomName: '',
      user: 'user',
      chatSocket: '',
    }

  },
  async mounted() {
    this.$refs.message_input.focus();

    console.log(this.roomName);

    this.chatSocket = new WebSocket('ws://127.0.0.1:8000' + '/ws' + this.roomName + '/');

    this.chatSocket.onmessage = function (e) {
      const data = JSON.parse(e.data);
      document.querySelector('#chat-log').value += (data.message + '\n');
    };

    this.chatSocket.onclose = function (e) {
      console.error('Chat socket closed unexpectedly');
    };

  },
  created() {
    this.roomName = this.$store.state.room
  },
  methods: {
    submitMessage() {
      const messageInputDom = document.querySelector('#chat-message-input');
      const message = messageInputDom.value;
      console.log(this.chatSocket);
      this.chatSocket.send(JSON.stringify({
        'message': message
      }));
      messageInputDom.value = '';
    }
  }
}
</script>
