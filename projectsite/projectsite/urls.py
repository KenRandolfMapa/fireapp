from django.contrib import admin
from django.urls import path

from fire.views import HomePageView, ChartView, PieCountbySeverity, LineCountbyMonth, MultilineIncidentTop3Country, multipleBarbySeverity
from fire.views import map_station, fire_incidents_map, station_list, station_create, station_detail,station_update, station_delete
from fire import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),
    path('PieChart/', PieCountbySeverity, name='chart'),
    path('lineChart/', LineCountbyMonth, name='chart'),
    path('multilineChart/', MultilineIncidentTop3Country, name='chart'),
    path('multiBarChart/', multipleBarbySeverity, name='chart'),
    path('stations', views.map_station, name='map-station'),
    path('fire_incidents_map/', views.fire_incidents_map, name='fire_incidents_map'),

    path('stations/', views.station_list, name='station-list'),
    path('stations/create/', views.station_create, name='station-create'),
    path('stations/<int:id>/', views.station_detail, name='station-detail'),
    path('stations/<int:id>/update/', views.station_update, name='station-update'),
    path('stations/<int:id>/delete/', views.station_delete, name='station-delete'),


]