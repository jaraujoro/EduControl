from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Prefetch
from .serializers import MenuSerializer
from apps.menu.models import Menu
from apps.rol.models import RolMenu
from apps.usuario.models import UsuarioRol, UsuarioMenu

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_menu_x_usuario(request):

    user = request.user

    # 1. OBTENER ROL DEL USUARIO
    usuario_rol = UsuarioRol.objects.get(usuario=user)
    rol = usuario_rol.usuario_rol

    # 2. MENÚS POR ROL
    role_menu_ids = RolMenu.objects.filter(
        rol=rol
    ).values_list('menu_id', flat=True)

    # 3. MENÚS POR USUARIO
    user_menu_ids = UsuarioMenu.objects.filter(
        usuario=user,
        permiso_ver=True
    ).values_list('menu_id', flat=True)

    # 4. UNIR AMBOS (sin duplicados)
    menu_ids = set(role_menu_ids) | set(user_menu_ids)
    
    # 5. QUERY OPTIMIZADA
    menus = Menu.objects.filter(
        id__in=menu_ids,
        menu_padre__isnull=True,
        menu_activo=True
    ).prefetch_related(
        Prefetch(
            'menus_hijos',
            queryset=Menu.objects.filter(
                id__in=menu_ids,
                menu_activo=True
            ).order_by('menu_orden'),
            to_attr='children_list'
        )
    ).order_by('menu_orden')

    # 6. SERIALIZER
    serializer = MenuSerializer(menus, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def list_menu(request):

    menus = Menu.objects.filter(
        menu_padre__isnull=True,
        menu_activo=True
    ).prefetch_related(
        Prefetch(
            'menus_hijos',
            queryset=Menu.objects.filter(menu_activo=True).order_by('menu_orden'),
            to_attr='children_list'
        )
    ).order_by('menu_orden')

    serializer = MenuSerializer(menus, many=True)

    return Response(serializer.data)