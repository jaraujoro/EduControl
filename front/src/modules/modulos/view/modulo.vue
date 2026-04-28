<template>
    <div class="bg-gray-50 flex flex-col">
        <!-- Header -->
        <div class="bg-white border-b border-gray-200 px-4 md:px-6 py-4 sticky top-0 z-10 flex-shrink-0">
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
                    <component :is="Icons.PlusIcon" class="w-4 h-4" />
                    Nuevo Módulo
                </button>
            </div>
        </div>

        <!-- Tabla de Módulos -->
        <div class="flex-1 px-4 md:px-6 py-4 md:py-6 overflow-hidden">
            <div class="bg-white rounded-xl border border-gray-200 shadow-sm overflow-hidden h-full flex flex-col">
                <!-- Barra de búsqueda y filtros -->
                <div class="p-4 border-b border-gray-200 bg-gray-50 flex-shrink-0">
                    <div class="flex flex-col sm:flex-row gap-3">
                        <div class="flex-1 relative">
                            <component :is="Icons.MagnifyingGlassIcon"
                                class="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-400" />
                            <input type="text" v-model="searchTerm" placeholder="Buscar módulo por nombre o ruta..."
                                class="w-full pl-9 pr-4 py-2 text-sm border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500" />
                        </div>
                        <div class="flex gap-2">
                            <button @click="expandAll"
                                class="inline-flex items-center gap-1 px-3 py-2 text-sm text-gray-600 hover:text-blue-600 border border-gray-300 rounded-lg hover:bg-white transition-colors">
                                <component :is="Icons.ChevronDoubleDownIcon" class="w-4 h-4" />
                                Expandir todo
                            </button>
                            <button @click="collapseAll"
                                class="inline-flex items-center gap-1 px-3 py-2 text-sm text-gray-600 hover:text-blue-600 border border-gray-300 rounded-lg hover:bg-white transition-colors">
                                <component :is="Icons.ChevronDoubleUpIcon" class="w-4 h-4" />
                                Colapsar todo
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Tabla principal -->
                <div class="overflow-x-auto flex-1">
                    <table class="min-w-[800px] w-full">
                        <thead class="bg-gray-50 border-b border-gray-200 sticky top-0">
                            <tr>
                                <th
                                    class="px-4 md:px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider w-10">
                                </th>
                                <th
                                    class="px-4 md:px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                                    Módulo
                                </th>
                                <th
                                    class="px-4 md:px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                                    Ruta
                                </th>
                                <th
                                    class="px-4 md:px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                                    Estado
                                </th>
                                <th
                                    class="px-4 md:px-6 py-4 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">
                                    Orden
                                </th>
                                <th
                                    class="px-4 md:px-6 py-4 text-center text-xs font-semibold text-gray-600 uppercase tracking-wider">
                                    Acciones
                                </th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-gray-100">
                            <template v-for="module in filteredModules" :key="module.id">
                                <!-- Módulo padre -->
                                <tr class="hover:bg-gray-50 transition-colors">
                                    <td class="px-4 md:px-6 py-4 whitespace-nowrap">
                                        <button v-if="module.children?.length" @click="toggleExpand(module)"
                                            class="text-gray-400 hover:text-gray-600 transition-transform"
                                            :class="{ 'rotate-90': module.expanded }">
                                            <component :is="Icons.ChevronRightIcon" class="w-4 h-4" />
                                        </button>
                                        <div v-else class="w-4"></div>
                                    </td>
                                    <td class="px-4 md:px-6 py-4 whitespace-nowrap">
                                        <div class="flex items-center gap-2 md:gap-3">
                                            <component :is="getIconComponent(module.icono)"
                                                class="w-5 h-5 text-gray-400" />
                                            <span class="text-sm font-medium text-gray-900">
                                                {{ module.titulo }}
                                            </span>
                                        </div>
                                    </td>
                                    <td class="px-4 md:px-6 py-4">
                                        <code class="text-xs text-gray-600 bg-gray-100 px-2 py-1 rounded">
                                            {{ module.ruta || "—" }}
                                        </code>
                                    </td>
                                    <td class="px-4 md:px-6 py-4 whitespace-nowrap">
                                        <span :class="module.activo
                                            ? 'bg-green-100 text-green-800'
                                            : 'bg-gray-100 text-gray-600'
                                            "
                                            class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium">
                                            <span :class="module.activo ? 'bg-green-500' : 'bg-gray-400'"
                                                class="w-1.5 h-1.5 rounded-full"></span>
                                            {{ module.activo ? "Activo" : "Inactivo" }}
                                        </span>
                                    </td>
                                    <td class="px-4 md:px-6 py-4 whitespace-nowrap text-left">
                                        <span class="text-xs text-gray-500 bg-gray-100 px-2 py-1 rounded">
                                            {{ module.orden }}
                                        </span>
                                    </td>
                                    <td class="px-4 md:px-6 py-4 text-center">
                                        <div class="flex justify-center gap-2">
                                            <button @click="openModal(module)"
                                                class="text-xs font-medium text-gray-600 hover:text-blue-600 px-3 py-1.5 rounded-md hover:bg-blue-50 transition-all">
                                                Editar
                                            </button>
                                            <button @click="confirmDelete(module)"
                                                class="text-xs font-medium text-gray-600 hover:text-red-600 px-3 py-1.5 rounded-md hover:bg-red-50 transition-all">
                                                Eliminar
                                            </button>
                                        </div>
                                    </td>
                                </tr>

                                <!-- Submódulos -->
                                <tr v-for="child in (module.expanded ? module.children : [])" :key="child.id"
                                    class="hover:bg-gray-50 transition-colors bg-gray-50/30">
                                    <td class="px-4 md:px-6 py-4 whitespace-nowrap">
                                        <div class="w-4"></div>
                                    </td>
                                    <td class="px-4 md:px-6 py-4 whitespace-nowrap">
                                        <div class="flex items-center gap-2 md:gap-3 pl-6 relative">
                                            <div class="absolute left-0 top-1/2 w-4 h-px bg-gray-300"></div>
                                            <component :is="Icons.DocumentTextIcon" class="w-4 h-4 text-gray-400" />
                                            <span class="text-sm text-gray-700">
                                                {{ child.titulo }}
                                            </span>
                                        </div>
                                    </td>
                                    <td class="px-4 md:px-6 py-4">
                                        <code class="text-xs text-gray-500 bg-gray-100 px-2 py-1 rounded">
                                            {{ child.ruta || "—" }}
                                        </code>
                                    </td>
                                    <td class="px-4 md:px-6 py-4 whitespace-nowrap">
                                        <span :class="child.activo
                                            ? 'bg-green-100 text-green-800'
                                            : 'bg-gray-100 text-gray-600'
                                            "
                                            class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium">
                                            <span :class="child.activo ? 'bg-green-500' : 'bg-gray-400'"
                                                class="w-1.5 h-1.5 rounded-full"></span>
                                            {{ child.activo ? "Activo" : "Inactivo" }}
                                        </span>
                                    </td>
                                    <td class="px-4 md:px-6 py-4 whitespace-nowrap text-left">
                                        <span class="text-xs text-gray-500 bg-gray-100 px-2 py-1 rounded">
                                            {{ child.orden }}
                                        </span>
                                    </td>
                                    <td class="px-4 md:px-6 py-4 text-center">
                                        <div class="flex justify-center gap-2">
                                            <button @click="openModal(child)"
                                                class="text-xs font-medium text-gray-600 hover:text-blue-600 px-3 py-1.5 rounded-md hover:bg-blue-50 transition-all">
                                                Editar
                                            </button>
                                            <button @click="confirmDelete(child)"
                                                class="text-xs font-medium text-gray-600 hover:text-red-600 px-3 py-1.5 rounded-md hover:bg-red-50 transition-all">
                                                Eliminar
                                            </button>
                                        </div>
                                    </td>
                                </tr>
                            </template>

                            <!-- Mensaje sin resultados -->
                            <tr v-if="filteredModules.length === 0">
                                <td colspan="6" class="px-4 md:px-6 py-12 text-center">
                                    <component :is="Icons.FolderOpenIcon"
                                        class="w-12 h-12 mx-auto text-gray-300 mb-4" />
                                    <p class="text-gray-500">No se encontraron módulos</p>
                                    <p class="text-sm text-gray-400 mt-1">Prueba con otros términos de búsqueda</p>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- Modal mejorado -->
        <div v-if="showModal" class="fixed inset-0 z-50 overflow-y-auto">
            <div class="fixed inset-0 bg-black/50 backdrop-blur-sm" @click="btnCerrarModal"></div>

            <div class="flex min-h-full items-center justify-center p-4">
                <div class="relative bg-white w-full max-w-2xl rounded-xl shadow-2xl flex flex-col max-h-[90vh]">
                    <!-- Header -->
                    <div
                        class="flex items-center justify-between px-6 py-4 border-b border-gray-200 bg-gradient-to-r from-gray-50 to-white rounded-t-xl">
                        <div>
                            <h3 class="text-lg font-semibold text-gray-800">
                                {{ selectedModule?.id ? "Actualizar Módulo" : "Crear Nuevo Módulo" }}
                            </h3>
                            <p class="text-sm text-gray-500">
                                {{
                                    selectedModule?.id
                                        ? "Modifica la configuración del módulo"
                                        : "Ingresa los datos del nuevo módulo"
                                }}
                            </p>
                        </div>
                        <button @click="btnCerrarModal"
                            class="text-gray-400 hover:text-gray-600 transition-colors p-1 rounded-lg hover:bg-gray-100">
                            ×
                        </button>
                    </div>

                    <!-- Body con tabs -->
                    <div class="flex-1 overflow-hidden flex flex-col">
                        <!-- Tabs de navegación -->
                        <div class="border-b border-gray-200 px-6">
                            <div class="flex gap-6 overflow-x-auto">
                                <button v-for="tab in tabs" :key="tab.key" @click="activeTab = tab.key" :class="[
                                    'py-3 text-sm font-medium transition-colors relative whitespace-nowrap',
                                    activeTab === tab.key
                                        ? 'text-blue-600'
                                        : 'text-gray-500 hover:text-gray-700',
                                ]">
                                    {{ tab.label }}
                                    <div v-if="activeTab === tab.key"
                                        class="absolute bottom-0 left-0 right-0 h-0.5 bg-blue-600 rounded-full"></div>
                                </button>
                            </div>
                        </div>

                        <div class="flex-1 overflow-y-auto p-6">
                            <!-- Tab: Datos básicos -->
                            <div v-show="activeTab === 'basic'" class="space-y-5 max-w-2xl">
                                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                    <div>
                                        <label class="block text-sm font-medium text-gray-700 mb-1">
                                            Título del módulo <span class="text-red-500">*</span>
                                        </label>
                                        <input v-model="selectedModule.titulo" type="text"
                                            class="w-full px-3 py-2 text-sm border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-all"
                                            placeholder="Ej: Usuarios, Cursos, Configuración" />
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

                                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                                    <div>
                                        <label class="block text-sm font-medium text-gray-700 mb-1">
                                            Ruta del módulo
                                        </label>
                                        <input v-model="selectedModule.ruta" type="text"
                                            class="w-full px-3 py-2 text-sm border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 font-mono"
                                            placeholder="Ej: /usuarios/list" />
                                        <p class="text-xs text-gray-400 mt-1">Ruta de navegación</p>
                                    </div>
                                    <div>
                                        <label class="block text-sm font-medium text-gray-700 mb-1">
                                            Estado
                                        </label>
                                        <select v-model="selectedModule.activo"
                                            class="w-full px-3 py-2 text-sm border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white">
                                            <option :value="true">Activo</option>
                                            <option :value="false">Inactivo</option>
                                        </select>
                                    </div>
                                </div>

                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-1">
                                        Módulo padre
                                    </label>
                                    <select v-model="selectedModule.padre_id"
                                        class="w-full px-3 py-2 text-sm border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white">
                                        <option :value="null">(Ninguno - Módulo principal)</option>
                                        <option v-for="mod in parentModules" :key="mod.id" :value="mod.id"
                                            :disabled="mod.id === selectedModule?.id">
                                            {{ mod.titulo }} (ID: {{ mod.id }})
                                        </option>
                                    </select>
                                    <p class="text-xs text-gray-400 mt-1">Dejar vacío para módulo principal</p>
                                </div>

                                <!-- Vista previa -->
                                <div class="bg-gray-50 rounded-lg p-4 border border-gray-200">
                                    <p class="text-xs font-medium text-gray-500 uppercase tracking-wider mb-2">Vista
                                        previa</p>
                                    <div class="flex items-center gap-3">
                                        <div
                                            class="w-10 h-10 rounded-lg bg-gradient-to-br from-blue-500 to-blue-600 flex items-center justify-center text-white shadow-sm">
                                            <component :is="getIconComponent(selectedModule?.icono)" class="w-5 h-5" />
                                        </div>
                                        <div>
                                            <p class="text-sm font-medium text-gray-900">{{ selectedModule?.titulo }}</p>
                                            <p class="text-xs text-gray-500 font-mono">{{ selectedModule?.ruta }}</p>
                                        </div>
                                        <span class="ml-auto text-xs text-gray-400">Orden: {{ selectedModule?.orden || 0
                                        }}</span>
                                    </div>
                                </div>
                            </div>

                            <!-- Tab: Icono -->
                            <div v-show="activeTab === 'icon'" class="space-y-5 max-w-2xl">
                                <div>
                                    <label class="block text-sm font-medium text-gray-700 mb-2">Seleccionar
                                        Icono</label>
                                    <input v-model="iconSearch" placeholder="Buscar icono..."
                                        class="w-full px-3 py-2 text-sm border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500" />
                                </div>
                                <div
                                    class="grid grid-cols-3 sm:grid-cols-4 md:grid-cols-6 gap-3 max-h-64 overflow-y-auto pr-2">
                                    <div v-for="iconOption in filteredIcons" :key="iconOption.name"
                                        @click="selectedModule.icono = iconOption.name" :class="['flex flex-col items-center gap-2 p-3 rounded-lg border cursor-pointer transition-all',
                                            selectedModule.icono === iconOption.name
                                                ? 'border-blue-500 bg-blue-50 ring-2 ring-blue-200'
                                                : 'border-gray-200 hover:border-gray-300 hover:bg-gray-50']">
                                        <component :is="iconOption.component" class="w-6 h-6 text-gray-600" />
                                        <span class="text-[10px] text-gray-500 text-center break-all">
                                            {{ iconOption.label }}
                                        </span>
                                    </div>
                                </div>
                                <div v-if="selectedModule.icono"
                                    class="flex items-center gap-3 p-3 bg-gray-50 rounded-lg border">
                                    <component :is="getIconComponent(selectedModule.icono)"
                                        class="w-6 h-6 text-blue-600" />
                                    <span class="text-sm text-gray-700">
                                        {{ selectedModule.icono }}
                                    </span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Footer mejorado -->
                    <div
                        class="flex flex-col sm:flex-row justify-end gap-3 px-6 py-4 border-t border-gray-200 bg-gray-50 rounded-b-xl">
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
import * as Icons from "@heroicons/vue/24/outline";

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

