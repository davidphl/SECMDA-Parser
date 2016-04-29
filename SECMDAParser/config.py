import os

#Look for files downloaded by SECEdgar Package
DEFAULT_DATA_PATH = os.path.abspath(os.path.join(
                                    os.path.dirname(__file__), '..','..', 'SEC-Edgar', 'SEC-Edgar-Data'))