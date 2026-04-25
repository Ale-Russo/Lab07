from database.meteo_dao import MeteoDao


class Model:
    def __init__(self):
        self._sequenza_ottima = []
        self._costo_minimo = -1

    def get_media_umidita(self,mese):
        return MeteoDao.get_media_umidita(mese)

    def calcola_sequenza(self,mese):
        lista = MeteoDao.get_meta_mese(mese)
        print(len(lista))
        return lista