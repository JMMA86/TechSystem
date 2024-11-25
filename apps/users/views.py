from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.shortcuts import render

from apps.common.services.pgadmin.models import UserAccount


@login_required
def show_users(request):
    users = UserAccount.objects.all()
    for user in users:
        roles = user.userrole_set.select_related("role_id").values(
            _id=F("role_id__role_id"),
            role_name=F("role_id__role_name"),
            description=F("role_id__description"),
        )
        user.roles = list(roles)
    return render(request, "layouts/users.html", {"users": users})
