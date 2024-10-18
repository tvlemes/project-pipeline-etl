import typing
from pathlib import Path
import logging
import abc

from src.aquisicao.base_etl import BaseETL

class EscolaETL(BaseETL, abc.ABC):

    caminho_entrada: Path
    caminho_saida: Path
    _logger : logging.Logger
    # reprocessar: bool
    # _dados_entrada: typing.Dict[str, pd.DataFrame]
    # _dados_saida: typing.Dict[str, pd.DataFrame]

    def __init__(
            self,
            entrada: typing.Union[str, Path],
            saida: typing.Union[str, Path],
            criar_caminho: bool = True,
            reprocessar: bool = False,
    ) -> None:
        self.caminho_entrada = Path(entrada)
        self.caminho_saida = Path(saida)

        # self._logger =  logging.getLogger(self.__class__.__name__) # self.__class__.__name__

        # Obtendo um logger
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
            datefmt='%m/%d/%Y %I:%M:%S %p',
            filename='logs.log', 
            encoding='utf-8', 
            level=[logging.INFO]
        )

    def __str__(self) -> str:
        """
        Representação da classe em modo texto
        """
        return self.__class__.__name__

    def teste_log(self) -> str:
        logging.info('TESTE')