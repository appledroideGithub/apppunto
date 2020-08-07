from flask import Flask, jsonify, request
from src.cn.data_base_connection import Database
from src.models.dbModel import dbModel
from src.entities.userEntity import userEntity
from src.entities.userStoreEntity import userStoreEntity

class userStoreModel(dbModel):

    def __init__(self):
        dbModel.__init__(self)

    def get_user_stores(self,id_user):
        _db = None
        _status = 1
        _id_user = id_user
        _data_row = []
        print(id_user)
        try:
            _db = Database()
            _db.connect(self.host,self.port,self.user,self.password,self.database)
            print('Se conecto a la bd')
            _con_client = _db.get_client()
            _sql = """SELECT id, id_user, full_name, address, longitude, latitude, main, status FROM main.user_store
                      WHERE status = %s and id_user = %s;"""
            _cur = _con_client.cursor()
            _cur.execute(_sql,(_status,_id_user))
            _rows = _cur.fetchall()

            for row in _rows:
                _userStoreEntity= userStoreEntity()
                _userStoreEntity.id  = row[0]
                _userStoreEntity.id_user  = row[1] 
                _userStoreEntity.full_name  = row[2]
                _userStoreEntity.address  = row[3]
                _userStoreEntity.longitude  = row[4]
                _userStoreEntity.latitude  = row[5]
                _userStoreEntity.main  = row[6]
                _userStoreEntity.status  = row[7]
                _data_row.append(_userStoreEntity)
            print(_data_row)
            _cur.close()
        except(Exception) as e:
            print('error: '+ str(e))
        finally:
            if _db is not None:
                _db.disconnect()
                print("Se cerro la conexion")
        return _data_row