<template>
  <div>
    <h1 class="text-2xl font-bold text-gray-800 mb-6">Dashboard</h1>
    
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
      <div class="bg-white rounded-xl shadow-sm p-6 border border-gray-100">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-gray-500 text-sm">Total Usuarios</p>
            <p class="text-2xl font-bold text-gray-800">1,234</p>
          </div>
          <div class="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center">
            <span class="text-2xl">👥</span>
          </div>
        </div>
      </div>
      
      <div class="bg-white rounded-xl shadow-sm p-6 border border-gray-100">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-gray-500 text-sm">Cursos Activos</p>
            <p class="text-2xl font-bold text-gray-800">45</p>
          </div>
          <div class="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center">
            <span class="text-2xl">📚</span>
          </div>
        </div>
      </div>
      
      <div class="bg-white rounded-xl shadow-sm p-6 border border-gray-100">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-gray-500 text-sm">Estudiantes</p>
            <p class="text-2xl font-bold text-gray-800">892</p>
          </div>
          <div class="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center">
            <span class="text-2xl">🎓</span>
          </div>
        </div>
      </div>
      
      <div class="bg-white rounded-xl shadow-sm p-6 border border-gray-100">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-gray-500 text-sm">Profesores</p>
            <p class="text-2xl font-bold text-gray-800">24</p>
          </div>
          <div class="w-12 h-12 bg-orange-100 rounded-lg flex items-center justify-center">
            <span class="text-2xl">👨‍🏫</span>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Tabla reciente -->
    <div class="bg-white rounded-xl shadow-sm border border-gray-100">
      <div class="px-6 py-4 border-b border-gray-100">
        <h2 class="font-semibold text-gray-800">Usuarios Recientes</h2>
      </div>
      <div class="overflow-x-auto">
        <table class="w-full">
          <thead class="bg-gray-50">
            <tr>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Nombre</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Email</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Rol</th>
              <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Estado</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-100">
            <tr>
              <td class="px-6 py-4 text-sm text-gray-800">Juan Pérez</td>
              <td class="px-6 py-4 text-sm text-gray-600">juan@email.com</td>
              <td class="px-6 py-4 text-sm text-gray-600">Estudiante</td>
              <td class="px-6 py-4"><span class="px-2 py-1 text-xs rounded-full bg-green-100 text-green-700">Activo</span></td>
            </tr>
            <tr>
              <td class="px-6 py-4 text-sm text-gray-800">María García</td>
              <td class="px-6 py-4 text-sm text-gray-600">maria@email.com</td>
              <td class="px-6 py-4 text-sm text-gray-600">Profesor</td>
              <td class="px-6 py-4"><span class="px-2 py-1 text-xs rounded-full bg-green-100 text-green-700">Activo</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>