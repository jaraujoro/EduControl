<!-- src/layouts/AdminLayout.vue -->
<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Overlay para móvil -->
    <div 
      v-if="isMobileMenuOpen" 
      @click="closeMobileMenu"
      class="fixed inset-0 bg-black bg-opacity-50 z-20 lg:hidden transition-opacity duration-300"
    ></div>

    <!-- Sidebar -->
    <aside 
      :class="[
        'fixed left-0 top-0 h-full bg-gradient-to-br from-[#1e3c72] to-[#2a5298] transition-all duration-300 z-30 shadow-xl',
        isCollapsed ? 'w-20' : 'w-64',
        // En móvil: se oculta/ muestra con transform
        isMobileMenuOpen ? 'translate-x-0' : '-translate-x-full lg:translate-x-0'
      ]"
    >
      <!-- Logo -->
      <div class="flex items-center justify-center h-16 border-b border-white/10">
        <h2 :class="['text-white font-bold transition-all', isCollapsed ? 'text-sm' : 'text-xl']">
          {{ isCollapsed ? 'SE' : 'Sistema Educativo' }}
        </h2>
      </div>

      <!-- Menú -->
      <nav class="mt-6 px-2">
        <div 
          v-for="item in menuItems" 
          :key="item.path"
          @click="navigate(item.path)"
          :class="[
            'flex items-center px-3 py-3 mb-1 rounded-lg cursor-pointer transition-all',
            isActive(item.path) 
              ? 'bg-white/20 text-white shadow-md' 
              : 'text-white/70 hover:bg-white/10 hover:text-white'
          ]"
        >
          <span class="text-xl">{{ item.icon }}</span>
          <span v-if="!isCollapsed" class="ml-3 text-sm font-medium">{{ item.title }}</span>
        </div>
      </nav>

      <!-- Botón colapsar (solo desktop) -->
      <button 
        v-if="!isMobile"
        @click="toggleSidebar"
        class="absolute bottom-4 left-1/2 -translate-x-1/2 p-2 rounded-lg bg-white/10 text-white hover:bg-white/20 transition-all"
      >
        <svg v-if="!isCollapsed" class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
        </svg>
        <svg v-else class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
        </svg>
      </button>
    </aside>

    <!-- Contenido principal -->
    <div 
      :class="[
        'transition-all duration-300',
        // En desktop: margen según colapso
        isMobile ? 'ml-0' : (isCollapsed ? 'ml-20' : 'ml-64')
      ]"
    >
      <!-- HEADER FIJO -->
      <header class="bg-white shadow-sm sticky top-0 z-20">
        <div class="flex justify-between items-center px-4 md:px-6 h-16">
          <div class="flex items-center gap-4">
            <!-- Botón menú hamburguesa (solo móvil) -->
            <button @click="toggleMobileMenu" class="lg:hidden text-gray-600 p-2 hover:bg-gray-100 rounded-lg transition-colors">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
              </svg>
            </button>
            
            <!-- Botón colapsar sidebar (solo desktop) -->
            <button @click="toggleSidebar" class="hidden lg:block text-gray-600 hover:bg-gray-100 p-2 rounded-lg transition-colors">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
              </svg>
            </button>
            
            <h1 class="text-lg md:text-xl font-semibold text-gray-800 truncate">{{ pageTitle }}</h1>
          </div>
          
          <div class="flex items-center gap-2 md:gap-4">
            <!-- Usuario -->
            <div class="relative">
              <button @click="showUserMenu = !showUserMenu" class="flex items-center gap-2 md:gap-3 hover:bg-gray-50 px-2 md:px-3 py-2 rounded-lg transition-colors">
                <div class="w-8 h-8 rounded-full bg-gradient-to-r from-[#1e3c72] to-[#2a5298] flex items-center justify-center text-white text-sm font-medium">
                  {{ userInitial }}
                </div>
                <div class="hidden sm:block text-left">
                  <p class="text-sm font-medium text-gray-700">{{ userName }}</p>
                  <p class="text-xs text-gray-500">Administrador</p>
                </div>
              </button>
              
              <!-- Dropdown -->
              <transition enter-active-class="transition duration-200" enter-from-class="opacity-0 -translate-y-2" enter-to-class="opacity-100 translate-y-0" leave-active-class="transition duration-150" leave-from-class="opacity-100 translate-y-0" leave-to-class="opacity-0 -translate-y-2">
                <div v-if="showUserMenu" class="absolute right-0 mt-2 w-56 bg-white rounded-lg shadow-lg border border-gray-100 py-1 z-30">
                  <div class="px-4 py-3 border-b border-gray-100">
                    <p class="text-sm font-medium text-gray-900">{{ userName }}</p>
                    <p class="text-xs text-gray-500 truncate">admin@educacion.edu</p>
                  </div>
                  <button @click="logout" class="w-full text-left px-4 py-2 text-sm text-red-600 hover:bg-red-50 transition-colors flex items-center gap-2">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path>
                    </svg>
                    Cerrar Sesión
                  </button>
                </div>
              </transition>
            </div>
          </div>
        </div>
      </header>

      <!-- CONTENIDO DINÁMICO -->
      <main class="p-4 md:p-6">
        <router-view />
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()
const isCollapsed = ref(false)
const isMobileMenuOpen = ref(false)
const showUserMenu = ref(false)
const isMobile = ref(false)

// Configuración del menú
const menuItems = [
  { path: '/admin/dashboard', title: 'Dashboard', icon: '📊' },
  { path: '/admin/users', title: 'Usuarios', icon: '👥' },
  { path: '/admin/courses', title: 'Cursos', icon: '📚' },
  { path: '/admin/settings', title: 'Configuración', icon: '⚙️' }
]

// Datos del usuario
const userName = ref('Admin')
const userInitial = computed(() => userName.value.charAt(0).toUpperCase())

// El título cambia según la ruta actual
const pageTitle = computed(() => {
  const item = menuItems.find(i => route.path.includes(i.path))
  return item ? item.title : 'Panel de Control'
})

const isActive = (path) => {
  return route.path.includes(path)
}

const navigate = (path) => {
  router.push(path)
  // En móvil, cerrar el menú después de navegar
  if (isMobile.value) {
    closeMobileMenu()
  }
}

const toggleSidebar = () => {
  isCollapsed.value = !isCollapsed.value
}

const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value
}

const closeMobileMenu = () => {
  isMobileMenuOpen.value = false
}

const logout = () => {
  localStorage.removeItem('user')
  router.push('/login')
}

// Detectar si es móvil
const checkMobile = () => {
  isMobile.value = window.innerWidth < 1024 // lg breakpoint
  if (!isMobile.value) {
    closeMobileMenu() // Cerrar menú móvil al pasar a desktop
  }
}

// Cerrar dropdown
const handleClickOutside = (event) => {
  if (!event.target.closest('.relative')) {
    showUserMenu.value = false
  }
}

watch(showUserMenu, (newVal) => {
  if (newVal) {
    document.addEventListener('click', handleClickOutside)
  } else {
    document.removeEventListener('click', handleClickOutside)
  }
})

// Escuchar cambios de tamaño
onMounted(() => {
  checkMobile()
  window.addEventListener('resize', checkMobile)
})

onUnmounted(() => {
  window.removeEventListener('resize', checkMobile)
})
</script>

<style scoped>
/* Asegurar que en móvil el contenido no tenga márgenes extra */
@media (max-width: 1023px) {
  .transition-all {
    transition-property: all;
  }
}
</style>