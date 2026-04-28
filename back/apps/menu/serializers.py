from rest_framework import serializers
from .models import Menu

class MenuSerializer(serializers.ModelSerializer):

    titulo = serializers.CharField(source='menu_titulo')
    ruta = serializers.CharField(source='menu_ruta')
    icono = serializers.CharField(source='menu_icono')
    orden = serializers.IntegerField(source='menu_orden')
    activo = serializers.BooleanField(source='menu_activo')
    padre_id = serializers.IntegerField(source='menu_padre_id')

    children = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = [
            'id',
            'titulo',
            'ruta',
            'icono',
            'orden',
            'activo',
            'padre_id',
            'children'
        ]

    def get_children(self, obj):
        children = getattr(obj, 'children_list', [])

        # 👉 IMPORTANTE: solo serializamos sin children
        return [
            {
                "id": c.id,
                "titulo": c.menu_titulo,
                "ruta": c.menu_ruta,
                "icono": c.menu_icono,
                "orden": c.menu_orden,
                "activo": c.menu_activo,
                "padre_id": c.menu_padre_id
            }
            for c in children
        ]