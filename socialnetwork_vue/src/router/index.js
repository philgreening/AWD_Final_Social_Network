import { createRouter, createWebHistory } from 'vue-router'
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
    component: UserProfile
  },
  {
    path: '/profile/',
    name: 'EditUserProfile',
    component: EditUserProfile
  },
  {
    path: '/search/',
    name: 'Search',
    component: Search
  },
  {
    path: '/user-feed/:user',
    name: 'UserFeed',
    component: UserFeed
  },
  {
    path: '/feed/',
    name: 'MyFeed',
    component: MyFeed
  },
  {
    path: '/my-profile/',
    name: 'MyProfile',
    component: MyProfile
  }



]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
