from api.v1.views import app_bp


@app_bp.route('/<user_id>/projects',
             methods=['GET', 'POST'], strict_slashes=False)
def user_projects_viewer(user_id):
    pass

@app_bp.route('/<user_id>/projects/<project_id>',
             methods=['PUT', 'DELETE'], strict_slashes=False)
def user_projects_modifier(user_id, project_id):
    pass



@app_bp.route('/<user_id>/projects/<project_id>/tasks',
             methods=['GET', 'POST'], strict_slashes=False)
def user_project_tasks_viewer(user_id, project_id):
    pass

@app_bp.route('/<user_id>/projects/<project_id>/tasks/<task_id>',
             methods=['PUT', 'DELETE'], strict_slashes=False)
def user_project_tasks_modifier(user_id, project_id, task_id):
    pass



@app_bp.route('/<user_id>/projects/<project_id>/notes',
             methods=['GET', 'POST'], strict_slashes=False)
def user_project_notes_viewer(user_id, project_id):
    pass

@app_bp.route('/<user_id>/projects/<project_id>/notes/<note_id>',
             methods=['PUT', 'DELETE'], strict_slashes=False)
def user_project_notes_modifier(user_id, project_id, note_id):
    pass
