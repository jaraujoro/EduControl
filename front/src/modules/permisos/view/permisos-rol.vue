<template>
    <div class="bg-gray-50 flex flex-col">

        <!-- Header -->
        <div class="bg-white border-b border-gray-200 px-4 md:px-6 py-4">
            <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-3">
                <div>
                    <h1 class="text-lg md:text-xl font-semibold text-gray-800">
                        Gestión de Roles
                    </h1>
                    <p class="text-xs md:text-sm text-gray-500 mt-0.5">
                        Administración de permisos y accesos al sistema
                    </p>
                </div>

                <button @click="openModal(null)"
                    class="w-full md:w-auto inline-flex justify-center items-center gap-2 px-4 py-2 bg-blue-500 hover:bg-blue-600 text-white text-sm font-medium rounded-md shadow-sm transition">
                    <component :is="Icons.PlusIcon" class="w-4 h-4" />
                    Nuevo Rol
                </button>
            </div>
        </div>

        <!-- Tabla -->
        <div class="flex-1 px-4 md:px-6 py-4 md:py-6">
            <div class="bg-white rounded-lg border border-gray-200 shadow-sm overflow-hidden">

                <!-- Scroll horizontal en mobile -->
                <div class="overflow-x-auto">
                    <table class="min-w-[700px] w-full">
                        <thead class="bg-gray-50 border-b border-gray-200">
                            <tr>
                                <th class="px-4 md:px-6 py-3 text-left text-xs font-semibold text-gray-600 uppercase">
                                    Rol
                                </th>
                                <th class="px-4 md:px-6 py-3 text-left text-xs font-semibold text-gray-600 uppercase">
                                    Descripción
                                </th>
                                <th class="px-4 md:px-6 py-3 text-left text-xs font-semibold text-gray-600 uppercase">
                                    Estado
                                </th>
                                <th class="px-4 md:px-6 py-3 text-right text-xs font-semibold text-gray-600 uppercase">
                                    Acciones
                                </th>
                            </tr>
                        </thead>

                        <tbody class="divide-y divide-gray-100">
                            <tr v-for="role in roles" :key="role.id" class="hover:bg-gray-50 transition">
                                <td class="px-4 md:px-6 py-4 whitespace-nowrap">
                                    <div class="flex items-center gap-2 md:gap-3">
                                        <div class="w-8 h-8 bg-blue-50 rounded-md flex items-center justify-center">
                                            <component :is="Icons.ShieldCheckIcon" class="w-4 h-4 text-blue-600" />
                                        </div>
                                        <span class="text-sm font-medium text-gray-900">
                                            {{ role.rol_nombre }}
                                        </span>
                                    </div>
                                </td>

                                <td class="px-4 md:px-6 py-4">
                                    <span class="text-sm text-gray-500 line-clamp-1">
                                        {{ role.rol_descripcion || "Sin descripción" }}
                                    </span>
                                </td>

                                <td class="px-4 md:px-6 py-4 whitespace-nowrap">
                                    <span :class="role.rol_activo
                                        ? 'bg-green-100 text-green-800'
                                        : 'bg-gray-100 text-gray-600'"
                                        class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium">

                                        <span :class="role.rol_activo ? 'bg-green-500' : 'bg-gray-400'"
                                            class="w-1.5 h-1.5 rounded-full"></span>

                                        {{ role.rol_activo ? "Activo" : "Inactivo" }}
                                    </span>
                                </td>

                                <td class="px-4 md:px-6 py-4 text-right">
                                    <div class="flex justify-end gap-2">
                                        <button @click="openModal(role)"
                                            class="p-1.5 text-gray-500 hover:text-blue-600 hover:bg-blue-50 rounded-md">
                                            <component :is="Icons.KeyIcon" class="w-4 h-4" />
                                        </button>

                                        <button @click="confirmDelete(role)"
                                            class="p-1.5 text-gray-500 hover:text-red-600 hover:bg-red-50 rounded-md">
                                            <component :is="Icons.TrashIcon" class="w-4 h-4" />
                                        </button>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- Modal corporativo -->
        <div v-if="showModal" class="fixed inset-0 z-50">
            <div class="fixed inset-0 bg-black/50" @click="btnCerrarModal"></div>

            <div class="flex min-h-full items-center justify-center p-4 sm:p-6">
                <div
                    class="relative bg-white w-full h-full sm:h-auto sm:max-w-3xl rounded-none sm:rounded-lg shadow-xl flex flex-col">

                    <!-- Header -->
                    <div
                        class="flex items-center justify-between px-4 sm:px-6 py-4 border-b border-gray-200 bg-gray-50 sm:rounded-t-lg">
                        <div>
                            <h3 class="text-base sm:text-lg font-semibold text-gray-800">
                                {{ selectedRole?.id ? "Editar Rol" : "Crear Nuevo Rol" }}
                            </h3>
                            <p class="text-xs sm:text-sm text-gray-500 mt-0.5">
                                {{
                                    selectedRole?.id
                                        ? "Modifica la configuración del rol"
                                        : "Ingresa los datos del nuevo rol"
                                }}
                            </p>
                        </div>
                        <button @click="btnCerrarModal" class="text-gray-400 hover:text-gray-600 transition-colors">
                            <component :is="Icons.XMarkIcon" class="w-5 h-5" />
                        </button>
                    </div>

                    <!-- Body -->
                    <div class="flex-1 px-4 sm:px-6 py-5 max-h-[70vh] sm:max-h-[75vh] overflow-y-auto">
                        <div class="space-y-5">

                            <!-- Datos básicos -->
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-1">
                                        Nombre del rol <span class="text-red-500">*</span>
                                    </label>
                                    <input v-model="selectedRole.rol_nombre" type="text"
                                        class="w-full px-3 py-2 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors"
                                        placeholder="Ej: Administrador" />
                                </div>

                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-1">
                                        Estado
                                    </label>
                                    <select v-model="selectedRole.rol_activo"
                                        class="w-full px-3 py-2 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors bg-white">
                                        <option :value="true">Activo</option>
                                        <option :value="false">Inactivo</option>
                                    </select>
                                </div>
                            </div>

                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-1">
                                    Descripción
                                </label>
                                <textarea v-model="selectedRole.rol_descripcion" rows="2"
                                    class="w-full px-3 py-2 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors resize-none"
                                    placeholder="Describe las responsabilidades y alcance del rol..."></textarea>
                            </div>

                            <!-- Separador -->
                            <div class="border-t border-gray-200 pt-4">
                                <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between mb-3 gap-2">
                                    <div>
                                        <h4 class="text-sm font-medium text-gray-800">
                                            Permisos y accesos
                                        </h4>
                                        <p class="text-xs text-gray-500 mt-0.5">
                                            Selecciona los menús a los que tendrá acceso este rol
                                        </p>
                                    </div>
                                </div>

                                <div
                                    class="border border-gray-200 rounded-md overflow-hidden max-h-72 sm:max-h-80 overflow-y-auto">
                                    <div v-for="menu in menus" :key="menu.id"
                                        class="border-b border-gray-100 last:border-0">

                                        <!-- Menú padre -->
                                        <div class="flex items-center gap-3 px-3 sm:px-4 py-2.5 hover:bg-gray-50">
                                            <button v-if="menu.children?.length" @click="toggleExpand(menu)"
                                                class="text-gray-500 hover:text-gray-700 transition-transform"
                                                :class="{ 'rotate-90': menu.expanded }">
                                                <component :is="Icons.ChevronRightIcon" class="w-4 h-4" />
                                            </button>
                                            <div v-else class="w-4"></div>

                                            <label class="flex items-center gap-3 cursor-pointer flex-1">
                                                <input type="checkbox" v-model="menu.checked"
                                                    @change="toggleChildren(menu)"
                                                    class="w-4 h-4 rounded border-gray-300 text-blue-600 focus:ring-2 focus:ring-blue-500" />
                                                <span class="text-sm font-medium text-gray-800">
                                                    {{ menu.titulo }}
                                                </span>
                                            </label>
                                        </div>

                                        <!-- Submenús -->
                                        <transition name="fade">
                                            <div v-if="menu.children?.length && menu.expanded"
                                                class="bg-gray-50 pl-10 sm:pl-16 pr-3 sm:pr-4 py-2 relative">

                                                <!-- Línea vertical -->
                                                <div class="absolute left-5 top-0 bottom-0 w-px bg-gray-300"></div>

                                                <div v-for="child in menu.children" :key="child.id"
                                                    class="relative flex items-center gap-3 py-1.5">

                                                    <!-- Línea horizontal tipo └── -->
                                                    <div class="absolute left-5 top-1/2 w-4 h-px bg-gray-300"></div>

                                                    <label class="flex items-center gap-3 cursor-pointer pl-4">
                                                        <input type="checkbox" v-model="child.checked"
                                                            @change="checkParent(menu)"
                                                            class="w-4 h-4 rounded border-gray-300 text-blue-600 focus:ring-2 focus:ring-blue-500" />

                                                        <span class="text-sm text-gray-600">
                                                            {{ child.titulo }}
                                                        </span>
                                                    </label>
                                                </div>
                                            </div>
                                        </transition>

                                    </div>
                                </div>
                            </div>

                        </div>
                    </div>

                    <!-- Footer -->
                    <div
                        class="flex flex-col sm:flex-row justify-end gap-2 sm:gap-3 px-4 sm:px-6 py-4 border-t border-gray-200 bg-gray-50 sm:rounded-b-lg">
                        <button @click="btnCerrarModal"
                            class="w-full sm:w-auto px-4 py-2 text-sm font-medium text-white bg-red-500 border border-gray-300 rounded-md hover:bg-red-600 transition-colors">
                            Cancelar
                        </button>
                        <button @click="btnConfirmar"
                            class="w-full sm:w-auto px-4 py-2 text-sm font-medium text-white bg-blue-500 border border-gray-300 rounded-md hover:bg-blue-600 transition-colors">
                            Confirmar
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import * as Icons from "@heroicons/vue/24/outline";
import { list_rol, list_rol_x_menu, save_rol } from "../api/permisos-rol.ts";
import sweetalert2 from "sweetalert2";

