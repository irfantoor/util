from zipfile import ZipFile
from typing import Tuple
from pathlib import Path
import os, requests
from abc import ABC

from util.setting import DEFAULT_PATH

class Downloader(ABC):
    def __init__(
                self,
                data_path: str = DEFAULT_PATH
        ) -> None:
            self.__data_path__: Path = data_path
            # self._kwargs: Dict[str, Any] = kwargs

    def normalize(self, file: str)->str:
        return str(Path(self.__data_path__ + "/" + file))

    def download(self, url: str, file: str = None, extract: bool = False):
        if (not file):
            file = os.path.basename(url)

        file_path = self.normalize(file)
        print("Téléchargement du fichier (%s) :" % (file) , end=" ")

        if (os.path.exists(file_path)):
            print("déjà téléchargé")
        else:
            with open(file_path,'wb') as fp:
                r = requests.get(url)
                if (fp.write(r.content)):
                    print("téléchargé")
                else:
                    print("error")

        if (extract):
            self.extract(file)

    # extraction d'un fichier zip
    def extract(self, file: str):
        print("Extraction du fichier (%s) :" % (file), end = " ")
        file_path = self.normalize(file)
        if not os.path.exists(file_path):
            print("-- error : untrouvable")
        else:
            print("")

            with ZipFile(file_path, 'r') as zip:
                for file_info in zip.infolist():
                    file = file_info.filename
                    print(" -", file, ":", end=" ")
                    file = self.__data_path__ + file

                    if os.path.exists(file):
                        print("déjà présent")
                    else:
                        zip.extract(file_info, path=self.__data_path__)
                        print("fait")
