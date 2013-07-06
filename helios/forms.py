"""
Forms for Helios
"""

from django import forms
from models import Election
from widgets import *
from fields import *

from django.utils.translation import ugettext as _

class ElectionForm(forms.Form):
  short_name = forms.SlugField(label=_('Short name'), max_length=25, help_text=_('no spaces, will be part of the URL for your election, e.g. my-club-2010'))
  name = forms.CharField(label=_('Name'), max_length=100, widget=forms.TextInput(attrs={'size':60}), help_text=_('the pretty name for your election, e.g. My Club 2010 Election'))
  description = forms.CharField(label=_('Description'), max_length=2000, widget=forms.Textarea(attrs={'cols': 70, 'wrap': 'soft'}), required=False)
  election_type = forms.ChoiceField(label=_('Type'), choices = Election.ELECTION_TYPES)
  use_voter_aliases = forms.BooleanField(label=_('Use voter aliases'), required=False, initial=False, help_text=_('If selected, voter identities will be replaced with aliases, e.g. "V12", in the ballot tracking center'))
  #use_advanced_audit_features = forms.BooleanField(required=False, initial=True, help_text='disable this only if you want a simple election with reduced security but a simpler user interface')
  #private_p = forms.BooleanField(required=False, initial=False, label="Private?", help_text='a private election is only visible to registered/eligible voters', widget=forms.HiddenInput)
  private_p = forms.BooleanField(label=_('Private?'), required=False, initial=False, help_text=_('A private election is only visible to registered voters.'))
  

class VoterGroupForm(forms.Form):
  short_name = forms.SlugField(label=_('Short name'), max_length=20, required=True)
  name = forms.CharField(label=_('Name'), max_length=100, required=False)
  weight = forms.IntegerField(label=_('Peso'), min_value=1, required=True, widget=forms.TextInput(attrs={'size':'4'}))


class ElectionTimesForm(forms.Form):
  # times
  voting_starts_at = SplitDateTimeField(help_text = 'UTC date and time when voting begins',
                                   widget=SplitSelectDateTimeWidget)
  voting_ends_at = SplitDateTimeField(help_text = 'UTC date and time when voting ends',
                                   widget=SplitSelectDateTimeWidget)

  
class EmailVotersForm(forms.Form):
  subject = forms.CharField(max_length=80)
  body = forms.CharField(max_length=2000, widget=forms.Textarea)
  send_to = forms.ChoiceField(label="Send To", initial="all", choices= [('all', 'all voters'), ('voted', 'voters who have cast a ballot'), ('not-voted', 'voters who have not yet cast a ballot')])

class TallyNotificationEmailForm(forms.Form):
  subject = forms.CharField(max_length=80)
  body = forms.CharField(max_length=2000, widget=forms.Textarea, required=False)
  send_to = forms.ChoiceField(label="Send To", choices= [('all', 'all voters'), ('voted', 'only voters who cast a ballot'), ('none', 'no one -- are you sure about this?')])

class VoterPasswordForm(forms.Form):
  voter_id = forms.CharField(max_length=50, label="Voter ID")
  password = forms.CharField(widget=forms.PasswordInput(), max_length=100)

