admin_roles = [
    "super_admin",
    "moderator"
]


def is_admin(role):
    return role in admin_roles