const iconOptions = Object.keys(Icons).map(name => ({
    name,
    component: Icons[name as keyof typeof Icons],
    label: name.replace('Icon', '') // opcional: limpiar nombre
}));


const getIconComponent = (iconName: string) => {
    return Icons[iconName as keyof typeof Icons] || Icons.FolderIcon;
};

// Tabs
const tabs = [
    { key: "basic", label: "Datos básicos" },
    { key: "icon", label: "Icono" },
];
const activeTab = ref("basic");

// Datos de ejemplo
const modulesData = ref<Module[]>([
    { id: 1, titulo: "Dashboard", ruta: "/dashboard", icono: "HomeIcon", orden: 1, activo: true, padre_id: null, expanded: true },
    { id: 2, titulo: "Usuarios", ruta: "/usuarios", icono: "UsersIcon", orden: 2, activo: true, padre_id: null, expanded: true },
    { id: 3, titulo: "Lista Usuarios", ruta: "/usuarios/list", icono: "ListBulletIcon", orden: 1, activo: true, padre_id: 2 },
    { id: 4, titulo: "Crear Usuario", ruta: "/usuarios/create", icono: "PlusIcon", orden: 2, activo: true, padre_id: 2 },
    { id: 5, titulo: "Cursos", ruta: "/cursos", icono: "BookOpenIcon", orden: 3, activo: true, padre_id: null, expanded: false },
    { id: 6, titulo: "Configuración", ruta: "/configuracion", icono: "CogIcon", orden: 4, activo: true, padre_id: null, expanded: false },
    { id: 7, titulo: "Módulo Inactivo", ruta: "/inactivo", icono: "FolderIcon", orden: 5, activo: false, padre_id: null, expanded: false },
]);

