<template>
  <div class="min-h-screen flex justify-center items-center p-4 bg-gradient-to-br from-[#1e3c72] to-[#2a5298]">
    <div class="w-full max-w-[450px] bg-white rounded-2xl shadow-xl overflow-hidden animate-fadeIn">
      <!-- Logo y título -->
      <div class="text-center py-8 px-6 bg-white">
        <div
          class="w-[70px] h-[70px] mx-auto mb-4 bg-gradient-to-br from-[#1e3c72] to-[#2a5298] rounded-full flex items-center justify-center">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-10 h-10 text-white">
            <path
              d="M12 3L1 9l11 6 11-6-11-6zm0 11.5L3.5 10.5 12 15l8.5-4.5L12 14.5zm0 5L3.5 15.5 12 20l8.5-4.5L12 19.5z" />
          </svg>
        </div>
        <h2 class="text-2xl text-gray-800 mb-1">Sistema Educativo</h2>
        <p class="text-sm text-gray-500">Acceso al Sistema</p>
      </div>

      <!-- Formulario -->
      <form @submit.prevent="handleLogin" class="px-6 pb-6">
        <!-- Campo Usuario -->
        <div class="mb-5">
          <label class="block text-sm font-medium text-gray-700 mb-2">Usuario / Email</label>
          <div class="relative flex items-center">
            <svg class="absolute left-3 w-[18px] h-[18px] text-gray-400 pointer-events-none"
              xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
              <path d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" />
            </svg>
            <input v-model="form.username" type="text" placeholder="usuario@educacion.edu" :class="[
              'w-full pl-10 pr-3 py-3 border-2 rounded-xl text-sm outline-none transition-all bg-white',
              errors.username ? 'border-red-500' : 'border-gray-200 focus:border-blue-500 focus:ring-2 focus:ring-blue-500/10'
            ]" />
          </div>
          <span v-if="errors.username" class="block text-xs text-red-500 mt-1">{{ errors.username }}</span>
        </div>

        <!-- Campo Contraseña -->
        <div class="mb-5">
          <label class="block text-sm font-medium text-gray-700 mb-2">Contraseña</label>
          <div class="relative flex items-center">
            <svg class="absolute left-3 w-[18px] h-[18px] text-gray-400 pointer-events-none"
              xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd"
                d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z"
                clip-rule="evenodd" />
            </svg>
            <input :type="showPassword ? 'text' : 'password'" v-model="form.password"
              placeholder="Ingrese su contraseña" :class="[
                'w-full pl-10 pr-10 py-3 border-2 rounded-xl text-sm outline-none transition-all bg-white',
                errors.password ? 'border-red-500' : 'border-gray-200 focus:border-blue-500 focus:ring-2 focus:ring-blue-500/10'
              ]" />
            <button type="button" @click="showPassword = !showPassword" class="absolute right-3 p-0 flex items-center">
              <svg v-if="!showPassword" class="w-[18px] h-[18px] text-gray-400" xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20" fill="currentColor">
                <path d="M10 12a2 2 0 100-4 2 2 0 000 4z" />
                <path fill-rule="evenodd"
                  d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z"
                  clip-rule="evenodd" />
              </svg>
              <svg v-else class="w-[18px] h-[18px] text-gray-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"
                fill="currentColor">
                <path fill-rule="evenodd"
                  d="M3.707 2.293a1 1 0 00-1.414 1.414l14 14a1 1 0 001.414-1.414l-1.473-1.473A10.014 10.014 0 0019.542 10C18.268 5.943 14.478 3 10 3a9.958 9.958 0 00-4.512 1.074l-1.78-1.781zm4.261 4.26l1.514 1.515a2.003 2.003 0 012.45 2.45l1.514 1.514a4 4 0 00-5.478-5.478z"
                  clip-rule="evenodd" />
              </svg>
            </button>
          </div>
          <span v-if="errors.password" class="block text-xs text-red-500 mt-1">{{ errors.password }}</span>
        </div>

        <!-- Opciones -->
        <div class="flex justify-between items-center mb-6 flex-wrap gap-2">
          <label class="flex items-center gap-2 text-sm text-gray-600 cursor-pointer">
            <input type="checkbox" v-model="rememberMe" class="cursor-pointer">
            <span>Recordarme</span>
          </label>
          <a href="#" class="text-sm text-blue-500 hover:opacity-80 transition-opacity">¿Olvidaste tu contraseña?</a>
        </div>

        <!-- Botón Submit -->
        <button type="submit" :disabled="loading"
          class="w-full py-3.5 bg-gradient-to-br from-[#1e3c72] to-[#2a5298] text-white font-semibold rounded-xl transition-all hover:-translate-y-0.5 hover:shadow-lg disabled:opacity-60 disabled:cursor-not-allowed disabled:hover:translate-y-0 flex items-center justify-center gap-2">
          <span v-if="loading"
            class="inline-block w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></span>
          <span v-else>Ingresar</span>
        </button>

        <!-- Alerta de error -->
        <div v-if="errorMessage"
          class="mt-4 p-3 rounded-xl text-sm flex items-center gap-2 bg-red-50 text-red-700 border border-red-200">
          <svg class="w-[18px] h-[18px] flex-shrink-0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"
            fill="currentColor">
            <path fill-rule="evenodd"
              d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
              clip-rule="evenodd" />
          </svg>
          {{ errorMessage }}
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { login_usuario } from "../api/usuario-service";
import { useRouter } from "vue-router";

const router = useRouter();

const form = ref({
  username: "",
  password: ""
});

const errors = ref({ username: "", password: "" });
const loading = ref(false);
const errorMessage = ref("");
const showPassword = ref(false);
const rememberMe = ref(false);

const handleLogin = async () => {
  // Validaciones
  let hasError = false;
  if (!form.value.username) {
    errors.value.username = "El usuario es requerido";
    hasError = true;
  } else {
    errors.value.username = "";
  }

  if (!form.value.password) {
    errors.value.password = "La contraseña es requerida";
    hasError = true;
  } else if (form.value.password.length < 4) {
    errors.value.password = "Mínimo 4 caracteres";
    hasError = true;
  } else {
    errors.value.password = "";
  }

  if (hasError) return;

  loading.value = true;
  errorMessage.value = "";

  try {
    const response = await login_usuario(form.value);
    console.log(response.data);
    console.log(response.data.user)


    if (response.data && response.data.success) {

      const data = response.data.user;

      localStorage.setItem("user", JSON.stringify({
        id: data.id,
        username: data.username,
        email: data.email,
        is_superuser: data.is_superuser,
        is_staff: data.is_staff
      }));

      if (rememberMe.value) {
        localStorage.setItem("saved_user", form.value.username);
      } else {
        localStorage.removeItem("saved_user");
      }

      router.push('/admin/dashboard');

    } else {
      errorMessage.value = "Error al obtener datos del usuario";
    }

  } catch (e: any) {
    errorMessage.value = e.response?.data?.message || "Error al iniciar sesión";
    setTimeout(() => errorMessage.value = "", 3000);
  } finally {
    loading.value = false;
  }

};

// Cargar usuario guardado
const savedUser = localStorage.getItem("saved_user");
if (savedUser) {
  form.value.username = savedUser;
  rememberMe.value = true;
}
</script>

<style scoped>
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fadeIn {
  animation: fadeIn 0.5s ease;
}
</style>