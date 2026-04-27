<template>
    <div class="bg-gray-50 min-h-screen flex flex-col">
        <!-- Header -->
        <div class="bg-white border-b border-gray-200 px-4 md:px-6 py-4 sticky top-0 z-10">
            <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-3">
                <div>
                    <h1 class="text-lg md:text-xl font-semibold text-gray-800">
                        Gestión de Módulos
                    </h1>
                    <p class="text-xs md:text-sm text-gray-500 mt-0.5">
                        Administra la estructura de menús y navegación del sistema
                    </p>
                </div>

                <button @click="openModal(null)"
                    class="w-full md:w-auto inline-flex justify-center items-center gap-2 px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white text-sm font-medium rounded-lg shadow-sm transition-all duration-200">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" />
                    </svg>
                    Nuevo Módulo
                </button>
            </div>
        </div>

        <!-- Contenido principal -->
        <div class="flex-1 px-4 md:px-6 py-4 md:py-6">
            <!-- Tarjeta de estadísticas -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
                <div class="bg-white rounded-xl border border-gray-200 p-4 shadow-sm">
                    <div class="flex items-center justify-between">
                        <div>
                            <p class="text-sm text-gray-500">Total Módulos</p>
                            <p class="text-2xl font-bold text-gray-800">12</p>
                        </div>
                        <div class="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center">
                            <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 10h16M4 14h16M4 18h16" />
                            </svg>
                        </div>
                    </div>
                </div>
                <div class="bg-white rounded-xl border border-gray-200 p-4 shadow-sm">
                    <div class="flex items-center justify-between">
                        <div>
                            <p class="text-sm text-gray-500">Módulos Activos</p>
                            <p class="text-2xl font-bold text-green-600">10</p>
                        </div>
                        <div class="w-10 h-10 bg-green-100 rounded-lg flex items-center justify-center">
                            <svg class="w-5 h-5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                            </svg>
                        </div>
                    </div>
                </div>
                <div class="bg-white rounded-xl border border-gray-200 p-4 shadow-sm">
                    <div class="flex items-center justify-between">
                        <div>
                            <p class="text-sm text-gray-500">Módulos Padre</p>
                            <p class="text-2xl font-bold text-purple-600">5</p>
                        </div>
                        <div class="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center">
                            <svg class="w-5 h-5 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z" />
                            </svg>
                        </div>
                    </div>
                </div>
                <div class="bg-white rounded-xl border border-gray-200 p-4 shadow-sm">
                    <div class="flex items-center justify-between">
                        <div>
                            <p class="text-sm text-gray-500">Submódulos</p>
                            <p class="text-2xl font-bold text-orange-600">7</p>
                        </div>
                        <div class="w-10 h-10 bg-orange-100 rounded-lg flex items-center justify-center">
                            <svg class="w-5 h-5 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7v8a2 2 0 002 2h6M8 7V5a2 2 0 012-2h4.586a1 1 0 01.707.293l4.414 4.414a1 1 0 01.293.707V15a2 2 0 01-2 2h-2M8 7H6a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2v-2" />
                            </svg>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Vista de árbol / Tabla -->
            <div class="bg-white rounded-xl border border-gray-200 shadow-sm overflow-hidden">
                <!-- Barra de búsqueda y filtros -->
                <div class="p-4 border-b border-gray-200 bg-gray-50">
                    <div class="flex flex-col sm:flex-row gap-3">
                        <div class="flex-1 relative">
                            <svg class="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                            </svg>
                            <input type="text" v-model="searchTerm" placeholder="Buscar módulo por nombre o ruta..."
                                class="w-full pl-9 pr-4 py-2 text-sm border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500" />
                        </div>
                        <div class="flex gap-2">
                            <button @click="expandAll" class="px-3 py-2 text-sm text-gray-600 hover:text-blue-600 border border-gray-300 rounded-lg hover:bg-white transition-colors">
                                Expandir todo
                            </button>
                            <button @click="collapseAll" class="px-3 py-2 text-sm text-gray-600 hover:text-blue-600 border border-gray-300 rounded-lg hover:bg-white transition-colors">
                                Colapsar todo
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Vista de árbol jerárquica -->
                <div class="overflow-x-auto">
                    <div class="min-w-[800px] divide-y divide-gray-100">
                        <!-- Módulos padres -->
                        <div v-for="module in treeModules" :key="module.id" class="hover:bg-gray-50 transition-colors">
                            <!-- Módulo padre -->
                            <div class="flex items-center px-4 md:px-6 py-4">
                                <!-- Botón expandir/colapsar -->
                                <button @click="toggleExpand(module)" class="mr-3 text-gray-400 hover:text-gray-600">
                                    <svg class="w-4 h-4 transition-transform" :class="{ 'rotate-90': module.expanded }" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                                    </svg>
                                </button>

                                <!-- Icono del módulo -->
                                <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-blue-500 to-blue-600 flex items-center justify-center text-white text-xs mr-3 shadow-sm">
                                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z" />
                                    </svg>
                                </div>

                                <!-- Información -->
                                <div class="flex-1 grid grid-cols-12 gap-4 items-center">
                                    <div class="col-span-3">
                                        <p class="text-sm font-medium text-gray-900">{{ module.titulo }}</p>
                                        <p class="text-xs text-gray-400 mt-0.5">ID: {{ module.id }}</p>
                                    </div>
                                    <div class="col-span-3">
                                        <p class="text-sm text-gray-600 font-mono">{{ module.ruta || '—' }}</p>
                                    </div>
                                    <div class="col-span-2">
                                        <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium"
                                            :class="module.activo ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-600'">
                                            <span :class="module.activo ? 'bg-green-500' : 'bg-gray-400'" class="w-1.5 h-1.5 rounded-full"></span>
                                            {{ module.activo ? 'Activo' : 'Inactivo' }}
                                        </span>
                                    </div>
                                    <div class="col-span-2">
                                        <span class="text-xs text-gray-500 bg-gray-100 px-2 py-1 rounded">Orden: {{ module.orden }}</span>
                                    </div>
                                    <div class="col-span-2 text-right">
                                        <div class="flex justify-end gap-2">
                                            <button @click="openModal(module)" class="text-xs font-medium text-gray-600 hover:text-blue-600 px-3 py-1.5 rounded-md hover:bg-blue-50 transition-all">
                                                Editar
                                            </button>
                                            <button @click="confirmDelete(module)" class="text-xs font-medium text-gray-600 hover:text-red-600 px-3 py-1.5 rounded-md hover:bg-red-50 transition-all">
                                                Eliminar
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- Submódulos -->
                            <transition name="fade">
                                <div v-if="module.children?.length && module.expanded" class="bg-gray-50 border-t border-gray-100">
                                    <div v-for="child in module.children" :key="child.id" class="flex items-center px-4 md:px-6 py-3 pl-12 md:pl-16 hover:bg-gray-100 transition-colors">
                                        <!-- Línea de conexión visual -->
                                        <div class="relative mr-4">
                                            <div class="absolute left-0 top-1/2 w-4 h-px bg-gray-300"></div>
                                        </div>

                                        <!-- Icono submódulo -->
                                        <div class="w-7 h-7 rounded-lg bg-gradient-to-br from-gray-400 to-gray-500 flex items-center justify-center text-white text-xs mr-3 shadow-sm">
                                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="=" />
                                            </svg>
                                        </div>

                                        <!-- Información submódulo -->
                                        <div class="flex-1 grid grid-cols-12 gap-4 items-center">
                                            <div class="col-span-3">
                                                <p class="text-sm font-medium text-gray-800">{{ child.titulo }}</p>
                                            </div>
                                            <div class="col-span-3">
                                                <p class="text-sm text-gray-500 font-mono">{{ child.ruta || '—' }}</p>
                                            </div>
                                            <div class="col-span-2">
                                                <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium"
                                                    :class="child.activo ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-600'">
                                                    <span :class="child.activo ? 'bg-green-500' : 'bg-gray-400'" class="w-1.5 h-1.5 rounded-full"></span>
                                                    {{ child.activo ? 'Activo' : 'Inactivo' }}
                                                </span>
                                            </div>
                                            <div class="col-span-2">
                                                <span class="text-xs text-gray-500 bg-gray-100 px-2 py-1 rounded">Orden: {{ child.orden }}</span>
                                            </div>
                                            <div class="col-span-2 text-right">
                                                <div class="flex justify-end gap-2">
                                                    <button @click="openModal(child)" class="text-xs font-medium text-gray-600 hover:text-blue-600 px-3 py-1.5 rounded-md hover:bg-blue-50 transition-all">
                                                        Editar
                                                    </button>
                                                    <button @click="confirmDelete(child)" class="text-xs font-medium text-gray-600 hover:text-red-600 px-3 py-1.5 rounded-md hover:bg-red-50 transition-all">
                                                        Eliminar
                                                    </button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </transition>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Modal para crear/editar módulo -->
        <div v-if="showModal" class="fixed inset-0 z-50 overflow-y-auto">
            <div class="fixed inset-0 bg-black/50 backdrop-blur-sm" @click="btnCerrarModal"></div>

            <div class="flex min-h-full items-center justify-center p-4">
                <div class="relative bg-white w-full max-w-2xl rounded-xl shadow-2xl flex flex-col max-h-[90vh]">
                    <!-- Header -->
                    <div class="flex items-center justify-between px-6 py-4 border-b border-gray-200 bg-gradient-to-r from-gray-50 to-white rounded-t-xl">
                        <div>
                            <h3 class="text-lg font-semibold text-gray-800">
                                {{ selectedModule?.id ? "Actualizar Módulo" : "Crear Nuevo Módulo" }}
                            </h3>
                            <p class="text-sm text-gray-500">
                                {{ selectedModule?.id ? "Modifica la configuración del módulo" : "Ingresa los datos del nuevo módulo" }}
                            </p>
                        </div>
                        <button @click="btnCerrarModal" class="text-gray-400 hover:text-gray-600 transition-colors p-1 rounded-lg hover:bg-gray-100 text-2xl">
                            ×
                        </button>
                    </div>

                    <!-- Body -->
                    <div class="flex-1 overflow-y-auto p-6">
                        <div class="space-y-5 max-w-2xl mx-auto">
                            <!-- Nombre del módulo -->
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-1">
                                    Título del módulo <span class="text-red-500">*</span>
                                </label>
                                <input v-model="selectedModule.titulo" type="text"
                                    class="w-full px-3 py-2 text-sm border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all"
                                    placeholder="Ej: Usuarios, Cursos, Configuración" />
                            </div>

                            <!-- Ruta y Orden en grid -->
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-1">
                                        Ruta del módulo
                                    </label>
                                    <input v-model="selectedModule.ruta" type="text"
                                        class="w-full px-3 py-2 text-sm border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 font-mono"
                                        placeholder="Ej: /usuarios/list" />
                                    <p class="text-xs text-gray-400 mt-1">Ruta de navegación (ej: /modulo/submodulo)</p>
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-1">
                                        Orden <span class="text-red-500">*</span>
                                    </label>
                                    <input v-model.number="selectedModule.orden" type="number"
                                        class="w-full px-3 py-2 text-sm border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                                        placeholder="0" />
                                </div>
                            </div>

                            <!-- Icono y Estado -->
                            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-1">
                                        Icono
                                    </label>
                                    <select v-model="selectedModule.icono"
                                        class="w-full px-3 py-2 text-sm border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white">
                                        <option value="FolderIcon">📁 Carpeta</option>
                                        <option value="UsersIcon">👥 Usuarios</option>
                                        <option value="BookOpenIcon">📖 Cursos</option>
                                        <option value="CogIcon">⚙️ Configuración</option>
                                        <option value="ChartBarIcon">📊 Reportes</option>
                                        <option value="ListBulletIcon">📋 Lista</option>
                                        <option value="PlusIcon">➕ Crear</option>
                                        <option value="HomeIcon">🏠 Inicio</option>
                                    </select>
                                </div>
                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-1">
                                        Estado
                                    </label>
                                    <select v-model="selectedModule.activo"
                                        class="w-full px-3 py-2 text-sm border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white">
                                        <option :value="true">✅ Activo</option>
                                        <option :value="false">❌ Inactivo</option>
                                    </select>
                                </div>
                            </div>

                            <!-- Módulo padre -->
                            <div>
                                <label class="block text-sm font-medium text-gray-700 mb-1">
                                    Módulo padre
                                </label>
                                <select v-model="selectedModule.padre_id"
                                    class="w-full px-3 py-2 text-sm border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white">
                                    <option :value="null">(Ninguno - Módulo principal)</option>
                                    <option v-for="module in parentModules" :key="module.id" :value="module.id" :disabled="module.id === selectedModule?.id">
                                        {{ module.titulo }} (ID: {{ module.id }})
                                    </option>
                                </select>
                                <p class="text-xs text-gray-400 mt-1">Dejar vacío para módulo principal</p>
                            </div>

                            <!-- Vista previa del icono -->
                            <div class="bg-gray-50 rounded-lg p-4 border border-gray-200">
                                <p class="text-xs font-medium text-gray-500 uppercase tracking-wider mb-2">Vista previa</p>
                                <div class="flex items-center gap-3">
                                    <div class="w-10 h-10 rounded-lg bg-gradient-to-br from-blue-500 to-blue-600 flex items-center justify-center text-white shadow-sm">
                                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z" />
                                        </svg>
                                    </div>
                                    <div>
                                        <p class="text-sm font-medium text-gray-900">{{ selectedModule.titulo || 'Nombre del módulo' }}</p>
                                        <p class="text-xs text-gray-500 font-mono">{{ selectedModule.ruta || '/ruta/ejemplo' }}</p>
                                    </div>
                                    <span class="ml-auto text-xs text-gray-400">Orden: {{ selectedModule.orden || 0 }}</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Footer -->
                    <div class="flex flex-col sm:flex-row justify-end gap-3 px-6 py-4 border-t border-gray-200 bg-gray-50 rounded-b-xl">
                        <button @click="btnCerrarModal"
                            class="px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors">
                            Cancelar
                        </button>
                        <button @click="btnConfirmar"
                            class="px-6 py-2 text-sm font-medium text-white bg-blue-600 rounded-lg hover:bg-blue-700 transition-colors shadow-sm">
                            {{ selectedModule?.id ? "Actualizar" : "Crear" }}
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, computed } from "vue";

