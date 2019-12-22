import Vue from 'vue'
import Router from 'vue-router'
import home from './views/home.vue'
// import home from './views/home.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: home
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/about.vue')
    },
    {
      path: '/contact',
      name: 'contact',
      component: () => import(/* webpackChunkName: "about" */ './views/contact.vue')
    },
    {
      path: '/programs',
      name: 'programs',
      component: () => import(/* webpackChunkName: "about" */ './views/programs.vue')
    },{
      path: '/blogs',
      name: 'blogs',
      component: () => import(/* webpackChunkName: "about" */ './views/blogs.vue')
    }
  ]
})
