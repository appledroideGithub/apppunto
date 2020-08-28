from src.models.userModel import userModel
from src.models.serviceModel import serviceModel
from src.entities.serviceEntity import serviceEntity
from src.entities.responseEntity import responseEntity
from src.controllers.responseController import responseController

class serviceController(responseController):

    def get_services(self):
        _message = None
        _status = self.interruption
        _data= None
        try:
            _serviceModel = serviceModel()
            _data = _serviceModel.get_services()
            _status = self.OK
            _message = self.messageOK
        except(Exception) as e:
            _status = self.interruption
            _message = self.messageInterruption + str(e)
            print('error: '+ str(e))
        return responseEntity(_status,_message,_data).toJSON()

    def get_services_wa(self):
        _data= None
        try:
            _serviceModel = serviceModel()
            _data = _serviceModel.get_services()
        except(Exception) as e:
            print('error: '+ str(e))
        return _data
    
    
    def get_service_by_id_wa(self,index):
        _entity= None
        try:
            _model = serviceModel()
            _entity = _model.get_services_by_id(index)
        except(Exception) as e:
            print('error: '+ str(e))
        return _entity
    
    def add_service(self,entity):
        try:
            _model = serviceModel()
            _entity = _model.add_service(entity)
        except(Exception) as e:
            print('error: '+ str(e))
        return _entity
    
    def get_services_by_user(self,index):
        _message = None
        _status = None
        _data= None
        try:
            _serviceModel = serviceModel()
            _data = _serviceModel.get_services_by_user(index)
            _status = self.OK
            _message = self.messageOK
        except(Exception) as e:
            _status = self.interruption
            _message = self.messageInterruption + str(e)
            print('error: '+ str(e))
        return responseEntity(_status,_message,_data).toJSON()
    
    def update_file_image(self,file_image):
        _message = None
        _status = None
        _data= None
        id_service = 5
        try:
            _model = serviceModel()
            _data = _model.update_file_image(id_service,file_image)
            _status = self.OK
            _message = self.messageOK
        except(Exception) as e:
            _status = self.interruption
            _message = self.messageInterruption + str(e)
            print('error: '+ str(e))
        return responseEntity(_status,_message,_data).toJSON()