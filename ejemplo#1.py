class persona():
    def __init__(self, apepat, apemat, nom):
        self. apellidopaterno = apepat
        self. apellidomaterno = apemat
        self. nombres = nom

    def  mostrarnombrecompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.apellidopaterno, self.apellidomaterno, self.nombres)

class estudiante(persona):
    pass

estu1 = estudiante("rodas","lopez","mafe")
print(estu1.mostrarnombrecompleto())


