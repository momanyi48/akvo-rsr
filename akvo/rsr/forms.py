# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.

"""
Forms and validation code for user registration and updating.

"""

from django import forms

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.sites.models import get_current_site
from django.utils.translation import ugettext_lazy as _

from registration.models import RegistrationProfile

from urlparse import urlsplit, urlunsplit

from .models import Country, Organisation, ProjectUpdate, ProjectUpdateLocation

from akvo import settings


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        max_length=254,
        widget=forms.TextInput(
            attrs={'placeholder': 'Email'}
        ),
    )
    first_name = forms.CharField(
        label='First name',
        max_length=30,
        widget=forms.TextInput(
            attrs={'placeholder': 'First name'}
        ),
    )
    last_name = forms.CharField(
        label='Last name',
        max_length=30,
        widget=forms.TextInput(
            attrs={'placeholder': 'Last name'}
        ),
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password'},
            render_value=False
        )
    )
    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Repeat password'},
            render_value=False
        )
    )

    def clean(self):
        """
        Verify that the values entered into the two password fields match. Note that an error here will end up in
        non_field_errors() because it doesn't apply to a single field.
        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(
                    _(u'Passwords do not match. Please enter the same password in both fields.')
                )
        return self.cleaned_data

    def clean_email(self):
        """
        Verify that the email entered does not exist as an email or username.
        """
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists() \
                or get_user_model().objects.filter(username=email).exists():
            raise forms.ValidationError(_(u'A user with this email address already exists.'))
        return email

    def save(self, request):
        """
        Create the new User and RegistrationProfile, and returns the User.

        This is essentially a light wrapper around RegistrationProfile.objects.create_inactive_user(), feeding it the
        form data and a profile callback (see the documentation on create_inactive_user() for details) if supplied.
        Modified to set user.is_active = False and add User object creation.
        """
        site = get_current_site(request)
        new_user = RegistrationProfile.objects.create_inactive_user(
            username=self.cleaned_data['email'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1'],
            site=site,
        )
        new_user.first_name = self.cleaned_data['first_name']
        new_user.last_name = self.cleaned_data['last_name']
        new_user.is_active = False
        new_user.save()
        return new_user


class ProfileForm(forms.Form):
    email = forms.EmailField(
        label='',
        max_length=254,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email',
                'readonly': True}
        ),
    )
    first_name = forms.CharField(
        label='',
        max_length=30,
        widget=forms.TextInput(
            attrs={'placeholder': 'First name'}
        ),
    )
    last_name = forms.CharField(
        label='',
        max_length=30,
        widget=forms.TextInput(
            attrs={'placeholder': 'Last name'}
        ),
    )

    def save(self, request):
        """
        Update the User profile.
        """
        user = request.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()


class PasswordForm(PasswordChangeForm):
    """
    Custom password form to remove the labels of the form fields.
    """
    old_password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Current password'},
            render_value=False
        )
    )
    new_password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'New password'},
            render_value=False
        )
    )
    new_password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Repeat new password'},
            render_value=False
        )
    )


class UserOrganisationForm(forms.Form):
    organisation = forms.ModelChoiceField(
        queryset=Organisation.objects.all(),
        label='',
        empty_label='Organisation'
    )
    job_title = forms.CharField(
        label='',
        required=False,
        max_length=50,
        widget=forms.TextInput(
            attrs={'placeholder': 'Job title (optional)'}
        ),
    )
    country = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        label='',
        required=False,
        empty_label='Country (optional)'
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserOrganisationForm, self).__init__(*args, **kwargs)

    def clean(self):
        """
        Check that there is no link between user and organisation yet.
        """
        user = self.request.user
        if 'organisation' in self.cleaned_data:
            if self.cleaned_data['organisation'] in user.organisations.all():
                raise forms.ValidationError(
                    _(u'User already linked to organisation.')
                )
        return self.cleaned_data

    def save(self, request):
        """
        Link user to organisation.
        """
        # TODO: The approval process of users
        request.user.organisations.add(self.cleaned_data['organisation'])


class ProjectUpdateForm(forms.ModelForm):
    """Form representing a ProjectUpdate."""

    title = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'input',
        'size': '42',
        'maxlength': '50',
        'placeholder': 'Title',
        }))
    text = forms.CharField(label='', required=False, widget=forms.Textarea(attrs={
        'class': 'textarea',
        'placeholder': 'Description',
        }))
    language = forms.ChoiceField(choices=settings.LANGUAGES, initial='en')
    photo = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        'class': 'input',
        'size': '15',
        }))
    photo_caption = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={
        'class': 'input',
        'size': '25',
        'maxlength': '75',
        'placeholder': 'Photo caption',
        }))
    photo_credit = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={
        'class': 'input',
        'size': '25',
        'maxlength': '25',
        'placeholder': 'Photo credit',
        }))
    video = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'input',
        'size': '42',
        'maxlength': '255',
        'placeholder': 'Video link',
        }))
    video_caption = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={
        'class': 'input',
        'size': '25',
        'maxlength': '75',
        'placeholder': 'Video caption',
        }))
    video_credit = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={
        'class': 'input',
        'size': '25',
        'maxlength': '25',
        'placeholder': 'Video credit',
        }))
    latitude = forms.FloatField(widget=forms.HiddenInput())
    longitude = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = ProjectUpdate
        fields = ('title', 'text', 'language', 'photo', 'photo_caption', 'photo_credit', 'video', 'video_caption',
        'video_credit')

    def clean_video(self):
        data = self.cleaned_data['video']
        if data:
            scheme, netloc, path, query, fragment = urlsplit(data)
            netloc = netloc.lower()
            valid_url = (netloc == 'vimeo.com' or
                         netloc == 'www.youtube.com' and path == '/watch' or
                         netloc == 'youtu.be')
            if not valid_url:
                raise forms.ValidationError(_('Invalid video URL. Currently only YouTube and Vimeo are supported.'))
            if netloc == 'youtu.be':
                netloc = 'www.youtube.com'
                path = '/watch?v=%s' % path.lstrip('/')
                data = urlunsplit((scheme, netloc, path, query, fragment))
        return data

    def save(self, project=None, user=None):
        if project and user:
            # Save update
            update = super(ProjectUpdateForm, self).save(commit=False)
            update.project = project
            update.user = user
            update.update_method = 'W'
            update.save()

            # Save update location
            # Only when adding an update. When editing an update, the initial location is maintained.
            if not update.primary_location:
                latitude_data = self.cleaned_data['latitude']
                longitude_data = self.cleaned_data['longitude']
                ProjectUpdateLocation.objects.create(
                    latitude=latitude_data,
                    longitude=longitude_data,
                    location_target=update,
                )

            return update
        else:
            raise forms.ValidationError('Project or user not found.')


class UserAvatarForm(forms.ModelForm):
    """Form for updating the avatar of a user."""
    avatar = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'input',
        'size': '15',
    }))

    class Meta:
        model = get_user_model()
        fields = ('avatar',)
