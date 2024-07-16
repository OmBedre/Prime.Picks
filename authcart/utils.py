from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        # Generate a hash value based on user's primary key, timestamp, and active status
        return (
            six.text_type(user.pk) +
            six.text_type(timestamp) +
            six.text_type(user.is_active)
        )

# Instantiate the TokenGenerator to use for generating tokens
generate_token = TokenGenerator()
