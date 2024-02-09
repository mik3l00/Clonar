from django.contrib import admin
from .models import goteo,riego_invernadero,riego_jardines,aspersion,conducciones,riego_Arboles,riego_tecnificados,servicio_riego

@admin.register(goteo)
class goteoAdmin(admin.ModelAdmin):
    list_display = ('nombre_servicio', 'costo_estimado')

@admin.register(riego_invernadero)
class riego_invernaderoAdmin(admin.ModelAdmin):
    list_display = ('nombre_servicio', 'costo_estimado')

@admin.register(riego_jardines)
class riego_jardinesAdmin(admin.ModelAdmin):
    list_display = ('nombre_servicio', 'costo_estimado')

@admin.register(aspersion)
class aspersionAdmin(admin.ModelAdmin):
    list_display = ('nombre_servicio', 'costo_estimado')

@admin.register(conducciones)
class conduccionesAdmin(admin.ModelAdmin):
    list_display = ('nombre_servicio', 'costo_estimado')

@admin.register(riego_Arboles)
class riego_ArbolesAdmin(admin.ModelAdmin):
    list_display = ('nombre_servicio', 'costo_estimado')

@admin.register(riego_tecnificados)
class riego_tecnificadosAdmin(admin.ModelAdmin):
    list_display = ('nombre_servicio', 'costo_estimado')


@admin.register(servicio_riego)
class servicio_riegoAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_goteo', 'id_riego_invernadero', 'id_riego_jardines', 'id_aspersion', 'id_conducciones', 'id_riego_Arboles', 'id_riego_tecnificados')
