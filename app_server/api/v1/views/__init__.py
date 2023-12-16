from flask import Blueprint

app_bp = Blueprint('api routing blueprint', __name__, url_prefix='/api/v1')

from api.v1.views.folders import *
from api.v1.views.notes import *
from api.v1.views.projects import *
from api.v1.views.tasks import *
from api.v1.views.users import *
from api.v1.views.filters import *

