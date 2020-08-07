
from flask import Flask, jsonify, request
from src.cn.data_base_connection import Database
from src.models.dbModel import dbModel
from src.entities.serviceEntity import serviceEntity

class serviceModel(dbModel):

    def __init__(self):
        dbModel.__init__(self)

    def get_services(self):
        _db = None
        _status = 1
        _data_row = []
        try:
            _db = Database()
            _db.connect(self.host,self.port,self.user,self.password,self.database)
            print('Se conecto a la bd')
            _con_client = _db.get_client()
            _sql = """SELECT id, full_name, url_image, status FROM main.service
                      WHERE status = %s;"""
            _cur = _con_client.cursor()
            _cur.execute(_sql,(_status,))
            _rows = _cur.fetchall()
            for row in _rows:
                _serviceEntity = serviceEntity()
                _serviceEntity.id  = row[0]
                _serviceEntity.full_name  = row[1] 
                _serviceEntity.url_image  = row[2]
                _serviceEntity.status  = row[3]
                _data_row.append(_serviceEntity)

            _cur.close()
        except(Exception) as e:
            print('error: '+ str(e))
        finally:
            if _db is not None:
                _db.disconnect()
                print("Se cerro la conexion")
        return _data_row

    def get_services_by_user(self,id_user):
        _db = None
        _status = 1
        _data_row = []
        _id_user = id_user
        try:
            _db = Database()
            _db.connect(self.host,self.port,self.user,self.password,self.database)
            print('Se conecto a la bd')
            _con_client = _db.get_client()
            _sql = """SELECT s.id, 
                        s.full_name, 
                        s.url_image, 
                        b.enable, 
                        s.status 
                    FROM   main.service s 
                        LEFT JOIN (SELECT s.id AS id_service, 
                                            s.status, 
                                            us.enable 
                                    FROM   main.service s 
                                            LEFT JOIN main.user_service us 
                                                    ON s.id = us.id_service 
                                    WHERE  us.id_user = %s) b 
                                ON s.id = b.id_service; """
                                        
            _cur = _con_client.cursor()
            _cur.execute(_sql,(_id_user,))
            _rows = _cur.fetchall()
            for row in _rows:
                _serviceEntity = serviceEntity()
                _serviceEntity.id  = row[0]
                _serviceEntity.full_name  = row[1] 
                _serviceEntity.url_image  = row[2]
                _serviceEntity.enable  = row[3]
                _serviceEntity.status  = row[4]
                _data_row.append(_serviceEntity)

            _cur.close()
        except(Exception) as e:
            print('error: '+ str(e))
        finally:
            if _db is not None:
                _db.disconnect()
                print("Se cerro la conexion")
        return _data_row