from django.contrib import admin
from django.urls import path

from fire.views import HomePageView, ChartView, PieCountbySeverity, LineCountbyMonth, MultilineIncidentTop3Country, multipleBarbySeverity
from fire.views import map_station, fire_incidents_map, station_list, station_create, station_detail,station_update, station_delete
from fire.views import delete_location
from fire.views import IncidentList,IncidentCreateView, IncidentUpdateView, IncidentDeleteView
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

    path('location/', views.location_view, name='location'),
    path('location/<int:location_id>/delete/', views.delete_location, name='delete_location'),

    path('stations/', views.station_list, name='station-list'),
    path('stations/create/', views.station_create, name='station-create'),
    path('stations/<int:id>/', views.station_detail, name='station-detail'),
    path('stations/<int:id>/update/', views.station_update, name='station-update'),
    path('stations/<int:id>/delete/', views.station_delete, name='station-delete'),

path('incidents/', IncidentList.as_view(), name='incident-list'),
path('incidents/add/', IncidentCreateView.as_view(), name='incident-add'),
path('incidents/<pk>/', IncidentUpdateView.as_view(), name='incident-update'),
path('incidents/<pk>/delete/', IncidentDeleteView.as_view(), name='incident-delete'),


]