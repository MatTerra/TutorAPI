from nova_api import error_response, success_response, use_dao

from database.TutorDAO import TutorDAO
from entities.Tutor import Tutor


@use_dao(TutorDAO, "API Unavailable")
def probe(dao: TutorDAO = None):
    total, _ = dao.get_all(length=1, offset=0, filters=None)
    return success_response(message="API Ready",
                            data={"available": total})


@use_dao(TutorDAO, "Unable to list tutor")
def read(length: int = 20, offset: int = 0,
         dao: TutorDAO = None, **kwargs):
    for key, value in kwargs.items():
        kwargs[key] = value.split(',') \
                        if len(value.split(',')) > 1 \
                        else value
    total, results = dao.get_all(length=length, offset=offset,
                                 filters=kwargs if len(kwargs) > 0 else None)
    return success_response(message="List of tutor",
                            data={"total": total, "results": [dict(result)
                                                              for result
                                                              in results]})


@use_dao(TutorDAO, "Unable to retrieve tutor")
def read_one(id_: str, dao: TutorDAO = None):
    result = dao.get(id_=id_)

    if not result:
        return success_response(status_code=404,
                                message="Tutor not found in database",
                                data={"id_": id_})

    return success_response(message="Tutor retrieved",
                            data={"Tutor": dict(result)})


@use_dao(TutorDAO, "Unable to create tutor")
def create(entity: dict, dao: TutorDAO = None):
    entity_to_create = Tutor(**entity)

    dao.create(entity=entity_to_create)

    return success_response(message="Tutor created",
                            data={"Tutor": dict(entity_to_create)})


@use_dao(TutorDAO, "Unable to update tutor")
def update(id_: str, entity: dict, dao: TutorDAO = None):
    entity_to_update = dao.get(id_)

    if not entity_to_update:
        return error_response(status_code=404,
                              message="Tutor not found",
                              data={"id_": id_})

    entity_fields = dao.fields.keys()

    for key, value in entity.items():
        if key not in entity_fields:
            raise KeyError("{key} not in {entity}"
                           .format(key=key,
                                   entity=dao.return_class))

        entity_to_update.__dict__[key] = value

    dao.update(entity_to_update)

    return success_response(message="Tutor updated",
                            data={"Tutor": dict(entity_to_update)})


@use_dao(TutorDAO, "Unable to delete tutor")
def delete(id_: str, dao: TutorDAO):
    entity = dao.get(id_=id_)

    if not entity:
        return error_response(status_code=404,
                              message="Tutor not found",
                              data={"id_": id_})

    dao.remove(entity)

    return success_response(message="Tutor deleted",
                            data={"Tutor": dict(entity)})
