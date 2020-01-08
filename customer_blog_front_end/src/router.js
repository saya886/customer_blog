import Vue from 'vue'
import Router from 'vue-router'
import home from './views/home.vue'
// import home from './views/home.vue'

Vue.use(Router)

const scrollBehavior = function (to, from, savedPosition) {
  if (to.hash) {
    return {
      // 通过 to.hash 的值來找到对应的元素
      selector: to.hash
    }
  }else{
    return { x: 0, y: 0 }
  }
}
export default new Router({
  scrollBehavior,
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
    },
    {
      path: '/programs/:program_id',
      name: 'programs',
      component: () => import(/* webpackChunkName: "about" */ './views/program_detail.vue')
    },{
      path: '/blogs',
      name: 'blogs',
      component: () => import(/* webpackChunkName: "about" */ './views/blogs.vue')
    },{
      path: '/blogs/:blog_id',
      name: 'blogs',
      component: () => import(/* webpackChunkName: "about" */ './views/blog_main.vue')
    },{
      path: '/categary/:categary',
      name: 'categary',
      component: () => import(/* webpackChunkName: "about" */ './views/blog_more.vue')
    }
  ]
})
