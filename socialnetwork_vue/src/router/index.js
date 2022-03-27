import { createRouter, createWebHistory } from 'vue-router'
import store from '../store';

// import HomeView from '../views/HomeView.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import Home from '../views/Home.vue'
import UserProfile from '../views/UserProfile.vue'
import EditUserProfile from '../views/EditUserProfile.vue'
import Search from '../views/Search.vue'
import UserFeed from '../views/UserFeed.vue'
import MyFeed from '../views/MyFeed.vue'
import MyProfile from '../views/MyProfile.vue'
import Chat from '../views/Chat.vue'
// import ChatRoom from '../views/ChatRoom.vue'




const routes = [
  // {
  //   path: '/',
  //   name: 'home',
  //   component: HomeView
  // },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/sign-up/',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in/',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/create-profile/',
    name: 'UserProfile',
    component: UserProfile,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/profile/',
    name: 'EditUserProfile',
    component: EditUserProfile,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/search/',
    name: 'Search',
    component: Search,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/user-feed/:user',
    name: 'UserFeed',
    component: UserFeed,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/feed/',
    name: 'MyFeed',
    component: MyFeed,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/my-profile/',
    name: 'MyProfile',
    component: MyProfile,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/chat/',
    name: 'Chat',
    component: Chat,
    meta: {
      requiresAuth: true
    }
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// Checks if login is requred and that user is authenticated
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth) && !store.state.isAuthenticated) {
    next({ name: 'LogIn', query: { to: to.path } });
  } else {
    next()
  }
})

export default router
