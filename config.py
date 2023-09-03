import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "21970953"))
    API_HASH = os.environ.get("API_HASH", "914f964d0e1e15b1627b33e1d2ea35bd")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6300757268:AAFRfeC35-JSpFy5NsB_vHeD978TZ2yXPjg")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "6408947191")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://JohnWick:JohnWick@cluster0.ap7ydbx.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQFPQAkAb8opqzXFA7qtqXfvSAc8XCHG369xunogKtMNMiOVWvzDSaQMkr3mIScjGl7Bm8NlbXAb14ydXM_HA-RtLM3EdZLrQW0AUlgJgD7-pPyNq2sbvQPntTLv88zQj03cgvELsEptiFRVwqZZrYC-tuS20z4QpF3DD15tOHJowoeXxibzKAQ-VrCGlVfNV2CDU8Abruhh263HW8AQRJ_qEG-vd_OOwJEJXjFn9xkwDBtmN9vFwBLlH9A-VKJu9n2jFVXMrj_wPYIAaYam0QvavvGBjqFzrsdt3ypZ1efXjnn_8LZ_sXZvnIvsbuDV2mVvcMJFpEYrT7Xono5-LQdUnWfvRwAAAAF-AMX3AA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001956947105"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "johnwickforward_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