// Interfaces
interface Module {
    id: number;
    titulo: string;
    ruta: string | null;
    icono: string;
    orden: number;
    activo: boolean;
    padre_id: number | null;
    expanded?: boolean;
    children?: Module[];
}

// Datos de ejemplo (simulando la estructura de tu DB)
const modulesData = ref<Module[]>([
    {
        id: 1,
        titulo: "Dashboard",
        ruta: "/dashboard",
        icono: "HomeIcon",
        orden: 1,
        activo: true,
        padre_id: null,
        expanded: true,
    },
    {
        id: 2,
        titulo: "Usuarios",
        ruta: "/usuarios",
        icono: "UsersIcon",
        orden: 2,
        activo: true,
        padre_id: null,
        expanded: true,
        children: [
            {
                id: 5,
                titulo: "Lista Usuarios",
                ruta: "/usuarios/list",
                icono: "ListBulletIcon",
                orden: 1,
                activo: true,
                padre_id: 2,
            },
            {
                id: 6,
                titulo: "Crear Usuario",
                ruta: "/usuarios/create",
                icono: "PlusIcon",
                orden: 2,
                activo: true,
                padre_id: 2,
            },
        ],
    },
    {
        id: 3,
        titulo: "Cursos",
        ruta: "/cursos",
        icono: "BookOpenIcon",
        orden: 3,
        activo: true,
        padre_id: null,
        expanded: true,
        children: [
            {
                id: 7,
                titulo: "Lista Cursos",
                ruta: "/cursos/list",
                icono: "ListBulletIcon",
                orden: 1,
                activo: true,
                padre_id: 3,
            },
            {
                id: 8,
                titulo: "Crear Curso",
                ruta: "/cursos/create",
                icono: "PlusIcon",
                orden: 2,
                activo: false,
                padre_id: 3,
            },
        ],
    },
    {
        id: 4,
        titulo: "Configuración",
        ruta: "/configuracion",
        icono: "CogIcon",
        orden: 4,
        activo: true,
        padre_id: null,
        expanded: false,
        children: [
            {
                id: 9,
                titulo: "Permisos",
                ruta: "/configuracion/permisos",
                icono: "ListBulletIcon",
                orden: 1,
                activo: true,
                padre_id: 4,
            },
            {
                id: 10,
                titulo: "Permisos de Rol",
                ruta: "/configuracion/permisos-rol",
                icono: "ListBulletIcon",
                orden: 2,
                activo: true,
                padre_id: 9,
            },
        ],
    },
]);

