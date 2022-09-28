from pathlib import Path
import os

class List_Files:

    def __init__(self):
        self._path = os.getcwd() + 'in/' # Se requiere cambiar el backslash por slash segun el S.O
        self._arr_list_file = [] # Array de almacenamiento del path completo del archivo a descifrar
        self._arr_list_dir = [] # Array de almacenamiento de las carpetas encontradas en la ubicación atual
        self._arr_list_dir2 = [] # Array de control de las carpetas listadas recorridas
        self.list_objects()


    def list_objects(self):
        self._contenido = os.listdir(self._path)

        for i in self._contenido:
            self._path1 = self._path
            _p = self._path+i
            if i[-4:] == '.txt' or i[-4:] == '.csv':
                self._path = _p
                self.list_files()
            elif Path(_p).is_dir() == True:
                self._path = _p+'\\' # Se requiere cambiar el backslash por slash segun el S.O
                self.list_folders()

            self._path = self._path1

        self.clear_array()
        return self._arr_list_file, self._arr_list_dir


    def clear_array(self):
        if len(self._arr_list_dir2) > 0:
            self._arr_list_dir2.pop(0)
        else:
            pass
        self._arr_list_dir2.extend(self._arr_list_dir)
        self._arr_list_dir.clear()
        self.list_tour()
        return self._arr_list_dir2, self._arr_list_dir

    def list_tour(self):
        for j in self._arr_list_dir2:
            self._path = j
            self.list_objects()
        return self.list_objects


    def list_folders(self):
        self._arr_list_dir.append(self._path)
        return self._arr_list_dir


    def list_files(self):
        print("Archivo agregado: "+self._path)
        self._arr_list_file.append(self._path)
        return self._arr_list_file
