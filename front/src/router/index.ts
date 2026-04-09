// src/router/index.js
import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/Login.vue";

const routes = [
  {
    path: "/",
    redirect: "/login"
  },
  {
    path: "/login",
    name: "Login",
    component: Login
  },
  {
    path: "/admin",
    component: () => import("../layouts/sidebar.vue"),
    meta: { requiresAuth: true },
    children: [
      { 
        path: "dashboard", 
        name: "Dashboard",
        component: () => import("../views/Dashboard.vue") 
      },
      { 
        path: "", 
        redirect: "/admin/dashboard" 
      }
    ]
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  
  const user = localStorage.getItem('user');
  const isAuthenticated = user !== null;
  
  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/login');
  } 

  else if (to.path === '/login' && isAuthenticated) {
    next('/admin/dashboard');
  } 
  else {
    next();
  }
});

export default router;