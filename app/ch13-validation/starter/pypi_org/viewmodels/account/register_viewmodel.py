from services import user_service
from viewmodels.shared.viewmodelbase import ViewModelBase


class RegisterViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.name = self.request_dict.name
        self.email = self.request_dict.email.lower().strip()
        self.password = self.request_dict.password.strip()

    def validate(self):
        if not self.name or not self.name.strip():
            self.error = 'You must specify a name.'
        elif not self.email or not self.email.strip():
            self.error = 'You must specify an email.'
        elif user_service.find_user_by_email(self.email):
            self.error = 'A user with that email address already exists.'
        elif not self.password:
            self.error = 'You must specify a password.'
        elif len(self.password.strip()) < 5:
            self.error = 'Your password must be at least 5 characters.'