const showModal = ref(false);
const selectedModule = ref<any>(null);
const searchTerm = ref("");
const expandedState = ref<Record<number, boolean>>({});

const initExpandedState = (modules: Module[]) => {
    modules.forEach(module => {
        expandedState.value[module.id] = module.expanded ?? false;
        if (module.children) initExpandedState(module.children);
    });
};

const buildTree = (modules: Module[]): Module[] => {
    const map = new Map<number, Module>();
    const roots: Module[] = [];

    modules.forEach(module => {
        map.set(module.id, {
            ...module,
            children: [],
            expanded: expandedState.value[module.id] ?? module.expanded ?? false
        });
    });

    modules.forEach(module => {
        const node = map.get(module.id);
        if (module.padre_id && map.has(module.padre_id)) {
            const parent = map.get(module.padre_id);
            if (parent && node) {
                if (!parent.children) parent.children = [];
                parent.children.push(node);
            }
        } else if (node) {
            roots.push(node);
        }
    });

    const sortByOrder = (items: Module[]) => {
        items.sort((a, b) => (a.orden || 0) - (b.orden || 0));
        items.forEach(item => {
            if (item.children?.length) sortByOrder(item.children);
        });
    };
    sortByOrder(roots);
    return roots;
};

const treeModules = computed(() => buildTree(modulesData.value));

