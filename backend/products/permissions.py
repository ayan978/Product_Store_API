from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
    # def has_permission(self, request, view):
    #     if not request.user.is_staff:
    #         return False
    #     return super().has_permission(request, view)
    
    # def has_permission(self, request, view):
    #     if request.user.is_staff:
    #         if request.user.has_perm("products.view_product"): #app_name.action_model_name
    #             return True
    #         if request.user.has_perm("products.change_product"):
    #             return True
    #         if request.user.has_perm("products.add_product"):
    #             return True
    #         if request.user.has_perm("products.delete_product"):
    #             return True
    #         return False
    #     return False
              
    #     print(request.user.get_all_permissions())
    #     return False
             
    
    