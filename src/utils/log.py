import logging
import logging.config
import src.utils.configs as configs 

def logs_personal():
    caminho_log = configs.PASTA_LOGS
    if caminho_log:
            caminho_log.mkdir(parents=True, exist_ok=True)
            caminho_log.mkdir(parents=True, exist_ok=True)


    # debug(), info(), warning(), error() and critical()
    logging.basicConfig(
        format      = f"\n%(levelname)s - %(asctime)s - %(name)s - %(message)s", 
        datefmt     = '%m/%d/%Y %I:%M:%S %p',
        filename    = caminho_log / 'logs.log', 
        encoding    = 'utf-8', 
        level       = logging.DEBUG
    )