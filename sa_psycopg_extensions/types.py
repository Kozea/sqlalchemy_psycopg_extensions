import psycopg2.extras
from sqlalchemy.dialects.postgresql.base import ischema_names
from sqlalchemy import types

"""
This module provides an HStore SQLAlchemy datatype.

Sample usage:

    from sa_psycopg_extensions.types import HStore
    # The mapping is dependent on the hstore oid in the database
    HStore.register(my_sqlalchemy_engine)
"""

class HStore(types.UserDefinedType):
    """An sqlalchemy type for managing hstore (python dictionary.

    This class is basically a no-op, because psycopg2 handles all the
    conversion for us.
    """

    def __init__(self):
        super(HStore, self).__init__()

    def python_type(self):
        return dict

    def get_col_spec(self):
        """Returns the column specification (ie, type as it appears in a create
        table statement."""
        return "hstore"

    def bind_processor(self, dialect):
        return lambda x: x

    def result_processor(self, dialect, coltype):
        return lambda x: x

    @classmethod
    def register(cls, bind):
        """Register the HSTORE datatype on psycopg2, and on sqlalchemy."""
        oid = tuple(bind.execute("select 'hstore'::regtype::oid,"
                            "'hstore[]'::regtype::oid;").first())
        # Registering the concrete type in psycopg2
        psycopg2.extras.register_hstore(None, globally=True, unicode=True,
                oid=oid[0], array_oid=oid[1])
        psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
        ischema_names['hstore'] = cls
