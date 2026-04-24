from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from apps.rol.models import Rol, RolMenu
from apps.menu.models import Menu
from django.db import transaction

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_rol(request):
    roles = Rol.objects.order_by('id')
    return Response(roles.values())

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_rol(request):
    data = request.data

    rol_data = data.get('rol')
    menus = data.get('menus', [])

    try:
        with transaction.atomic():

            # 🔹 1. CREAR o ACTUALIZAR ROL
            rol_id = rol_data.get('id')

            if rol_id:
                rol = Rol.objects.get(id=rol_id)
                rol.rol_nombre = rol_data.get('rol_nombre')
                rol.rol_descripcion = rol_data.get('rol_descripcion')
                rol.rol_activo = rol_data.get('rol_activo')
                rol.save()
            else:
                rol = Rol.objects.create(
                    rol_nombre=rol_data.get('rol_nombre'),
                    rol_descripcion=rol_data.get('rol_descripcion'),
                    rol_activo=rol_data.get('rol_activo')
                )

            # 🔹 2. OBTENER MENUS ACTUALES EN BD
            current_menus = set(
                RolMenu.objects.filter(rol=rol)
                .values_list('menu_id', flat=True)
            )

            # 🔹 3. MENUS QUE VIENEN DEL FRONT
            new_menus = set(menus)

            # 🔹 4. CALCULAR
            to_add = new_menus - current_menus
            to_remove = current_menus - new_menus

            # 🔹 5. INSERTAR LOS NUEVOS (checked)
            RolMenu.objects.bulk_create([
                RolMenu(rol=rol, menu_id=menu_id)
                for menu_id in to_add
            ])

            # 🔹 6. ELIMINAR LOS DESMARCADOS
            RolMenu.objects.filter(
                rol=rol,
                menu_id__in=to_remove
            ).delete()

        return Response({
            "message": "Rol y permisos guardados correctamente",
            "rol_id": rol.id
        })

    except Exception as e:
        return Response({
            "error": str(e)
        }, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_rol_x_menu(request, rol_id):

    role_menu_ids = set(
        RolMenu.objects.filter(rol_id=rol_id)
        .values_list('menu_id', flat=True)
    )

    menus = Menu.objects.filter(
        menu_padre__isnull=True,
        menu_activo=True
    ).order_by('menu_orden')

    data = []

    for menu in menus:
        children = Menu.objects.filter(
            menu_padre=menu,
            menu_activo=True
        ).order_by('menu_orden')

        data.append({
            "id": menu.id,
            "titulo": menu.menu_titulo,
            "ruta": menu.menu_ruta,
            "icono": menu.menu_icono,
            "checked": menu.id in role_menu_ids,
            "children": [
                {
                    "id": c.id,
                    "titulo": c.menu_titulo,
                    "ruta": c.menu_ruta,
                    "icono": c.menu_icono,
                    "checked": c.id in role_menu_ids
                } for c in children
            ]
        })

    return Response(data)