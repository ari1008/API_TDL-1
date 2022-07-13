from Findscrapper import Cfind


def convertLanguage(p):
    limit = -1
    if len(p) <= 1:
        print("error")
        return
    cp = p[2][1]
    Type = p[2][2]
    entityTable = entityExtract(p[1], [])
    if len(p) == 4 and p[3] >= 0:
        limit = p[3]
    Cfind(cp, Type, entityTable, limit)


def entityExtract(entity, entityTable):
    if type(entity) != str:
        if len(entity) > 2 and type(entity) == tuple:
            entityExtract(entity[2], entityTable)
        if len(entity) > 1 and type(entity) == tuple:
            entityExtract(entity[1], entityTable)
    if 'ENTITY' != entity and 'EMPTY' != entity and type(entity) == str:
        entityTable.append(entity)
    return entityTable
