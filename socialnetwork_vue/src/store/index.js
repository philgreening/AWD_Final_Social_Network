import { createStore } from 'vuex'

export default createStore({
  state: {
    isAuthenticated: false,
    token: '',
    user:{
      id: '',
      username: ''
    },
    
  },
  getters: {
  },
  mutations: {
    // initialises store on application start
    initializeStore(state) {
      
      if (localStorage.getItem('token')) {
          state.token = localStorage.getItem('token')
          state.isAuthenticated = true
          state.user.id = localStorage.getItem('userid')
          state.user.username = localStorage.getItem('username')
          
      } else {
          state.token = ''
          state.isAuthenticated = false
          state.user.id = 0
          state.user.username = ''
      } 
    },
    // sets the authentication state
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
    },
    // clears the authentication state 
    removeToken(state) {
        state.token = ''
        state.isAuthenticated = false
    },
    // stores current username for session
    setUser(state, user) {
      state.user = user
    }
  },
  actions: {
  },
  modules: {
  }
})
