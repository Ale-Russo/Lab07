from database.meteo_dao import MeteoDao


class Model:
    def __init__(self):
        self._sequenza_ottima = []
        self._costo_minimo = -1

    def get_media_umidita(self,mese):
        return MeteoDao.get_media_umidita(mese)

    def calcola_sequenza(self,mese):
        lista_giorni = MeteoDao.get_meta_mese(mese)
        self._sequenza_ottima = []
        self._costo_minimo = -1

        self.ricorsione(0, [], lista_giorni)

        return self._sequenza_ottima, self._costo_minimo

    def calcola_costo(self, parziale):
        costo = 0
        citta_corrente = ""
        for s in parziale:
            costo += s.umidita
            if citta_corrente != "" and s.localita != citta_corrente:
                costo += 100
                citta_corrente = s.localita
        return costo

    def ricorsione(self, giorno_i, parziale, lista_giorni):
        #TERMINALE
        if giorno_i == 15:
         costo= self.calcola_costo(parziale)
         if costo < self._costo_minimo or self._costo_minimo == -1:
             self._costo_minimo = costo
             self._sequenza_ottima = list(parziale)
             return
        #RICORSIONE
        else:
            for citta in ["Torino", "Genova", "Milano"]:
                situazione_oggi = None
                for s in lista_giorni[giorno_i*3: (giorno_i*3) +3]:
                    if s.localita == citta:
                        situazione_oggi = s
                        break

                giorni_totali=0
                for s in parziale:
                    if s.localita == citta:
                        giorni_totali += 1

                if giorni_totali >= 6:
                    continue

                if len(parziale) > 0:
                    citta_prima = parziale[-1].localita
                    if citta_prima != citta:
                        consecutivi = 0
                        for s in reversed(parziale):
                            if s.localita == citta_prima:
                                consecutivi += 1
                            else:
                                break
                        if consecutivi < 3:
                            continue

                parziale.append(situazione_oggi)
                self.ricorsione(giorno_i+1, parziale, lista_giorni)
                parziale.pop()