const roles = ref<any[]>([]);
const showModal = ref(false);
const selectedRole = ref<any>(null);
const menus = ref<any[]>([]);
// const searchTerm = ref("");
// const currentPage = ref(1);
// const pageSize = 10;

// const filteredRoles = computed(() => {
//     let filtered = roles.value;
//     if (searchTerm.value) {
//         filtered = filtered.filter(
//             (role) =>
//                 role.rol_nombre
//                     .toLowerCase()
//                     .includes(searchTerm.value.toLowerCase()) ||
//                 role.rol_descripcion
//                     ?.toLowerCase()
//                     .includes(searchTerm.value.toLowerCase()),
//         );
//     }
//     const start = (currentPage.value - 1) * pageSize;
//     return filtered.slice(start, start + pageSize);
// });

const rs_list = async () => {
    const response = await list_rol();
    roles.value = response.data;
};

const openModal = async (role: any) => {
    selectedRole.value = role
        ? { ...role }
        : {
            rol_nombre: "",
            rol_descripcion: "",
            rol_activo: true,
        };
    showModal.value = true;

    const response = await list_rol_x_menu(role?.id || 0);
    menus.value = response.data.map((m: any) => ({
        ...m,
        expanded: false,
    }));
};

const confirmDelete = (role: any) => {
    sweetalert2
        .fire({
            title: "¿Estás seguro?",
            text: `¿Deseas eliminar el rol "${role.rol_nombre}"? Esta acción no se puede deshacer.`,
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#d33",
            cancelButtonColor: "#3085d6",
            confirmButtonText: "Sí, eliminar",
            cancelButtonText: "Cancelar",
        })
        .then((result) => {
            if (result.isConfirmed) {
                // Aquí iría la lógica para eliminar el rol
                sweetalert2.fire(
                    "Eliminado",
                    `El rol "${role.rol_nombre}" ha sido eliminado.`,
                    "success",
                );
            }
        });
};

const btnCerrarModal = () => {
    showModal.value = false;
    selectedRole.value = null;
};

const btnConfirmar = async () => {
    const data = {
        rol: selectedRole.value,
        menus: getSelectedMenus(),
    };
    await save_rol(data);
    await rs_list();
    btnCerrarModal();
};

const toggleExpand = (menu: any) => {
    menu.expanded = !menu.expanded;
};

const toggleChildren = (menu: any) => {
    if (menu.children) {
        menu.children.forEach((c: any) => {
            c.checked = menu.checked;
        });
    }
};

const checkParent = (menu: any) => {
    if (!menu.children) return;
    const hasChecked = menu.children.some((c: any) => c.checked);
    menu.checked = hasChecked;
};

const getSelectedMenus = () => {
    const selected: number[] = [];
    menus.value.forEach((menu: any) => {
        if (menu.checked) selected.push(menu.id);
        if (menu.children) {
            menu.children.forEach((c: any) => {
                if (c.checked) selected.push(c.id);
            });
        }
    });
    return selected;
};

// const getSelectedCount = () => getSelectedMenus().length;

onMounted(() => {
    rs_list();
});

</script>