const showModal = ref(false);
const selectedModule = ref<any>(null);
const searchTerm = ref("");

// Construir árbol jerárquico
const buildTree = (modules: Module[]): Module[] => {
    const map = new Map<number, Module>();
    const roots: Module[] = [];

    modules.forEach(module => {
        map.set(module.id, { ...module, children: [], expanded: module.expanded || false });
    });

    modules.forEach(module => {
        const node = map.get(module.id);
        if (module.padre_id && map.has(module.padre_id)) {
            const parent = map.get(module.padre_id);
            if (parent && node) {
                parent.children = parent.children || [];
                parent.children.push(node);
            }
        } else if (node) {
            roots.push(node);
        }
    });

    // Ordenar por orden
    const sortByOrder = (items: Module[]) => {
        items.sort((a, b) => a.orden - b.orden);
        items.forEach(item => {
            if (item.children?.length) sortByOrder(item.children);
        });
    };
    sortByOrder(roots);

    return roots;
};

// Módulos con estructura de árbol
const treeModules = computed(() => buildTree(modulesData.value));

// Filtrar módulos por búsqueda

// Módulos padres para el select
const parentModules = computed(() => {
    return modulesData.value.filter(m => !m.padre_id);
});

// Expandir/colapsar
const toggleExpand = (module: Module) => {
    module.expanded = !module.expanded;
};