const toggleExpand = (module: Module) => {
    expandedState.value[module.id] = !expandedState.value[module.id];
    module.expanded = expandedState.value[module.id];
};

const filteredModules = computed(() => {
    if (!searchTerm.value) return treeModules.value;
    const term = searchTerm.value.toLowerCase();
    const filterModules = (modules: Module[]): Module[] => {
        const result: Module[] = [];
        for (const module of modules) {
            const matches = module.titulo.toLowerCase().includes(term) || (module.ruta && module.ruta.toLowerCase().includes(term));
            const filteredChildren = module.children ? filterModules(module.children) : [];
            if (matches || filteredChildren.length > 0) {
                result.push({ ...module, children: filteredChildren, expanded: true });
            }
        }
        return result;
    };
    return filterModules(treeModules.value);
});

const parentModules = computed(() => modulesData.value.filter(m => !m.padre_id));

const expandAll = () => {
    const expandRecursive = (modules: Module[]) => {
        modules.forEach(module => {
            expandedState.value[module.id] = true;
            module.expanded = true;
            if (module.children?.length) expandRecursive(module.children);
        });
    };
    expandRecursive(treeModules.value);
};

const collapseAll = () => {
    const collapseRecursive = (modules: Module[]) => {
        modules.forEach(module => {
            expandedState.value[module.id] = false;
            module.expanded = false;
            if (module.children?.length) collapseRecursive(module.children);
        });
    };
    collapseRecursive(treeModules.value);
};

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
    activeTab.value = "basic";
    showModal.value = true;
};

