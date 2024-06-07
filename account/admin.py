from django.contrib import admin
from .models import User,Register,UserProfile


# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('username', 'created_at', 'updated_at')

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('username')

    def __str__(self):
        return self.username
    

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'created_at', 'updated_at')

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('username')

    
    

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'city', 'state', 'zipcode', 'country', 'profile_pic', 'created_at', 'updated_at')
    list_display_links = ('email',)
    list_editable = ('phone_number', 'city','state', 'zipcode', 'country', 'profile_pic')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('email', 'phone_number', 'city','state', 'zipcode', 'country', 'profile_pic')

    class Meta:
        #change the name of the model
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
        #change the name of the app
        
        #change name web page to UreStory
        app_label = 'UreStory'


admin.site.register(Register, RegisterAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
