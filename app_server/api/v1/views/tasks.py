from api.v1.views import app_bp


@app_bp.route('/<user_id>/tasks',
             methods=['GET', 'POST'], strict_slashes=False)
def user_tasks_viewer(user_id):
    pass

@app_bp.route('/<user_id>/tasks/<task_id>',
             methods=['PUT', 'DELETE'], strict_slashes=False)
def user_tasks_modifier(user_id, task_id):
    pass
