# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PaymentLinkCreateParams", "Customer", "Notify"]


class PaymentLinkCreateParams(TypedDict, total=False):
    amount: Required[int]
    """Amount in the smallest currency unit (e.g., paise)"""

    currency: Required[str]
    """ISO currency code"""

    description: Required[str]
    """Description of the payment link"""

    accept_partial: bool
    """Allow partial payments"""

    callback_method: Literal["get", "post"]
    """HTTP method for callback"""

    callback_url: str
    """Redirect URL after payment"""

    customer: Customer

    expire_by: int
    """Unix timestamp when the link expires"""

    first_min_partial_amount: int
    """Minimum amount for the first partial payment"""

    notes: Dict[str, str]

    notify: Notify

    reference_id: str
    """Unique reference for the payment link"""

    reminder_enable: bool
    """Enable reminders for the payment link"""


class Customer(TypedDict, total=False):
    contact: str

    email: str

    name: str


class Notify(TypedDict, total=False):
    email: bool

    sms: bool
