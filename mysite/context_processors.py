from django.conf import settings as django_settings


def settings(request):
    """
    Based on settings configuration expose only a set or all settings to the templates
    """
    settings_in_templates = {}
    if hasattr(django_settings, "TEMPLATE_ALLOWED_SETTINGS"):
        if isinstance(django_settings.TEMPLATE_ALLOWED_SETTINGS, str) and django_settings.TEMPLATE_ALLOWED_SETTINGS.lower() == "all":
            # Expose all settings to the templates
            settings_in_templates = django_settings
        elif isinstance(django_settings.TEMPLATE_ALLOWED_SETTINGS, list):
            # Expose only some settings to the templates.
            for attr in django_settings.TEMPLATE_ALLOWED_SETTINGS: 
                if (hasattr(django_settings, attr)):
                    settings_in_templates[attr] = getattr(django_settings, attr)

    # If configuration is missing return no settings
    return {
        'settings': settings_in_templates,
    }
