from django.db import models


class goteo(models.Model):
    nombre_servicio =  models.CharField(max_length=150)
    costo_estimado = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return f"{self.nombre_servicio}"

class riego_invernadero(models.Model):
    nombre_servicio =  models.CharField(max_length=150)
    costo_estimado = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.nombre_servicio}"


class riego_jardines(models.Model):
    nombre_servicio =  models.CharField(max_length=150)
    costo_estimado = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.nombre_servicio}"


class aspersion(models.Model):
    nombre_servicio =  models.CharField(max_length=150)
    costo_estimado = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.nombre_servicio}"


class conducciones(models.Model):
    nombre_servicio =  models.CharField(max_length=150)
    costo_estimado = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.nombre_servicio}"


class riego_Arboles(models.Model):
    nombre_servicio =  models.CharField(max_length=150)
    costo_estimado = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.nombre_servicio}"


class riego_tecnificados(models.Model):
    nombre_servicio =  models.CharField(max_length=150)
    costo_estimado = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.nombre_servicio}"


class servicio_riego(models.Model):
    id_goteo = models.ForeignKey(goteo, related_name='servicio_goteo', on_delete=models.SET_NULL, null=True)
    id_riego_invernadero = models.ForeignKey(riego_invernadero, related_name='servicio_riego_invernadero', on_delete=models.SET_NULL, null=True)
    id_riego_jardines = models.ForeignKey(riego_jardines, related_name='servicio_riego_jardines', on_delete=models.SET_NULL, null=True)
    id_aspersion = models.ForeignKey(aspersion, related_name='servicio_aspersion', on_delete=models.SET_NULL, null=True)
    id_conducciones = models.ForeignKey(conducciones, related_name='servicio_conducciones', on_delete=models.SET_NULL, null=True)
    id_riego_Arboles = models.ForeignKey(riego_Arboles, related_name='servicio_riego_Arboles', on_delete=models.SET_NULL, null=True)
    id_riego_tecnificados = models.ForeignKey(riego_tecnificados, related_name='servicio_riego_tecnificados', on_delete=models.SET_NULL, null=True)


 