const expandAll = () => {
    const expandRecursive = (modules: Module[]) => {
        modules.forEach(module => {
            module.expanded = true;
            if (module.children?.length) expandRecursive(module.children);
        });
    };
    expandRecursive(treeModules.value);
};

const collapseAll = () => {
    const collapseRecursive = (modules: Module[]) => {
        modules.forEach(module => {
            module.expanded = false;
            if (module.children?.length) collapseRecursive(module.children);
        });
    };
    collapseRecursive(treeModules.value);
};

// Abrir modal
const openModal = (module: Module | null) => {
    if (module) {
        selectedModule.value = { ...module };
    } else {
        selectedModule.value = {
            titulo: "",
            ruta: null,
            icono: "FolderIcon",
            orden: 0,
            activo: true,
            padre_id: null,
        };
    }
    showModal.value = true;
};

// Confirmar eliminación
const confirmDelete = (module: Module) => {
    // Simular SweetAlert (en tu proyecto real usa sweetalert2)
    if (confirm(`¿Eliminar el módulo "${module.titulo}"?`)) {
        console.log("Eliminar módulo:", module);
    }
};

// Cerrar modal
const btnCerrarModal = () => {
    showModal.value = false;
    selectedModule.value = null;
};

// Confirmar guardado
const btnConfirmar = () => {
    if (!selectedModule.value.titulo?.trim()) {
        alert("El título del módulo es obligatorio");
        return;
    }

    if (selectedModule.value.id) {
        // Actualizar
        const index = modulesData.value.findIndex(m => m.id === selectedModule.value.id);
        if (index !== -1) {
            modulesData.value[index] = { ...selectedModule.value };
        }
    } else {
        // Crear
        const newId = Math.max(...modulesData.value.map(m => m.id), 0) + 1;
        modulesData.value.push({
            ...selectedModule.value,
            id: newId,
        });
    }

    btnCerrarModal();
    // Recargar vista (en proyecto real refrescar desde API)
};
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: all 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
    transform: translateY(-10px);
}
</style>