const confirmDelete = (module: Module) => {
    if (confirm(`¿Eliminar el módulo "${module.titulo}"?`)) {
        const index = modulesData.value.findIndex(m => m.id === module.id);
        if (index !== -1) {
            modulesData.value.splice(index, 1);
        }
        delete expandedState.value[module.id];
    }
};

const btnCerrarModal = () => {
    showModal.value = false;
    selectedModule.value = null;
};

const btnConfirmar = () => {
    if (!selectedModule.value.titulo?.trim()) {
        alert("El título del módulo es obligatorio");
        return;
    }

    if (selectedModule.value.id) {
        const index = modulesData.value.findIndex(m => m.id === selectedModule.value.id);
        if (index !== -1) {
            modulesData.value[index] = { ...selectedModule.value };
        }
    } else {
        const newId = Math.max(...modulesData.value.map(m => m.id), 0) + 1;
        modulesData.value.push({
            ...selectedModule.value,
            id: newId,
        });
        expandedState.value[newId] = false;
    }

    btnCerrarModal();
};

const iconSearch = ref("");

const filteredIcons = computed(() => {
    if (!iconSearch.value) return iconOptions;

    return iconOptions.filter(icon =>
        icon.name.toLowerCase().includes(iconSearch.value.toLowerCase())
    );
});

initExpandedState(modulesData.value);
</script>