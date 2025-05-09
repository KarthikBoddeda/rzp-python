# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["PaymentLink", "Customer", "Notify"]


class Customer(BaseModel):
    contact: Optional[str] = None

    email: Optional[str] = None

    name: Optional[str] = None


class Notify(BaseModel):
    email: Optional[bool] = None

    sms: Optional[bool] = None


class PaymentLink(BaseModel):
    id: Optional[str] = None

    accept_partial: Optional[bool] = None

    amount: Optional[int] = None

    amount_paid: Optional[int] = None

    callback_method: Optional[str] = None

    callback_url: Optional[str] = None

    cancelled_at: Optional[int] = None

    created_at: Optional[int] = None

    currency: Optional[str] = None

    customer: Optional[Customer] = None

    description: Optional[str] = None

    entity: Optional[str] = None

    expire_by: Optional[int] = None

    expired_at: Optional[int] = None

    first_min_partial_amount: Optional[int] = None

    notes: Optional[Dict[str, str]] = None

    notify: Optional[Notify] = None

    payments: Optional[List[object]] = None

    reference_id: Optional[str] = None

    reminder_enable: Optional[bool] = None

    reminders: Optional[List[object]] = None

    short_url: Optional[str] = None

    status: Optional[str] = None

    updated_at: Optional[int] = None

    user_id: Optional[str] = None
