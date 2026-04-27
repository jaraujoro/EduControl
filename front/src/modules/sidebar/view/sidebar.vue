<template>
  <!-- Overlay móvil -->
  <div
    v-if="isMobileMenuOpen"
    @click="$emit('closeMobile')"
    class="fixed inset-0 bg-black bg-opacity-50 z-20 lg:hidden transition-opacity duration-300"
  ></div>

  <!-- Sidebar -->
  <aside
    :class="[
      'fixed left-0 top-0 h-full bg-gradient-to-br from-[#1e3c72] to-[#2a5298] transition-all duration-300 z-30 shadow-xl',
      isCollapsed ? 'w-20' : 'w-64',
      isMobileMenuOpen
        ? 'translate-x-0'
        : '-translate-x-full lg:translate-x-0',
    ]"
  >
    <!-- Menú -->
    <nav class="mt-4 px-2">
      <div v-for="item in menuItems" :key="item.path">

        <!-- ITEM -->
        <div
          @click="item.children && item.children.length ? toggleMenu(item.path) : navigate(item.path)"
          :class="[
            'flex items-center px-3 py-3 mb-1 rounded-lg cursor-pointer transition-all',
            isActive(item.path)
              ? 'bg-white/20 text-white shadow-md'
              : 'text-white/70 hover:bg-white/10 hover:text-white',
          ]"
        >
          <component
            v-if="Icons[item.icon]"
            :is="Icons[item.icon]"
            class="w-5 h-5"
          />

          <span v-if="!isCollapsed" class="ml-3 text-xs font-medium flex-1">
            {{ item.title }}
          </span>

          <!-- Flecha -->
          <svg
            v-if="item.children && item.children.length && !isCollapsed"
            :class="[
              'w-4 h-4 transition-transform',
              openMenus[item.path] ? 'rotate-90' : '',
            ]"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M9 5l7 7-7 7"/>
          </svg>
        </div>

        <!-- SUBMENU -->
        <div
          v-if="item.children && openMenus[item.path] && !isCollapsed"
          class="ml-6"
        >
          <div
            v-for="child in item.children"
            :key="child.path"
            @click="navigate(child.path)"
            :class="[
              'flex items-center px-3 py-2 mb-1 rounded-lg cursor-pointer text-xs transition-all',
              isActive(child.path)
                ? 'bg-white/20 text-white'
                : 'text-white/70 hover:bg-white/10 hover:text-white',
            ]"
          >
            <component
              v-if="Icons[child.icon]"
              :is="Icons[child.icon]"
              class="w-4 h-4"
            />
            <span class="ml-3">{{ child.title }}</span>
          </div>
        </div>

      </div>
    </nav>

    <!-- BOTÓN COLAPSAR -->
    <button
      v-if="!isMobile"
      @click="$emit('toggleSidebar')"
      class="absolute bottom-4 left-1/2 -translate-x-1/2 p-2 rounded-lg bg-white/10 text-white hover:bg-white/20 transition-all"
    >
      <svg
        v-if="!isCollapsed"
        class="w-4 h-4"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
      >
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
          d="M15 19l-7-7 7-7"/>
      </svg>

      <svg
        v-else
        class="w-4 h-4"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
      >
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
          d="M9 5l7 7-7 7"/>
      </svg>
    </button>
  </aside>
</template>

<script setup>
import * as Icons from "@heroicons/vue/24/outline";
import { ref, onMounted, watch } from "vue";
import { useRouter, useRoute } from "vue-router";
import { list_menu } from "../api/sidebar.ts";

/* PROPS */
defineProps({
  isCollapsed: Boolean,
  isMobileMenuOpen: Boolean,
  isMobile: Boolean,
});

/* EMITS */
defineEmits(["closeMobile", "toggleSidebar"]);

/* ROUTER */
const router = useRouter();
const route = useRoute();

/* STATE */
const menuItems = ref([]);
const openMenus = ref({});

/* NAVIGATION */
const navigate = (path) => {
  if (!path.startsWith("/")) path = "/" + path;
  router.push(path);
};

/* ACTIVE */
const isActive = (path) => {
  if (!path) return false;
  return route.path.startsWith("/" + path);
};

/* TOGGLE */
const toggleMenu = (path) => {
  openMenus.value[path] = !openMenus.value[path];
};

/* OPEN ACTIVE */
const openActiveMenu = () => {
  const currentPath = route.path;

  menuItems.value.forEach((item) => {
    if (item.children) {
      const found = item.children.find((child) =>
        currentPath.startsWith("/" + child.path)
      );

      if (found) openMenus.value[item.path] = true;
    }
  });
};

/* LOAD MENU */
const loadMenu = async () => {
  try {
    const res = await list_menu();
    menuItems.value = res.data;
    openActiveMenu();
  } catch (error) {
    console.error("Error cargando menú", error);
  }
};

/* WATCH ROUTE */
watch(route, () => {
  openActiveMenu();
});

/* INIT */
onMounted(() => {
  loadMenu();
});
</script>