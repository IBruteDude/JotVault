from api.v1.views import app_bp


@app_bp.route('/<user_id>/folders',
             methods=['GET', 'POST'], strict_slashes=False)
def user_folders_viewer(user_id):
    pass

@app_bp.route('/<user_id>/folders/<folder_id>',
             methods=['PUT', 'DELETE'], strict_slashes=False)
def user_folders_modifier(user_id, folder_id):
    pass
