import { createStore } from 'vuex'

export default createStore({
  state: {
    isAuthenticated: false,
    token: '',
    user:{
      id: '',
      username: ''
    },
    room: ''
    
  },
  getters: {
  },
  mutations: {
    initializeStore(state) {
      
      if (localStorage.getItem('token')) {
          state.token = localStorage.getItem('token')
          state.isAuthenticated = true
          state.user.id = localStorage.getItem('userid')
          state.user.username = localStorage.getItem('username')
          state.room = null
      } else {
          state.token = ''
          state.isAuthenticated = false
          state.user.id = 0
          state.user.username = ''
          state.room = ''
      } 
    },
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
    },  
    removeToken(state) {
        state.token = ''
        state.isAuthenticated = false
    },
    setUser(state, user) {
      state.user = user
    },
    setChatRoom(state, room){
      state.room = room
    }
  },
  actions: {
  },
  modules: {
  }
})
