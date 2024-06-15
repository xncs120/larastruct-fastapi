import os, importlib
from core.config import settings
from sqlmodel import SQLModel, Session, create_engine, select as select_, and_, or_

def checkRequiredSettings():
    if not hasattr(settings, 'MODELS_FOLDERNAME') or not hasattr(settings, 'MODELS_FILESUFFIX'):
        raise ValueError('Please add models MODELS_FOLDERNAME key and MODELS_FILESUFFIX(if have) in core/config to use Orm Wrapper.')

def initializeTables():
    checkRequiredSettings()
    files = next(os.walk(f'./{settings.MODELS_FOLDERNAME}'), (None, None, []))[2]
    model_files = [os.path.splitext(file)[0] for file in files if file.endswith(f'{settings.MODELS_FILESUFFIX}.py')]
    for model_file in model_files:
        importlib.import_module(f'{settings.MODELS_FOLDERNAME}.{model_file}')
    SQLModel.metadata.create_all(create_engine(settings.DATABASE_URL))

class Orm: # wrapper
    def __init__(self, class_name: str):
        checkRequiredSettings()
        module = importlib.import_module(f'{settings.MODELS_FOLDERNAME}.{class_name.lower()}{settings.MODELS_FILESUFFIX}')
        self.cls = getattr(module, class_name)
        self.engine = create_engine(settings.DATABASE_URL)
        self.session = Session(self.engine)

        self.columns = []
        self.query = ''
        self.where_query = ''
        self.or_where_query = ''
        
    def __buildQuery(self):
        if self.query == '':
            self.query = select_(self.cls)

        if self.where_query != '':
            self.query = self.query.where(self.where_query)

        if self.or_where_query != '':
            self.query = self.query.where(self.or_where_query)

    def select(self, columns: list):
        self.columns = columns
        column_list = [getattr(self.cls, column) for column in columns]
        self.query = select_(*column_list)
        return self

    def where(self, conditions: dict):
        condition_list = [getattr(self.cls, attr) == value for attr, value in conditions.items()]
        self.where_query = and_(*condition_list)
        return self
    
    def orWhere(self, conditions: dict):
        condition_list = [getattr(self.cls, attr) == value for attr, value in conditions.items()]
        self.where_query = or_(*condition_list)
        return self

    def get(self):
        self.__buildQuery()
        result = self.session.exec(self.query)
        if len(self.columns) > 0:
            result = result.mappings()
        return result.all()
    
    def first(self):
        self.__buildQuery()
        result = self.session.exec(self.query)
        if len(self.columns) > 0:
            result = result.mappings()
        return result.first()
    
    def create(self, kwargs):
        model = self(**kwargs)
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return model

    def update(self, kwargs):
        self.__buildQuery()
        rows = self.session.exec(self.query).all()
        for row in rows:
            for key, value in kwargs.items():
                setattr(row, key, value)
            self.session.add(row)
        self.session.commit()
        for row in rows:
            self.session.refresh(row)
        return rows
    
    def delete(self):
        self.__buildQuery()
        rows = self.session.exec(self.query).all()
        for row in rows:
            self.session.delete(row)
        self.session.commit()
        return rows
