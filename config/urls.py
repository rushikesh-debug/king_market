from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('dashboard.urls')),
    path('games/', include('games.urls')),

    # 🔥 ADD THIS (IMPORTANT)
    path('accounts/', include('accounts.urls')),
    
    path(
    "wallet/",
    include("wallet.urls")
),
    
    path(
    "adminpanel/",
    include("adminpanel.urls")
),
]