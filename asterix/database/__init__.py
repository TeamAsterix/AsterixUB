from asterix.database.postgres.afk_sql import AFKSQL
from asterix.database.postgres.dv_sql import DVSQL
from asterix.database.postgres.filters_sql import FILTERSSQL
from asterix.database.postgres.notes_sql import NOTESSQL
from asterix.database.postgres.pmpermit_sql import PMPERMITSQL
from asterix.database.postgres.welcome_sql import WELCOMESQL


class Database(AFKSQL, NOTESSQL, PMPERMITSQL, DVSQL, WELCOMESQL, FILTERSSQL):
    pass
