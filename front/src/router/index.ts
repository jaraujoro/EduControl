import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/login",
    name: "Login",
    component: () => import("../modules/auth/view/login.vue"),
  },
  {
    path: "/",
    component: () => import("../core/layout/AdminLayout.vue"),
    meta: { requiresAuth: true },
    children: [
      {
        path: "",
        redirect: "/dashboard",
      },
      {
        path: "dashboard",
        name: "Dashboard",
        component: () => import("../modules/dashboard/view/dashboard.vue"),
      },
      {
        path: "permisos/permisos-rol",
        name: "Permisos de rol",
        component: () => import("../modules/permisos/view/permisos-rol.vue"),
      },
    ],
  },

  {
    path: "/:pathMatch(.*)*",
    redirect: "/login",
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const auth = JSON.parse(localStorage.getItem("auth") || "{}");
  const token = auth.token;
  const isLogin = to.path === "/login";
  if (!token && !isLogin) {
    return next("/login");
  }
  if (token && isLogin) {
    return next("/dashboard");
  }
  next();
});

export default router;
