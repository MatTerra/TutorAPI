from nova_api.dao.generic_sql_dao import GenericSQLDAO
from nova_api.persistence.postgresql_helper import PostgreSQLHelper

from entities.Tutor import Tutor


class TutorDAO(GenericSQLDAO):
    def __init__(self, database_instance: PostgreSQLHelper = None):
        super(TutorDAO, self).__init__(database_instance=database_instance,
                                       database_type=PostgreSQLHelper,
                                       return_class=Tutor)
